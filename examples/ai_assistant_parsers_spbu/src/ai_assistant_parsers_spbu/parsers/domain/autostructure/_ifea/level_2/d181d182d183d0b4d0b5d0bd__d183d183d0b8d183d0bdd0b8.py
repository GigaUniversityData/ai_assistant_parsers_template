from bs4 import BeautifulSoup
from ai_assistant_parsers_core.parsers import SimpleSelectDomainBaseParser
from ai_assistant_parsers_core.magic_url import MagicURL
from ai_assistant_parsers_core.parsers.utils.clean_blocks import *
from ai_assistant_parsers_core.parsers.utils.restructure_blocks import *


class D181D182D183D0B4D0B5D0BdD187D0B5D181D0BaD0B8D0B9D0BeD0B1D0BcD0B5D0Bd122D183D183D0B8D183D0BdD0B8IfeaDomainParser(SimpleSelectDomainBaseParser):
    def __init__(self) -> None:
        super().__init__(
            allowed_domains_paths=["ifea.spbu.ru"],
            included_paths=["/%D1%81%D1%82%D1%83%D0%B4%D0%B5%D0%BD%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9-%D0%BE%D0%B1%D0%BC%D0%B5%D0%BD/122-%D1%83%D1%83-%D0%B8-%D1%83%D0%BD%D0%B8/*"],
            select_arguments=[],
        )
