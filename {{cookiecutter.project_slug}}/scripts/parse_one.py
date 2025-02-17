from os import getenv
import sys
import subprocess
import shlex

from dotenv import load_dotenv


load_dotenv()

PROJECT_SLUG = getenv("PROJECT_SLUG", "{{cookiecutter.project_slug}}")
PYTHON_PATH = sys.executable
URL = sys.argv[1]

COMMAND = f"{PYTHON_PATH} -m ai_assistant_parsers_core.cli parse-one {PROJECT_SLUG} output/parsing {URL}"
subprocess.run(shlex.split(COMMAND))
