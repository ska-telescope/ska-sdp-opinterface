FROM python:3.10-slim as build

COPY . ./
RUN pip install poetry && \
    poetry export --without-hashes -o requirements.txt && \
    poetry build

FROM python:3.10-slim

WORKDIR /install

COPY --from=build requirements.txt dist/*.whl ./
RUN pip install --no-cache-dir --no-compile -r requirements.txt *.whl

WORKDIR /app

ENTRYPOINT ["gunicorn", "-w", "2", "--threads", "3", "-b", "0.0.0.0:8000", "ska_sdp_opinterface.sdp:app"]
