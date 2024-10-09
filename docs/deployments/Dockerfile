FROM python:3.12

WORKDIR /app

COPY poetry.lock pyproject.toml Makefile /app/

RUN pip install poetry
RUN poetry install --no-root

COPY source /app/source

CMD ["poetry", "run", "sphinx-autobuild", "source", "build/html", "--host", "0.0.0.0"]
