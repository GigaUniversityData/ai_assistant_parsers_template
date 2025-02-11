from bs4 import BeautifulSoup
from ai_assistant_parsers_core.parsers import SimpleSelectDomainBaseParser
from ai_assistant_parsers_core.magic_url import MagicURL
from ai_assistant_parsers_core.parsers.utils.clean_blocks import *
from ai_assistant_parsers_core.parsers.utils.restructure_blocks import *


class UploadMedialibrary87ES073Upqgcrb6Erd4Z1Ggdkq6Bawv2Zf7AbiturientDomainParser(SimpleSelectDomainBaseParser):
    def __init__(self) -> None:
        super().__init__(
            allowed_domains_paths=["abiturient.spbu.ru"],
            included_paths=["/upload/medialibrary/87e/s073upqgcrb6erd4z1ggdkq6bawv2zf7/*"],
            select_arguments=[],
        )
