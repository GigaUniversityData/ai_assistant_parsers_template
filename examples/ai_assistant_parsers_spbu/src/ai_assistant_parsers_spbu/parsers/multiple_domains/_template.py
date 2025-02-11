from bs4 import BeautifulSoup
from ai_assistant_parsers_core.magic_url import MagicURL
from ai_assistant_parsers_core.parsers.utils.clean_blocks import *
from ai_assistant_parsers_core.parsers.utils.restructure_blocks import *
from ai_assistant_parsers_core.parsers import SimpleSelectDomainBaseParser


_ALLOWED_SUBDOMAINS_PATHS = [

]


class ВСТАВИТЬ_ТЕКСТ_СЮДАMultipleDomainsParser(SimpleSelectDomainBaseParser):
    def __init__(self) -> None:
        super().__init__(
            allowed_domains_paths=_ALLOWED_SUBDOMAINS_PATHS,
            select_arguments=["ВСТАВИТЬ_ТЕКСТ_СЮДА"],
        )
