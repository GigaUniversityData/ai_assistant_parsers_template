from bs4 import BeautifulSoup
from ai_assistant_parsers_core.parsers import SimpleSelectDomainBaseParser
from ai_assistant_parsers_core.magic_url import MagicURL
from ai_assistant_parsers_core.parsers.utils.clean_blocks import *
from ai_assistant_parsers_core.parsers.utils.restructure_blocks import *


class UploadMedialibraryD865Bh2Nqmd1K5Qokeuj6Cycmpz8Nalfh83AbiturientDomainParser(SimpleSelectDomainBaseParser):
    def __init__(self) -> None:
        super().__init__(
            allowed_domains_paths=["abiturient.spbu.ru"],
            included_paths=["/upload/medialibrary/d86/5bh2nqmd1k5qokeuj6cycmpz8nalfh83/*"],
            select_arguments=[],
        )
