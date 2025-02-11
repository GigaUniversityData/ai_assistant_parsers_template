from bs4 import BeautifulSoup
from ai_assistant_parsers_core.parsers import SimpleSelectDomainBaseParser
from ai_assistant_parsers_core.magic_url import MagicURL
from ai_assistant_parsers_core.parsers.utils.clean_blocks import *
from ai_assistant_parsers_core.parsers.utils.restructure_blocks import *


class FakultetOtdelyIKomissiiUchebnyjOtdel17DepartmentsAndCommissionsApmathDomainParser(SimpleSelectDomainBaseParser):
    def __init__(self) -> None:
        super().__init__(
            allowed_domains_paths=["apmath.spbu.ru"],
            included_paths=["/fakultet/otdely-i-komissii/uchebnyj-otdel/17-departments-and-commissions/*"],
            select_arguments=[],
        )
