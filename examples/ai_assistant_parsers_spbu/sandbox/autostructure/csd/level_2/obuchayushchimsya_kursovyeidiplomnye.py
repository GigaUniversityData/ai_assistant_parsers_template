from bs4 import BeautifulSoup
from ai_assistant_parsers_core.parsers import SimpleSelectDomainBaseParser
from ai_assistant_parsers_core.magic_url import MagicURL
from ai_assistant_parsers_core.parsers.utils.clean_blocks import *
from ai_assistant_parsers_core.parsers.utils.restructure_blocks import *


class ObuchayushchimsyaKursovyeIDiplomnyeCsdDomainParser(SimpleSelectDomainBaseParser):
    def __init__(self) -> None:
        super().__init__(
            allowed_domains_paths=["csd.spbu.ru"],
            included_paths=["/obuchayushchimsya/kursovye-i-diplomnye/*"],
            select_arguments=[],
        )
