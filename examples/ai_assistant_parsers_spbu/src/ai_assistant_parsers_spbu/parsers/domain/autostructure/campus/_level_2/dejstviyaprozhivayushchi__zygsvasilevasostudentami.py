from bs4 import BeautifulSoup
from ai_assistant_parsers_core.parsers import SimpleSelectDomainBaseParser
from ai_assistant_parsers_core.magic_url import MagicURL
from ai_assistant_parsers_core.parsers.utils.clean_blocks import *
from ai_assistant_parsers_core.parsers.utils.restructure_blocks import *


class DejstviyaProzhivayushchikhPriVozniknoveniiVneshtatnykhSituatsij8VctrechaProrektoraSpbguPoEkspluatatsiiMaterialnoTekhnicheskojBazyGSVasilevaSoStudentamiCampusDomainParser(SimpleSelectDomainBaseParser):
    def __init__(self) -> None:
        super().__init__(
            allowed_domains_paths=["campus.spbu.ru"],
            included_paths=["/dejstviya-prozhivayushchikh-pri-vozniknovenii-vneshtatnykh-situatsij/8-vctrecha-prorektora-spbgu-po-ekspluatatsii-materialno-tekhnicheskoj-bazy-g-s-vasileva-so-studentami/*"],
            select_arguments=[],
        )
