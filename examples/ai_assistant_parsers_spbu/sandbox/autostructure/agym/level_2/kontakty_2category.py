from bs4 import BeautifulSoup
from ai_assistant_parsers_core.parsers import SimpleSelectDomainBaseParser
from ai_assistant_parsers_core.magic_url import MagicURL
from ai_assistant_parsers_core.parsers.utils.clean_blocks import *
from ai_assistant_parsers_core.parsers.utils.restructure_blocks import *


class Kontakty2CategoryAgymDomainParser(SimpleSelectDomainBaseParser):
    def __init__(self) -> None:
        super().__init__(
            allowed_domains_paths=["agym.spbu.ru"],
            included_paths=["/kontakty/2-category/*"],
            select_arguments=[],
        )
