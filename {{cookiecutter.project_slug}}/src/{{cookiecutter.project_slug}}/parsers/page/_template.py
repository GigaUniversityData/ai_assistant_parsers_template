from bs4 import BeautifulSoup

from ai_assistant_parsers_core.parsers.utils.clean_blocks import *
from ai_assistant_parsers_core.parsers.utils.restructure_blocks import *
from ai_assistant_parsers_core.parsers import SimpleSelectDomainBaseParser


class ВСТАВИТЬ_ТЕКСТ_СЮДАPageParser(SimpleSelectDomainBaseParser):
    def __init__(self) -> None:
        super().__init__(
            allowed_domains_paths=["ВСТАВИТЬ_ТЕКСТ_СЮДА"],
            included_paths=["ВСТАВИТЬ_ТЕКСТ_СЮДА"],
            select_arguments=["ВСТАВИТЬ_ТЕКСТ_СЮДА"],
        )
