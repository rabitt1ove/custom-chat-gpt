FROM python:3.11-slim-bullseye

RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./app /app

EXPOSE 8501

HEALTHCHECK CMD curl —-fail http://localhost:8501/healthz || exit 1

CMD ["streamlit", "run", "/app/main.py"]
