import sys
import subprocess
import shlex


URL = sys.argv[1]
PYTHON_PATH = sys.executable
COMMAND = f"{PYTHON_PATH} -m ai_assistant_parsers_core {{cookiecutter.project_slug}} output/parse_one {URL}"

subprocess.run(shlex.split(COMMAND))
