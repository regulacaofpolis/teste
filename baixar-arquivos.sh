#!/bin/sh
# Alternativa ao baixar-arquivos.py, para quem prefere terminal com curl.
# Uso:  sh baixar-arquivos.sh
BASE="https://regulacaosmsfloripa.com/wp-content/uploads/"
while read -r url; do
  [ -z "$url" ] && continue
  rel="${url#$BASE}"
  [ "$rel" = "$url" ] && continue
  mkdir -p "assets/uploads/$(dirname "$rel")"
  if [ -s "assets/uploads/$rel" ]; then continue; fi
  echo "baixando $rel"
  curl -fsSL "$url" -o "assets/uploads/$rel" || echo "FALHOU: $url"
  sleep 0.15
done < arquivos.txt
echo "concluido"
