import subprocess


subprocess.run(["mkinit", "src/{{cookiecutter.project_slug}}", "--recursive", "-w", "--nomods", "--relative", "--black"])
