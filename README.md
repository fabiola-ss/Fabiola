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

- Os links de WhatsApp usam o número provisório `5500000000000`. Procure por
  `wa.me/5500000000000` no `index.html` e troque pelo número real.
- O portfólio mostra 6 projetos, com a captura real da home de cada um. Faltam
  as capturas de **Total Skin**, **BCorporate** e **Grupo VT Rads** — os cards
  agora são só imagem, então esses três saíram da esteira até as capturas
  chegarem. Mande os prints e eles voltam.
- O antes/depois embute os dois sites do Airton ao vivo (`airtonrafael.com` e
  `airtonrafael.com.br`). Daqui não consigo abrir nenhum dos dois para testar,
  então confira no site publicado se os dois aparecem — se algum vier em
  branco, é o servidor dele recusando ser embutido (`X-Frame-Options`), e aí a
  saída é trocar por uma captura de tela.
