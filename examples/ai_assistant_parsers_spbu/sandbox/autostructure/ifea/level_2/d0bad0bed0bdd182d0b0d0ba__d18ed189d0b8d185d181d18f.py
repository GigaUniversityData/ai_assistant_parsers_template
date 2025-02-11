from bs4 import BeautifulSoup
from ai_assistant_parsers_core.parsers import SimpleSelectDomainBaseParser
from ai_assistant_parsers_core.magic_url import MagicURL
from ai_assistant_parsers_core.parsers.utils.clean_blocks import *
from ai_assistant_parsers_core.parsers.utils.restructure_blocks import *


class D0BaD0BeD0BdD182D0B0D0BaD182D18B90D183D0BfD180D0B0D0B2D0BbD0B5D0BdD0B8D0B5D0BfD0BeD0BeD180D0B3D0B0D0BdD0B8D0B7D0B0D186D0B8D0B8D0BfD180D0B8D191D0BcD0B0D0BeD0B1D183D187D0B0D18ED189D0B8D185D181D18FIfeaDomainParser(SimpleSelectDomainBaseParser):
    def __init__(self) -> None:
        super().__init__(
            allowed_domains_paths=["ifea.spbu.ru"],
            included_paths=["/%D0%BA%D0%BE%D0%BD%D1%82%D0%B0%D0%BA%D1%82%D1%8B/90-%D1%83%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5-%D0%BF%D0%BE-%D0%BE%D1%80%D0%B3%D0%B0%D0%BD%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D0%B8-%D0%BF%D1%80%D0%B8%D1%91%D0%BC%D0%B0-%D0%BE%D0%B1%D1%83%D1%87%D0%B0%D1%8E%D1%89%D0%B8%D1%85%D1%81%D1%8F/*"],
            select_arguments=[],
        )
