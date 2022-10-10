#!/bin/sh
set -- $(echo "$2" | tr ' ' '\n')
HOST="$2" PORT="$3" python writeup/solve.py
