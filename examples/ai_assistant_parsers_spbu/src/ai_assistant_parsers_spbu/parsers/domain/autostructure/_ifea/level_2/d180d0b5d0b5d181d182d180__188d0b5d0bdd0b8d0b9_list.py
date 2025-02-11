from bs4 import BeautifulSoup
from ai_assistant_parsers_core.parsers import SimpleSelectDomainBaseParser
from ai_assistant_parsers_core.magic_url import MagicURL
from ai_assistant_parsers_core.parsers.utils.clean_blocks import *
from ai_assistant_parsers_core.parsers.utils.restructure_blocks import *


class D180D0B5D0B5D181D182D180D0BcD0B5D0B6D0B4D183D0BdD0B0D180D0BeD0B4D0BdD18BD185D181D0BeD0B3D0BbD0B0D188D0B5D0BdD0B8D0B9ListIfeaDomainParser(SimpleSelectDomainBaseParser):
    def __init__(self) -> None:
        super().__init__(
            allowed_domains_paths=["ifea.spbu.ru"],
            included_paths=["/%D1%80%D0%B5%D0%B5%D1%81%D1%82%D1%80-%D0%BC%D0%B5%D0%B6%D0%B4%D1%83%D0%BD%D0%B0%D1%80%D0%BE%D0%B4%D0%BD%D1%8B%D1%85-%D1%81%D0%BE%D0%B3%D0%BB%D0%B0%D1%88%D0%B5%D0%BD%D0%B8%D0%B9/list/*"],
            select_arguments=[],
        )
