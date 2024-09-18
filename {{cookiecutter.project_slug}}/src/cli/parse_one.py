import asyncio
import sys

from bs4 import BeautifulSoup
from aiohttp import ClientSession
from fake_headers import Headers
from ai_assistant_parsers_core.common_utils.beautiful_soup import converts_relative_links_to_absolute
from ai_assistant_parsers_core.turn_html_into_markdown import turn_html_into_markdown

from src.settings import PARSERS, PARSING_REFINERS, RESULTS_PATH

from .utils.parsers import (
    get_parser_by_url,
    fetch_html_by_url,
    process_html_by_refiners,
)


OUTPUT_DIR = RESULTS_PATH / "parse_one"
OUTPUT_DIR.mkdir(exist_ok=True)


async def main() -> None:
    url = sys.argv[1]

    headers = Headers(os="mac", headers=True).generate()
    async with ClientSession(headers=headers) as client:
        await _process_url(client=client, url=url)


async def _process_url(client: ClientSession, url: str) -> None:
    html = await fetch_html_by_url(url, client=client)
    cleaned_soup = _process_html(html, url=url)

    _write_data_to_files(cleaned_soup=cleaned_soup)


def _process_html(html: str, url: str) -> BeautifulSoup:
    soup = BeautifulSoup(html, "html5lib")

    parser = get_parser_by_url(url, parsers=PARSERS)
    print(type(parser).__name__)

    cleaned_soup = parser.parse(soup)
    converts_relative_links_to_absolute(soup=cleaned_soup, base_url=url)
    process_html_by_refiners(soup=cleaned_soup, refiners=PARSING_REFINERS)

    return soup


def _write_data_to_files(cleaned_soup: BeautifulSoup) -> None:
    html = str(cleaned_soup)

    path = OUTPUT_DIR / "result.html"
    with open(path, "w") as fp:
        fp.write(html)
    print(f"file://{path.absolute()}")

    path = OUTPUT_DIR / "result.md"
    with open(path, "w") as fp:
        fp.write(turn_html_into_markdown(html))

    print(f"file://{path.absolute()}")



if __name__ == "__main__":
    asyncio.run(main())
