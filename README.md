# Criar Estúdio — Landing Page

Site estático, sem framework e sem dependências externas. Não há etapa de
build: o que está na raiz deste repositório é o que vai ao ar.

## Onde o site mora

GitHub Pages, servindo a raiz da branch **`main`**, no domínio
**estudiocriar.online**.

É a `main` que vai ao ar — o que estiver em qualquer outra branch não aparece
no site até ser levado para lá.

Conferir isso: **Settings → Pages**, no repositório. Precisa estar em
*Deploy from a branch*, com `main` e a pasta `/ (root)`.

Dois arquivos existem só por causa disso e não devem ser apagados:

- `CNAME` — é ele que prende o domínio ao site. Sem ele o endereço volta a ser
  `fabiola-ss.github.io/Fabiola`.
- `.nojekyll` — desliga o Jekyll, que o GitHub Pages roda por padrão. Ele está
  vazio de propósito: o que importa é existir.

## Atualizar o site

Editar o arquivo no GitHub e salvar (*Commit changes*) já publica. Leva de 1 a
2 minutos. O andamento aparece na aba **Actions** do repositório — quando o
check verde aparecer no commit, está no ar.

Se a mudança não aparecer no navegador, é cache: recarregue com Ctrl+Shift+R
(ou Cmd+Shift+R no Mac).

## Arquivos

| Arquivo | Para que serve |
|---|---|
| `index.html` | A página. Todo o CSS, o JS e a fonte estão dentro dele. |
| `hero-bg.webm` / `hero-bg.mp4` | Vídeo de fundo do hero. O HTML aponta para estes nomes — se renomear um, o vídeo some. |
| `index-unico.html` | Cópia com o vídeo embutido num arquivo só. Não participa do site publicado — serve para mandar a página por e-mail, abrir sem internet ou hospedar em outro lugar. |
| `hero-bg-inline.*` | Vídeos reduzidos que alimentam o `index-unico.html`. |
| `build-single.py` | Regera o `index-unico.html`. Rode depois de editar o `index.html`. |
| `build-artifact.py` | Gera a versão de pré-visualização. |
| `embed-font.py` | Refaz a fonte embutida se os textos em destaque mudarem. |
| `favicon.ico`, `icon-192.png`, `apple-touch-icon.png` | Ícones do site. O da aba também vai embutido no HTML; estes cobrem o que o navegador busca sozinho e a tela de início do celular. |
| `gera-favicon.py` | Refaz os ícones a partir da `logo.png`. Rode se a logo mudar. |
| `CNAME`, `.nojekyll` | Configuração do GitHub Pages (ver acima). |

## Pendências

- Os 9 links de WhatsApp apontam para `5521996891354`, com a mensagem já
  escrita. Para trocar número ou mensagem, procure por `wa.me/` no
  `index.html` — todos usam exatamente a mesma URL.
- O portfólio mostra 6 projetos, com a captura real da home de cada um. Faltam
  as capturas de **Total Skin**, **BCorporate** e **Grupo VT Rads** — os cards
  agora são só imagem, então esses três saíram da esteira até as capturas
  chegarem. Mande os prints e eles voltam.
- A seção "antes e depois" do Airton foi removida. Se um dia voltar, ela está
  inteira no histórico: `git show 41645b1 -- index.html`.
