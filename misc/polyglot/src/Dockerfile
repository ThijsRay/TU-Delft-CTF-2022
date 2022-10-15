FROM python:3.10-buster
RUN python3 -m pip install capstone keystone-engine unicorn fastapi uvicorn[standard] pydantic

WORKDIR /app
COPY . .
EXPOSE 8000

ENTRYPOINT uvicorn app:app --host 0.0.0.0 --port 8000