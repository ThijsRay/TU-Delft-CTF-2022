#!/bin/bash
docker build --tag pyjail:latest .
docker run -d --rm -p 58931:58931 pyjail:latest /bin/bash -c 'while true; do /usr/bin/ncat -klv -m 50 -w 10 -C -e "/usr/local/bin/python /srv/app/main.py" 0.0.0.0 58931; done'
