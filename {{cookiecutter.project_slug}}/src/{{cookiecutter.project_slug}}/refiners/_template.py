from bs4 import BeautifulSoup

from ai_assistant_parsers_core.refiners import ABCParsingRefiner
from ai_assistant_parsers_core.parsers.utils.clean_blocks import *
from ai_assistant_parsers_core.parsers.utils.restructure_blocks import *


class CleanASideParsingRefiner(ABCParsingRefiner):
    def refine(self, soup: BeautifulSoup, url: str) -> None:
        ...
