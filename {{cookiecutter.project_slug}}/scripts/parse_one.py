import sys
from pathlib import Path
import subprocess


RESULTS_PATH = Path("output/parse_one")
URL = sys.argv[1]


subprocess.run(["python", "-m", "ai_assistant_parsers_core.cli", "{{cookiecutter.project_slug}}", RESULTS_PATH, URL])
