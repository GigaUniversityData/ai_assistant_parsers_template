from ...simple_find_domain_base import SimpleFindDomainBaseParser


class NAMEDomainParser(SimpleFindDomainBaseParser):
    def __init__(self) -> None:
        super().__init__(
            supported_subdomains=["DOMAIN"],
            find_arguments=[
                #{"class_": "breadcrumbs"},
                {"class_": "page-main-content"},
            ]
        )
