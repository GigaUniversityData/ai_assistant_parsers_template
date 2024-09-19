from bs4 import BeautifulSoup

from ai_assistant_parsers_core.parsers.utils.clean_blocks import clean_one_by_select
from ai_assistant_parsers_core.parsers.utils.restructure_blocks import rename_all_by_select
from ai_assistant_parsers_core.parsers import SimpleSelectDomainBaseParser


class WWWDomainParser(SimpleSelectDomainBaseParser):
    def __init__(self) -> None:
        super().__init__(
            allowed_domains_paths=["spbu.ru"],
            select_arguments=[".page-main-content"],
            excluded_paths=["/history/*"],
        )

    def _clean_parsed_html(self, soup: BeautifulSoup) -> None:
        clean_one_by_select(soup, '.constructor-box:has(> .box-title > :-soup-contains-own("Новости"))')
        clean_one_by_select(soup, '.constructor-box:has(> .box-title:-soup-contains-own("Участвовать в жизни сообщества выпускников"))')

        clean_one_by_select(soup, "aside.constructor-aside")  # https://spbu.ru/nauka/nauchnaya-biblioteka-imeni-m-gorkogo
        clean_one_by_select(soup, "aside:has(> #block-spbgu-spbgu-block-2)")  # https://spbu.ru/openuniversity/documents/ekspertnoe-zaklyuchenie-po-informacionnym-materialam-zaprosa-ministerstva
        clean_one_by_select(soup, "#spbgu-pages-documents-search-form")  # https://spbu.ru/openuniversity/documents
        clean_one_by_select(soup, "#spbgu-pages-programm-contact-form")  # https://spbu.ru/postupayushchim/programms/dopolnitelnyeprogrammy/bezopasnost-truda-na-obektakh-khimicheskoy
        clean_one_by_select(soup, "#block-spbgu-spbgu-block-10:has(.card-list)")  # https://spbu.ru/postupayushchim/programms/aspirantura/gidrogeologiya
        clean_one_by_select(soup, ".constructor-box:has(> div > .sidebar__content > #spbgu-pages-crm-recomendation-form)")  # https://spbu.ru/postupayushchim/programms/magistratura/poluchit-rekomendacii-po-postupleniyu
        # https://spbu.ru/postupayushchim, https://spbu.ru/postupayushchim/programms/bakalavriat
        clean_one_by_select(soup, ".page-headline-ver__btns")
        clean_one_by_select(soup, "#form-filter")

    def _restructure_parsed_html(self, soup: BeautifulSoup) -> None:
        # Headers
        rename_all_by_select(soup, "div.collapse__bt", "h2")
        rename_all_by_select(soup, "div.table-programs__title", "h2")
        rename_all_by_select(soup, ".contacts-headline__adress > span", "h2")

        # Table
        rename_all_by_select(soup, "div.table,.table-float", "table")
        rename_all_by_select(soup, "div.table__hrow,.table__row", "tr")
        rename_all_by_select(soup, "div.table__cell", "td")
        rename_all_by_select(soup, ".table__hrow > td.table__cell", "th")
