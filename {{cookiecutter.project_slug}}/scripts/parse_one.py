from os import getenv
import sys
import subprocess
import shlex

from dotenv import load_dotenv


load_dotenv()

MODULE_NAME = getenv("MODULE_NAME", "{{cookiecutter.project_slug}}")
PYTHON_PATH = sys.executable
URL = sys.argv[1]

COMMAND = f"{PYTHON_PATH} -m ai_assistant_parsers_core.cli parse-one {MODULE_NAME} output/parsing {URL}"
subprocess.run(shlex.split(COMMAND))
