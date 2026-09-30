# Regulação Floripa — versão estática (HTML puro)

Cópia do site `regulacaosmsfloripa.com` convertida em HTML, CSS e imagens, sem
WordPress, sem banco de dados e sem plugins. Pode ser hospedada de graça no
GitHub Pages (ou em Netlify, Cloudflare Pages, etc.).

## O que tem aqui

```
index.html                   Home
faq/, especialidades/, ...   uma pasta por página, cada uma com index.html
arquivos.txt                 lista dos PDFs e imagens do site antigo
baixar-arquivos.py           script que baixa esses arquivos para o seu computador
404.html                     página de endereço não encontrado
.nojekyll                    evita que o GitHub Pages processe as pastas
```

Cada página é um arquivo único: o CSS está embutido dentro do próprio HTML, então
não existe pasta `assets` e nenhuma página depende de outra para aparecer certo.
A contrapartida é que uma mudança de cor ou espaçamento precisa ser repetida no
bloco `<style>` de cada arquivo.

As páginas geradas são: home, notícias, ofertas de serviços e protocolos de
acesso (com especialidades, exames, odontologia e protocolos SES), alto
custo/TFD (com APAC, AIH, TFD e saúde auditiva), portarias e normativas, FAQ,
contato e as duas páginas de protocolos de ressonância e tomografia.

## Sobre os PDFs e as imagens

Todos os links de arquivo continuam apontando para o WordPress, no formato
`https://regulacaosmsfloripa.com/wp-content/uploads/ano/mes/arquivo.pdf`. Ou
seja: enquanto o site antigo estiver no ar, tudo abre normalmente, e a troca
para o Google Drive pode ser feita depois, arquivo por arquivo.

Para tirar cópia de tudo antes de encerrar a hospedagem, rode:

```
python baixar-arquivos.py
```

O script lê `arquivos.txt` (192 arquivos: 95 PDFs de protocolos e o restante em
imagens) e salva tudo em `assets/uploads/` no seu computador, organizado por
ano e mês. De lá você sobe para o Drive.

Quando for trocar os links, o endereço do Drive que funciona dentro de uma
página é `https://lh3.googleusercontent.com/d/ID_DO_ARQUIVO` para imagens, com o
arquivo compartilhado como "qualquer pessoa com o link". Vale testar com um PDF
e uma imagem antes de migrar os 192.

## Passo 2 — publicar no GitHub Pages

1. Crie uma conta em github.com (ou use a da Secretaria) e clique em
   **New repository**. Nome sugerido: `regulacao-floripa`. Deixe **Public**.
2. Na página do repositório vazio, clique em **uploading an existing file** e
   arraste **o conteúdo desta pasta** (não a pasta em si — o `index.html` tem
   que ficar na raiz do repositório). Confirme com **Commit changes**.
3. Vá em **Settings → Pages**. Em *Source*, escolha **Deploy from a branch**;
   em *Branch*, escolha `main` e a pasta `/ (root)`. Salve.
4. Em um ou dois minutos o site fica no ar em
   `https://SEU-USUARIO.github.io/regulacao-floripa/`.

## Passo 3 (opcional) — manter o domínio próprio

Se quiser continuar usando `regulacaosmsfloripa.com`:

1. Em **Settings → Pages → Custom domain**, escreva o domínio e salve. Isso cria
   um arquivo `CNAME` no repositório.
2. No painel onde o domínio está registrado, aponte os registros DNS para o
   GitHub Pages (registros A para `185.199.108.153`, `185.199.109.153`,
   `185.199.110.153` e `185.199.111.153`, ou um CNAME para
   `SEU-USUARIO.github.io`).
3. Marque **Enforce HTTPS** depois que o certificado for emitido.

Só cancele a hospedagem do WordPress **depois** de mudar os links dos arquivos,
porque hoje eles ainda dependem do endereço antigo.

## Como alterar o conteúdo daqui para frente

Não há mais painel de administração: cada página é um arquivo `index.html` que
pode ser editado direto pelo GitHub (botão do lápis) ou em qualquer editor de
texto. Alguns casos comuns:

- **Novo protocolo em uma lista** — copie um bloco `<li><a class="pdf" ...>` da
  página e troque o endereço e o nome.
- **Novo PDF** — suba o arquivo para onde ele vai ficar hospedado e use esse
  endereço completo no link.
- **Nova notícia** — copie um bloco `<a href="..."><figure>...</figure></a>`
  dentro de `<div class="galeria">` na página de notícias.
- **Cores, fontes e espaçamentos** — estão no bloco `<style>` no topo de cada
  arquivo; a mudança precisa ser repetida em todas as páginas.
- **Menu** — aparece repetido no `<header>` de cada página; ao mudar um item,
  mude em todas.

## Diferenças em relação ao site do WordPress

- A busca do topo foi removida (dependia do WordPress).
- O botão flutuante do Elementor não foi reproduzido.
- A página **Contato** estava vazia no arquivo exportado; ela foi montada com os
  contatos que aparecem nas demais páginas e precisa da sua conferência. Ela não
  estava no menu original, então ficou com um link no rodapé.
- O e-mail da Gerência no rodapé é `regulacao@floripa.sc.gov.br`. Os e-mails de
  setores que aparecem no meio do texto (saúde auditiva, TFD, ASSHUE) foram
  mantidos como estavam.
- As listas de protocolos, que eram uma sequência de títulos, viraram listas de
  links em cartões, com uma etiqueta indicando se o arquivo é PDF ou imagem.
- O restante dos textos, links, perguntas frequentes e imagens está igual ao
  original.
