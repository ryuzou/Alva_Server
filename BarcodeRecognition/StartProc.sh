#!/usr/bin/env bash
while :
do
  read key
  if [ "$key" = "q" ]; then
    break
  else
    python /usr/local/lib/AlvaReadBarcode.py
  fi
done

exit 0