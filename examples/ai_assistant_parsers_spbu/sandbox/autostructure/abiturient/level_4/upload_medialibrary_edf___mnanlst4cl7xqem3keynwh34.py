from bs4 import BeautifulSoup
from ai_assistant_parsers_core.parsers import SimpleSelectDomainBaseParser
from ai_assistant_parsers_core.magic_url import MagicURL
from ai_assistant_parsers_core.parsers.utils.clean_blocks import *
from ai_assistant_parsers_core.parsers.utils.restructure_blocks import *


class UploadMedialibraryEdfCi4Qt2Ammnanlst4Cl7Xqem3Keynwh34AbiturientDomainParser(SimpleSelectDomainBaseParser):
    def __init__(self) -> None:
        super().__init__(
            allowed_domains_paths=["abiturient.spbu.ru"],
            included_paths=["/upload/medialibrary/edf/ci4qt2ammnanlst4cl7xqem3keynwh34/*"],
            select_arguments=[],
        )
