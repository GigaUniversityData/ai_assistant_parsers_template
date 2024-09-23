from pathlib import Path

from ai_assistant_parsers_core.parsers import ABCParser, UniversalParser
from ai_assistant_parsers_core.refiners import (
    ABCParsingRefiner,
    CleanParsingRefiner,
    RestructureParsingRefiner,
)

from {{cookiecutter.project_slug}}.parsers import *
from {{cookiecutter.project_slug}}.refiners import *


__all__ = ["PARSERS", "PARSING_REFINERS", "RESULTS_PATH"]


PARSERS: list[ABCParser] = [
    UniversalParser(),
]
PARSING_REFINERS: list[ABCParsingRefiner] = [
    CleanParsingRefiner(),
    RestructureParsingRefiner(),
]
RESULTS_PATH = Path("output/")
