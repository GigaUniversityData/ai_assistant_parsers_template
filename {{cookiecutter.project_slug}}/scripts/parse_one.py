import asyncio
import sys
from pathlib import Path

from ai_assistant_parsers_core.cli import parse_one


RESULTS_PATH = Path("output/parse_one")


async def main() -> None:
    url = sys.argv[1]
    await parse_one.callback("{{cookiecutter.project_slug}}", RESULTS_PATH, url)


if __name__ == "__main__":
    asyncio.run(main())
