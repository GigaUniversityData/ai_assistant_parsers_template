from os import getenv
import subprocess
import shlex


MODULE_NAME = getenv("AAPC_MODULE_NAME", "{{cookiecutter.project_slug}}")

COMMAND = f"mkinit src/{MODULE_NAME} --recursive -w --nomods --relative --black"
subprocess.run(shlex.split(COMMAND))
