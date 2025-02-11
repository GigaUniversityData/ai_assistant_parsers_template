from bs4 import BeautifulSoup
from ai_assistant_parsers_core.parsers import SimpleSelectDomainBaseParser
from ai_assistant_parsers_core.magic_url import MagicURL
from ai_assistant_parsers_core.parsers.utils.clean_blocks import *
from ai_assistant_parsers_core.parsers.utils.restructure_blocks import *


class UchebnayaDeyatelnostStudentuSlushatelyu11UchebnoeUpravlenieStudentuSlushatelyuEduDomainParser(SimpleSelectDomainBaseParser):
    def __init__(self) -> None:
        super().__init__(
            allowed_domains_paths=["edu.spbu.ru"],
            included_paths=["/uchebnaya-deyatelnost/studentu-slushatelyu/11-uchebnoe-upravlenie/studentu-slushatelyu/*"],
            select_arguments=[],
        )
