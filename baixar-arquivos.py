# -*- coding: utf-8 -*-
"""
Baixa para dentro da pasta assets/uploads/ todos os PDFs e imagens que ainda
estao hospedados no WordPress (regulacaosmsfloripa.com).

COMO USAR
  1. Rode enquanto o site antigo ainda estiver no ar.
  2. Abra o terminal (Prompt de Comando no Windows) nesta pasta e execute:
         python baixar-arquivos.py
  3. Ao terminar, confira se ficou algum item na lista de falhas.

Requer apenas Python 3 instalado (https://www.python.org/downloads/).
"""
import os
import sys
import time
import urllib.request
import urllib.error

BASE = 'https://regulacaosmsfloripa.com/wp-content/uploads/'
DESTINO = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets', 'uploads')
LISTA = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'arquivos.txt')
CABECALHO = {'User-Agent': 'Mozilla/5.0 (compativel; copia-estatica)'}


def main():
    if not os.path.exists(LISTA):
        print('Nao encontrei arquivos.txt ao lado deste script.')
        sys.exit(1)

    with open(LISTA, encoding='utf-8') as f:
        urls = [l.strip() for l in f if l.strip()]

    total = len(urls)
    baixados = existentes = 0
    falhas = []

    print(f'{total} arquivos na lista. Salvando em {DESTINO}\n')

    for n, url in enumerate(urls, 1):
        if not url.startswith(BASE):
            falhas.append((url, 'fora da pasta uploads'))
            continue
        rel = url[len(BASE):]
        caminho = os.path.join(DESTINO, *rel.split('/'))
        if os.path.exists(caminho) and os.path.getsize(caminho) > 0:
            existentes += 1
            continue
        os.makedirs(os.path.dirname(caminho), exist_ok=True)
        try:
            req = urllib.request.Request(url, headers=CABECALHO)
            with urllib.request.urlopen(req, timeout=60) as r, open(caminho, 'wb') as saida:
                saida.write(r.read())
            baixados += 1
            print(f'[{n}/{total}] ok  {rel}')
        except Exception as e:                      # noqa: BLE001
            falhas.append((url, str(e)))
            print(f'[{n}/{total}] FALHOU  {rel}  ({e})')
            if os.path.exists(caminho) and os.path.getsize(caminho) == 0:
                os.remove(caminho)
        time.sleep(0.15)

    print('\n----------------------------------------')
    print(f'Baixados agora: {baixados}')
    print(f'Ja existiam:    {existentes}')
    print(f'Falhas:         {len(falhas)}')
    if falhas:
        print('\nArquivos que nao vieram:')
        for u, e in falhas:
            print(f'  {u}  ->  {e}')
        print('\nBaixe esses manualmente pelo navegador e salve na pasta '
              'assets/uploads/ mantendo o mesmo caminho (ano/mes/arquivo).')


if __name__ == '__main__':
    main()
