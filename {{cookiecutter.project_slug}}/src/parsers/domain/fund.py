from ai_assistant_parsers_core.parsers import SimpleSelectDomainBaseParser


# TODO: Перенести парсинг главной страница в отдельный парсер
class FundDomainParser(SimpleSelectDomainBaseParser):
    def __init__(self) -> None:
        super().__init__(
            allowed_domains_paths=["fund.spbu.ru"],
            select_arguments=[
                ".content__main",  # Только все страницы, кроме главной
                ".homepage",  # Только главная страница
            ]
        )
