from bs4 import BeautifulSoup
from aiohttp import ClientSession

from ai_assistant_parsers_core.parsers import ABCParser
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


def process_html_by_refiners(soup: BeautifulSoup, refiners: list[ABCParsingRefiner]) -> None:
    for parsing_refiner in refiners:
        parsing_refiner.refine(soup)
