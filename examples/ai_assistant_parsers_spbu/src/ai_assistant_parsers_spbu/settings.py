from ai_assistant_parsers_core.parsers import ABCParser, UniversalParser
from ai_assistant_parsers_core.refiners import (
    ABCParsingRefiner,
    DefaultRefiner,
)

from ai_assistant_parsers_spbu.parsers import *
from ai_assistant_parsers_spbu.refiners import *


__all__ = ["PARSERS", "PARSING_REFINERS"]


PARSERS: list[ABCParser] = [
    AbiturientDomainParser(),
    CampusDomainParser(),
    FundDomainParser(),
    PayDomainParser(),
    StudsovetDomainParser(),
    WWWDomainParser(),
    TMContentParser(),
    AbiturientMainPageParser(),

    UniversalParser(),
]
PARSING_REFINERS: list[ABCParsingRefiner] = [
    CleanASideParsingRefiner(),
    CleanEmptyTagsParsingRefiner(),
    HideProtectedMailsParsingRefiner(),

    DefaultRefiner(),
]
