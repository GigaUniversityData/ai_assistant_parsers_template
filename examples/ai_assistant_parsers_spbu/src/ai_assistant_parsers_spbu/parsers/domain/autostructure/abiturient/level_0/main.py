import re
from ai_assistant_parsers_core.magic_url import MagicURL
from bs4 import BeautifulSoup

from ai_assistant_parsers_core.parsers.utils.clean_blocks import (
    clean_one_by_select,
    clean_one_by_find,
    clean_all_by_select,
)
from ai_assistant_parsers_core.parsers.utils.restructure_blocks import rename_all_by_select
from ai_assistant_parsers_core.parsers import SimpleSelectDomainBaseParser


class AbiturientDomainParser(SimpleSelectDomainBaseParser):
    def __init__(self) -> None:
        super().__init__(
            allowed_domains_paths=["abiturient.spbu.ru"],
            select_arguments=[".page-main"],
            excluded_paths=["/", "/events/*", "/reception-foreign/", "/info/general-info/dni-otkrytykh-dverey/"],
        )

    def _clean_parsed_html(self, soup: BeautifulSoup, magic_url: MagicURL) -> None:
        clean_one_by_select(soup, ".page-main > aside")

        clean_one_by_select(soup, ".information")
        clean_one_by_select(soup, ".footnote.footer-note")
        clean_one_by_find(soup, dict(id=re.compile(r"news_\d+")))

    def _restructure_parsed_html(self, soup: BeautifulSoup, magic_url: MagicURL) -> None:
        # https://abiturient.spbu.ru/info/general-info/
        clean_all_by_select(soup, "button.useful-info__link")  # Кнопки "подробнее" не нужны из-за кривой структуры
        rename_all_by_select(
            soup,
            "h2.info-definition__title",
            "h4",
        )

        # https://abiturient.spbu.ru/programs/voennyy-uchebnyy-tsentr/
        rename_all_by_select(soup, ".accordion__button > span", "h3")
