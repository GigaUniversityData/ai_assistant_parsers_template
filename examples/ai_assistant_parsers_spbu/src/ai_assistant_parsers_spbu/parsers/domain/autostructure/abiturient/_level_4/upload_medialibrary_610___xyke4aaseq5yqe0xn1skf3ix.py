from bs4 import BeautifulSoup
from ai_assistant_parsers_core.parsers import SimpleSelectDomainBaseParser
from ai_assistant_parsers_core.magic_url import MagicURL
from ai_assistant_parsers_core.parsers.utils.clean_blocks import *
from ai_assistant_parsers_core.parsers.utils.restructure_blocks import *


class UploadMedialibrary610X7Djffnqxyke4Aaseq5Yqe0Xn1Skf3IxAbiturientDomainParser(SimpleSelectDomainBaseParser):
    def __init__(self) -> None:
        super().__init__(
            allowed_domains_paths=["abiturient.spbu.ru"],
            included_paths=["/upload/medialibrary/610/x7djffnqxyke4aaseq5yqe0xn1skf3ix/*"],
            select_arguments=[],
        )
