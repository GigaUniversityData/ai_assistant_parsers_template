from bs4 import BeautifulSoup
from ai_assistant_parsers_core.parsers import SimpleSelectDomainBaseParser
from ai_assistant_parsers_core.magic_url import MagicURL
from ai_assistant_parsers_core.parsers.utils.clean_blocks import *
from ai_assistant_parsers_core.parsers.utils.restructure_blocks import *


class N35UchebnoeUpravlenieIzuchenieAnglijskogoYazykaObuchayushchimisyaOsnovnykhObrazovatelnykhProgrammBakalavriataISpetsialitetaEduDomainParser(SimpleSelectDomainBaseParser):
    def __init__(self) -> None:
        super().__init__(
            allowed_domains_paths=["edu.spbu.ru"],
            included_paths=["/35-uchebnoe-upravlenie/izuchenie-anglijskogo-yazyka-obuchayushchimisya-osnovnykh-obrazovatelnykh-programm-bakalavriata-i-spetsialiteta/*"],
            select_arguments=[],
        )
