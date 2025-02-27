from bs4 import BeautifulSoup
from ai_assistant_parsers_core.parsers import SimpleSelectDomainBaseParser
from ai_assistant_parsers_core.magic_url import MagicURL
from ai_assistant_parsers_core.parsers.utils.clean_blocks import *
from ai_assistant_parsers_core.parsers.utils.restructure_blocks import *


class D0BaD0BeD0BdD182D0B0D0BaD182D18B88D0BfD0B0D181D0BfD0BeD180D182D0BdD0BeD0B2D0B8D0B7D0BeD0B2D18BD0B9D0BeD182D0B4D0B5D0BbD0B3D0BbD0B0D0B2D0BdD0BeD0B3D0BeD183D0BfD180D0B0D0B2D0BbD0B5D0BdD0B8D18FD0B0D0B4D0BcD0B8D0BdD0B8D181D182D180D0B8D180D0BeD0B2D0B0D0BdD0B8D18FD182D180D183D0B4D0BeD0B2D18BD185D0BeD182D0BdD0BeD188D0B5D0BdD0B8D0B9D0B8D0B4D0BeD0BaD183D0BcD0B5D0BdD182D0BeD0BeD0B1D0BeD180D0BeD182D0BeD0B2D181D0BfD0B1D0B3D183D0BfD0B2D0BeIfeaDomainParser(SimpleSelectDomainBaseParser):
    def __init__(self) -> None:
        super().__init__(
            allowed_domains_paths=["ifea.spbu.ru"],
            included_paths=["/%D0%BA%D0%BE%D0%BD%D1%82%D0%B0%D0%BA%D1%82%D1%8B/88-%D0%BF%D0%B0%D1%81%D0%BF%D0%BE%D1%80%D1%82%D0%BD%D0%BE-%D0%B2%D0%B8%D0%B7%D0%BE%D0%B2%D1%8B%D0%B9-%D0%BE%D1%82%D0%B4%D0%B5%D0%BB-%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%BE%D0%B3%D0%BE-%D1%83%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F-%D0%B0%D0%B4%D0%BC%D0%B8%D0%BD%D0%B8%D1%81%D1%82%D1%80%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F-%D1%82%D1%80%D1%83%D0%B4%D0%BE%D0%B2%D1%8B%D1%85-%D0%BE%D1%82%D0%BD%D0%BE%D1%88%D0%B5%D0%BD%D0%B8%D0%B9-%D0%B8-%D0%B4%D0%BE%D0%BA%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D0%BE%D0%BE%D0%B1%D0%BE%D1%80%D0%BE%D1%82%D0%BE%D0%B2-%D1%81%D0%BF%D0%B1%D0%B3%D1%83-%D0%BF%D0%B2%D0%BE/*"],
            select_arguments=[],
        )
