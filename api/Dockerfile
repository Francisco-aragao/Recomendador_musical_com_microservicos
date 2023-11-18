FROM python:3.9-slim-bullseye

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

ENTRYPOINT ["uvicorn","main:app","--reload","--port=32183","--host=0.0.0.0"]