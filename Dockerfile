FROM python:3.12-slim

WORKDIR /app

ARG APP_VERSION=unknown
ENV APP_VERSION=$APP_VERSION

COPY src/ ./src/

ENTRYPOINT ["python", "-m", "src.api"]
