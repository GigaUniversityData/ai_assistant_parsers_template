FROM python:3.12

WORKDIR /app

COPY ./poetry.lock /app/
COPY ./docs/Makefile /app/
COPY ./pyproject.toml /app/

RUN pip install poetry
RUN poetry install --no-root

COPY ./docs/source /app/source

CMD ["poetry", "run", "sphinx-autobuild", "source", "build/html", "--host", "0.0.0.0"]
