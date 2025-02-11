from .domain import (
    AbiturientDomainParser,
    CampusDomainParser,
    FundDomainParser,
    StudsovetDomainParser,
    WWWDomainParser,
)
from .multiple_domains import (
    TMContentMultipleDomainsParser,
)
from .page import (
    MainAbiturientPageParser,
)

__all__ = [
    "AbiturientDomainParser",
    "CampusDomainParser",
    "FundDomainParser",
    "MainAbiturientPageParser",
    "StudsovetDomainParser",
    "TMContentMultipleDomainsParser",
    "WWWDomainParser",
]
