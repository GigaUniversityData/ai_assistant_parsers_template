import asyncio
import sys
import json
from pathlib import Path

from bs4 import BeautifulSoup
from aiohttp import ClientSession
from fake_headers import Headers
from ai_assistant_parsers_core.common_utils.beautiful_soup import converts_relative_links_to_absolute
from ai_assistant_parsers_core.common_utils.parse_url import extract_url
from ai_assistant_parsers_core.turn_html_into_markdown import turn_html_into_markdown
from ai_assistant_parsers_core.parsers import ABCParser

from src.settings import PARSERS, PARSING_REFINERS, RESULTS_PATH

from .utils.parsers import (
    get_parser_by_url,
    fetch_html_by_url,
    process_html_by_refiners,
    hash_string,
    get_full_parser_name,
)


async def parse_one(url: str, output_dir: Path):
    output_dir.mkdir(exist_ok=True, parents=True)

    headers = Headers(os="mac", headers=True).generate()
    async with ClientSession(headers=headers) as client:
        await _process_url(client=client, url=url, output_dir=output_dir)


async def _process_url(client: ClientSession, url: str, output_dir: Path) -> None:
    html = await fetch_html_by_url(url, client=client)
    cleaned_soup, parser = _process_html(html, url=url)

    _write_data_to_files(cleaned_soup=cleaned_soup, url=url, parser=parser, output_dir=output_dir)


def _process_html(html: str, url: str) -> tuple[BeautifulSoup, ABCParser]:
    soup = BeautifulSoup(html, "html5lib")

    parser = get_parser_by_url(url, parsers=PARSERS)

    cleaned_soup = parser.parse(soup)
    converts_relative_links_to_absolute(soup=cleaned_soup, base_url=url)
    process_html_by_refiners(soup=cleaned_soup, refiners=PARSING_REFINERS)

    return soup, parser


def _write_data_to_files(cleaned_soup: BeautifulSoup, url: str, parser: ABCParser, output_dir: Path) -> None:
    url_hash = f"{extract_url(url).subdomain}_{hash_string(url)}"
    parser_name = get_full_parser_name(parser)
    html = str(cleaned_soup)

    result_dir = output_dir / url_hash
    result_dir.mkdir(exist_ok=True)

    print(parser_name)

    path = result_dir / "result.html"
    with open(path, "w") as fp:
        fp.write(html)
    print(f"file://{path.absolute()}")

    path = result_dir / "result.md"
    with open(path, "w") as fp:
        fp.write(turn_html_into_markdown(html))

    print(f"file://{path.absolute()}")

    metadata = {"parser_name": parser_name, "url": url, "hash": url_hash}
    path = result_dir / "meta.json"
    with open(path, "w") as fp:
        json.dump(metadata, fp=fp, indent=4)


async def _main() -> None:
    url = sys.argv[1]

    await parse_one(url=url, output_dir=RESULTS_PATH / "parse_one")


if __name__ == "__main__":
    asyncio.run(_main())
