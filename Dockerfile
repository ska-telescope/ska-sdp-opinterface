FROM python:3.9-slim

WORKDIR /app

RUN pip3 install poetry
RUN poetry config virtualenvs.create false \
     && poetry install --no-dev

COPY . .

ENTRYPOINT ["bash", "gunicorn_starter.sh"]
