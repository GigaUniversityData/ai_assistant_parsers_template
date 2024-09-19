from ai_assistant_parsers_core.parsers import SimpleSelectDomainBaseParser


class PayDomainParser(SimpleSelectDomainBaseParser):
    def __init__(self) -> None:
        super().__init__(
            allowed_domains_paths=["pay.spbu.ru"],
            select_arguments=["main"],
        )
