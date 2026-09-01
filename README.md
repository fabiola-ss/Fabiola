# Criar Estúdio — Landing Page

Site estático, sem framework e sem dependências externas. Não há etapa de
build: o que está na raiz deste repositório é o que vai ao ar.

## Publicar no Netlify (uma vez só)

1. No Netlify: **Add new site → Import an existing project → GitHub**.
2. Autorize e escolha o repositório **fabiola-ss/Fabiola**.
3. Confira os campos:
   - **Branch to deploy:** `claude/landing-page-single-file-f64suf`
     (é a branch padrão do repositório)
   - **Build command:** deixe **vazio**
   - **Publish directory:** `.` (um ponto)

   O `netlify.toml` já define isso; os campos devem vir preenchidos sozinhos.
4. **Deploy site**.

Feito isso, todo push para essa branch republica o site automaticamente.
Não é preciso arrastar arquivo nem mover nada de pasta.

## Atualizar o site depois

Editar o arquivo no GitHub e salvar (*Commit changes*) já dispara o deploy.
Leva de 30 segundos a 1 minuto. O andamento aparece na aba **Deploys** do
Netlify.

## Arquivos

| Arquivo | Para que serve |
|---|---|
| `index.html` | A página. Todo o CSS, o JS e a fonte estão dentro dele. |
| `hero-bg.webm` / `hero-bg.mp4` | Vídeo de fundo do hero. O HTML aponta para estes nomes — se renomear um, o vídeo some. |
| `index-unico.html` | Cópia com o vídeo embutido, para publicar arrastando um arquivo só. Não é usada no deploy pelo GitHub. |
| `hero-bg-inline.*` | Vídeos reduzidos que alimentam o `index-unico.html`. |
| `build-single.py` | Regera o `index-unico.html`. Rode depois de editar o `index.html`. |
| `build-artifact.py` | Gera a versão de pré-visualização. |
| `embed-font.py` | Refaz a fonte embutida se os textos em destaque mudarem. |

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
