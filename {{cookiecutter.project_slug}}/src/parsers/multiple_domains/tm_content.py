from bs4 import BeautifulSoup

from ai_assistant_parsers_core.parsers.utils.clean_blocks import clean_one_by_select, clean_all_by_select
from ai_assistant_parsers_core.parsers import SimpleSelectDomainBaseParser


_ALLOWED_SUBDOMAINS_PATHS = [
    "students.spbu.ru",
    "nauka.spbu.ru",
    "mil.spbu.ru",
    "ifea.spbu.ru",
    "guestbook.spbu.ru",
    "edu.spbu.ru",
    "horizont.spbu.ru",
    "diaghilevmuseum.spbu.ru",
    "cdop.chem.spbu.ru",
    "agym.spbu.ru",
    "philosophy.spbu.ru",
    "apmath.spbu.ru",
    "csd.spbu.ru",

    "theology.spbu.ru",
    "history.spbu.ru",
    "politology.spbu.ru",
    "phys.spbu.ru",
    "mathphys.spbu.ru",
    "sport.spbu.ru",
    "nanomaterials.spbu.ru",

    "hr.spbu.ru",
    "unipat.spbu.ru",
    "library.spbu.ru",
    "it.spbu.ru",
    "history.museums.spbu.ru",
]


class TMContentParser(SimpleSelectDomainBaseParser):
    def __init__(self) -> None:
        super().__init__(
            allowed_domains_paths=_ALLOWED_SUBDOMAINS_PATHS,
            select_arguments=["#tm-content"],
        )

    def _clean_parsed_html(self, soup: BeautifulSoup) -> None:
        # https://students.spbu.ru/mmen-novosti.html
        clean_one_by_select(soup, "ul.uk-breadcrumb")  # Breadcrumbs

        # https://students.spbu.ru/mmen-novosti.html
        clean_one_by_select(soup, "ul.uk-pagination")  # Пагинация

        # https://students.spbu.ru/mmen-meroprijatija.html
        clean_all_by_select(soup, '.uk-grid:has(> div > .uk-panel > .uk-panel-title:-soup-contains-own("Еще статьи"))')  # "Ещё статьи..."

        # https://guestbook.spbu.ru/prorektory-spbgu/prorector-obr/3052-ob-udostovereniyakh-aspirantov.html
        clean_all_by_select(soup, '.uk-list:has(> li:-soup-contains-own("Просмотров: "))')  # Число просмотров
