from bs4 import BeautifulSoup
from ai_assistant_parsers_core.parsers import SimpleSelectDomainBaseParser
from ai_assistant_parsers_core.magic_url import MagicURL
from ai_assistant_parsers_core.parsers.utils.clean_blocks import *
from ai_assistant_parsers_core.parsers.utils.restructure_blocks import *


class VseObrashcheniya412DirektoraInstitutovDirectorCognitivnyeIssledovaniyaGuestbookDomainParser(SimpleSelectDomainBaseParser):
    def __init__(self) -> None:
        super().__init__(
            allowed_domains_paths=["guestbook.spbu.ru"],
            included_paths=["/vse-obrashcheniya/412-direktora-institutov/director-cognitivnye-issledovaniya/*"],
            select_arguments=[],
        )
