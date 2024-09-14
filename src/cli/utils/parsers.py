from bs4 import BeautifulSoup
from aiohttp import ClientSession

from src.parsers import ABCParser
from ai_assistant_parsers_core.common_utils.beautiful_soup import (
    converts_relative_links_to_absolute as converts_relative_links_to_absolute_by_soup,
)
from ai_assistant_parsers_core.refiners import ABCParsingRefiner


def get_parser_by_url(url: str, parsers: list[ABCParser]) -> ABCParser:
    for parser in parsers:
        if parser.check(url=url):
            return parser
    raise RuntimeError


async def fetch_html_by_url(url: str, client: ClientSession) -> str:
    async with client.get(url) as response:
        try:
            return await response.text()
        except UnicodeDecodeError:
            return await response.text(encoding="windows-1251")


def process_html_by_refiners(html: str, refiners: list[ABCParsingRefiner]) -> str:
    for parsing_refiner in refiners:
        html = parsing_refiner.refine(html)
    return html


def converts_relative_links_to_absolute(html: str, base_url: str):
    soup = BeautifulSoup(html, "html5lib")

    converts_relative_links_to_absolute_by_soup(soup, base_url=base_url)

    return str(soup)
