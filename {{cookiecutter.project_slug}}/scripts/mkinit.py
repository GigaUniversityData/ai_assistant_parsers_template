import shlex
import subprocess


COMMAND = "mkinit src/{{cookiecutter.project_slug}} --recursive -w --nomods --relative --black"

subprocess.run(shlex.split(COMMAND))
