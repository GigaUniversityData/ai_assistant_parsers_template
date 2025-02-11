import sys
import subprocess
import shlex


URL = sys.argv[1]
PYTHON_PATH = sys.executable
COMMAND = f"{PYTHON_PATH} -m ai_assistant_parsers_core.cli parse-one ai_assistant_parsers_spbu output/parse_one {URL}"

subprocess.run(shlex.split(COMMAND))
