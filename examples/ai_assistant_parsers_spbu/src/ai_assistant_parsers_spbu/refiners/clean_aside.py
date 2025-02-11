from bs4 import BeautifulSoup
from ai_assistant_parsers_core.magic_url import MagicURL
from ai_assistant_parsers_core.refiners import ABCParsingRefiner
from ai_assistant_parsers_core.parsers.utils.clean_blocks import clean_all_by_select


class CleanASideParsingRefiner(ABCParsingRefiner):
    def refine(self, soup: BeautifulSoup, magic_url: MagicURL) -> None:
        clean_all_by_select(soup, "aside")
