from os import getenv
import sys
import subprocess
import shlex

from dotenv import load_dotenv


load_dotenv()

MODULE_NAME = getenv("AAPC_MODULE_NAME", "{{cookiecutter.project_slug}}")
PYTHON_PATH = sys.executable

COMMAND = f"{PYTHON_PATH} -m ai_assistant_parsers_core.cli parse-many {MODULE_NAME} output/parsing"
subprocess.run(shlex.split(COMMAND))
