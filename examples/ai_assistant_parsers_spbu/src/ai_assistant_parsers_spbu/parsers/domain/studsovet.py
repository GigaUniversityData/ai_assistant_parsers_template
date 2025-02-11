from bs4 import BeautifulSoup
from ai_assistant_parsers_core.magic_url import MagicURL
from ai_assistant_parsers_core.parsers.utils.clean_blocks import clean_all_by_select, clean_one_by_select
from ai_assistant_parsers_core.parsers import SimpleSelectDomainBaseParser


class StudsovetDomainParser(SimpleSelectDomainBaseParser):
    def __init__(self) -> None:
        super().__init__(
            allowed_domains_paths=["studsovet.spbu.ru"],
            select_arguments=["main"],
        )

    def _clean_parsed_html(self, soup: BeautifulSoup, magic_url: MagicURL) -> None:
        clean_all_by_select(soup, ".icons:has(> .btn-group > button[id^=dropdownMenuButton-])")
        clean_one_by_select(soup, ".pagination")
