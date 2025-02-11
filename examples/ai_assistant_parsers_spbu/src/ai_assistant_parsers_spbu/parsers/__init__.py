from .domain import (
    AbiturientDomainParser,
    CampusDomainParser,
    FundDomainParser,
    PayDomainParser,
    StudsovetDomainParser,
    WWWDomainParser,
)
from .multiple_domains import (
    TMContentParser,
)
from .page import (
    AbiturientMainPageParser,
)

__all__ = [
    "AbiturientDomainParser",
    "AbiturientMainPageParser",
    "CampusDomainParser",
    "FundDomainParser",
    "PayDomainParser",
    "StudsovetDomainParser",
    "TMContentParser",
    "WWWDomainParser",
]
