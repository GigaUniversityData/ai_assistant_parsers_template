from os import getenv
import subprocess
import shlex


PROJECT_SLUG = getenv("PROJECT_SLUG", "{{cookiecutter.project_slug}}")

COMMAND = f"mkinit src/{PROJECT_SLUG} --recursive -w --nomods --relative --black"
subprocess.run(shlex.split(COMMAND))
