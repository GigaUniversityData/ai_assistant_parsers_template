from bs4 import BeautifulSoup

from ai_assistant_parsers_core.parsers.utils.clean_blocks import *
from ai_assistant_parsers_core.parsers.utils.restructure_blocks import *
from ai_assistant_parsers_core.parsers import SimpleSelectPageBaseParser


class ВСТАВИТЬ_ТЕКСТ_СЮДАPageParser(SimpleSelectPageBaseParser):
    def __init__(self) -> None:
        super().__init__(
            allowed_paths=["ВСТАВИТЬ_ТЕКСТ_СЮДА"],
            select_arguments=["ВСТАВИТЬ_ТЕКСТ_СЮДА"],
        )
