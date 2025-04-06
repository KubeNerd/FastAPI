FROM python:3.12-slim-bookworm

ENV PYTHONUNBUFFERED=1 \
    PATH="/root/.local/bin:$PATH" \
    PYTHONPATH="/application"

WORKDIR /application

RUN apt-get update && apt-get install -y curl build-essential \
  && curl -sSL https://install.python-poetry.org | python3 - \
  && apt-get remove --purge -y curl \
  && apt-get autoremove -y \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

COPY ./pyproject.toml ./poetry.lock ./

RUN poetry config virtualenvs.create false \
  && poetry install --no-root --no-interaction --no-ansi

COPY ./application .


EXPOSE 8080


CMD ["python", "main.py"]
