from pathlib import Path

from src.parsers import *
from src.parsing_refiners import *

from ai_assistant_parsers_core.refiners import (
    ABCParsingRefiner,
    CleanPostParsingRefiner,
    RestructurePostParsingRefiner,
)


PARSERS: list[ABCParser] = [
    UniversalParser(),
]
PRE_PARSING_REFINERS: list[ABCParsingRefiner]  = []
POST_PARSING_REFINERS: list[ABCParsingRefiner] = [CleanPostParsingRefiner(), RestructurePostParsingRefiner()]
RESULTS_PATH = Path("results/")
