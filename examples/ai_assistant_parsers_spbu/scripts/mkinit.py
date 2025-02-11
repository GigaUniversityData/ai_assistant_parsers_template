import shlex
import subprocess


COMMAND = "mkinit src/ai_assistant_parsers_spbu --recursive -w --nomods --relative --black"

subprocess.run(shlex.split(COMMAND))
