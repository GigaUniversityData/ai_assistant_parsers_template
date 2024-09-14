import asyncio
import sys

from bs4 import BeautifulSoup
from aiohttp import ClientSession
from fake_headers import Headers

from src.settings import PARSERS, PRE_PARSING_REFINERS, POST_PARSING_REFINERS, RESULTS_PATH

from .utils.parsers import (
    get_parser_by_url,
    fetch_html_by_url,
    process_html_by_refiners,
    converts_relative_links_to_absolute,
)


OUTPUT_DIR = RESULTS_PATH / "parse_one"
OUTPUT_DIR.mkdir(exist_ok=True)


async def main() -> None:
    headers = Headers(os="mac", headers=True).generate()
    async with ClientSession(headers=headers) as client:
        await _process_url(client=client)


async def _process_url(client: ClientSession) -> None:
    url = sys.argv[1]

    html = await fetch_html_by_url(url, client=client)
    cleaned_html = _process_html(html, url=url)

    _write_data_to_file(cleaned_html=cleaned_html)


def _process_html(html: str, url: str):
    parser = get_parser_by_url(url, parsers=PARSERS)
    print(type(parser).__name__)

    process_html_by_refiners(html=html, refiners=PRE_PARSING_REFINERS)
    cleaned_html = parser.parse(html)
    converts_relative_links_to_absolute(html=cleaned_html, base_url=url)
    cleaned_html = process_html_by_refiners(html=cleaned_html, refiners=POST_PARSING_REFINERS)

    return cleaned_html


def _write_data_to_file(cleaned_html: str):
    path = OUTPUT_DIR / "result.html"
    prettified_html = BeautifulSoup(cleaned_html, "html5lib").prettify()

    with open(path, "w") as fp:
        fp.write(prettified_html)

    print(f"file://{path.absolute()}")


if __name__ == "__main__":
    asyncio.run(main())
