from bs4 import BeautifulSoup
from ai_assistant_parsers_core.parsers import SimpleSelectDomainBaseParser
from ai_assistant_parsers_core.magic_url import MagicURL
from ai_assistant_parsers_core.parsers.utils.clean_blocks import *
from ai_assistant_parsers_core.parsers.utils.restructure_blocks import *


class D0B7D0B0D180D183D0B1D0B5D0B6D0BdD18BD0B5D0BfD0B0D180D182D0BdD191D180D18B126D0BfD0B2D0BeD0B8D183D0BdD0B8IfeaDomainParser(SimpleSelectDomainBaseParser):
    def __init__(self) -> None:
        super().__init__(
            allowed_domains_paths=["ifea.spbu.ru"],
            included_paths=["/%D0%B7%D0%B0%D1%80%D1%83%D0%B1%D0%B5%D0%B6%D0%BD%D1%8B%D0%B5-%D0%BF%D0%B0%D1%80%D1%82%D0%BD%D1%91%D1%80%D1%8B/126-%D0%BF%D0%B2%D0%BE-%D0%B8-%D1%83%D0%BD%D0%B8/*"],
            select_arguments=[],
        )
