from bs4 import BeautifulSoup
from ai_assistant_parsers_core.parsers import SimpleSelectDomainBaseParser
from ai_assistant_parsers_core.magic_url import MagicURL
from ai_assistant_parsers_core.parsers.utils.clean_blocks import *
from ai_assistant_parsers_core.parsers.utils.restructure_blocks import *


class EnDirectorsOfInstitutesSIDudnik71VseObrashcheniyaNachalnikiUpravlenijYpravPoOrgPriemaGuestbookDomainParser(SimpleSelectDomainBaseParser):
    def __init__(self) -> None:
        super().__init__(
            allowed_domains_paths=["guestbook.spbu.ru"],
            included_paths=["/en/directors-of-institutes/s-i-dudnik/71-vse-obrashcheniya/nachalniki-upravlenij/yprav-po-org-priema/*"],
            select_arguments=[],
        )
