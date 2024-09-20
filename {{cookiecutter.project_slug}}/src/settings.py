from pathlib import Path

from ai_assistant_parsers_core.parsers import ABCParser, UniversalParser
from ai_assistant_parsers_core.refiners import (
    ABCParsingRefiner,
    CleanParsingRefiner,
    RestructureParsingRefiner,
)

from src.parsers import *
from src.refiners import *


PARSERS: list[ABCParser] = [
    UniversalParser(),
]
PARSING_REFINERS: list[ABCParsingRefiner] = [
    CleanParsingRefiner(),
    RestructureParsingRefiner(),
]
RESULTS_PATH = Path("output/")
