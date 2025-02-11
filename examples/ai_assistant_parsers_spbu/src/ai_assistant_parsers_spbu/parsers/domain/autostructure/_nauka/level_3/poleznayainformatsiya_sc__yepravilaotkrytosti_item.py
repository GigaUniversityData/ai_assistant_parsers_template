from bs4 import BeautifulSoup
from ai_assistant_parsers_core.parsers import SimpleSelectDomainBaseParser
from ai_assistant_parsers_core.magic_url import MagicURL
from ai_assistant_parsers_core.parsers.utils.clean_blocks import *
from ai_assistant_parsers_core.parsers.utils.restructure_blocks import *


class PoleznayaInformatsiyaScienceVvoditNovyePravilaOtkrytostiItemNaukaDomainParser(SimpleSelectDomainBaseParser):
    def __init__(self) -> None:
        super().__init__(
            allowed_domains_paths=["nauka.spbu.ru"],
            included_paths=["/poleznaya-informatsiya/science-vvodit-novye-pravila-otkrytosti/item/*"],
            select_arguments=[],
        )
