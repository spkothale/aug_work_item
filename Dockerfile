FROM python:3.12-slim

WORKDIR /app

COPY src/ ./src/

EXPOSE 8080

CMD ["python", "-m", "src/api.py"]
