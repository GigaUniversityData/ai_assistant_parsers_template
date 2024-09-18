import subprocess


subprocess.run(["mkinit", "src/parsers", "--recursive", "-w", "--nomods", "--relative", "--black"])
subprocess.run(["mkinit", "src/refiners", "--recursive", "-w", "--nomods", "--relative", "--black"])
