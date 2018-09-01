#!/usr/bin/env bash
while :
do
  read key
  if [ "$key" = "q" ]; then
    echo "breakコマンドを実行します..."
    break
  else
    echo "$keyが入力されました。"
  fi
done
echo "無限ループを抜けました。"

exit 0