from ai_assistant_parsers_core.parsers import ABCParser, UniversalParser
from ai_assistant_parsers_core.refiners import (
    ABCParsingRefiner,
    DefaultRefiner,
)

from {{cookiecutter.project_slug}}.parsers import *
from {{cookiecutter.project_slug}}.refiners import *


__all__ = ["PARSERS", "PARSING_REFINERS"]


PARSERS: list[ABCParser] = [
    UniversalParser(),
]
PARSING_REFINERS: list[ABCParsingRefiner] = [
    DefaultRefiner(),
]
