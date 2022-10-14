FROM python:slim

RUN apt update && apt install ncat -y

COPY src/shell.py /srv/app/main.py
COPY src/flag.txt /srv/app/flag.txt
