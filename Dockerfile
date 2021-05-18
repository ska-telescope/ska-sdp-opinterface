FROM python:3.9-slim
COPY requirements.txt /
RUN pip3 install -r /requirements.txt
COPY src/ska_sdp_opinterface /app
COPY gunicorn_starter.sh /app
WORKDIR /app
ENTRYPOINT ["./gunicorn_starter.sh"]
