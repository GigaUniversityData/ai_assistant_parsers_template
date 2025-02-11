from bs4 import BeautifulSoup
from ai_assistant_parsers_core.parsers import SimpleSelectDomainBaseParser
from ai_assistant_parsers_core.magic_url import MagicURL
from ai_assistant_parsers_core.parsers.utils.clean_blocks import *
from ai_assistant_parsers_core.parsers.utils.restructure_blocks import *


class UploadMedialibrary37DT38Cp12Vmxg77E28Krup06Fn36Gc812SAbiturientDomainParser(SimpleSelectDomainBaseParser):
    def __init__(self) -> None:
        super().__init__(
            allowed_domains_paths=["abiturient.spbu.ru"],
            included_paths=["/upload/medialibrary/37d/t38cp12vmxg77e28krup06fn36gc812s/*"],
            select_arguments=[],
        )
