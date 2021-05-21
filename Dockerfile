FROM python:3.9-slim

WORKDIR /app

COPY . .
RUN pip install -r requirements.txt
RUN pip install .

ENTRYPOINT ["bash", "gunicorn_starter.sh"]
