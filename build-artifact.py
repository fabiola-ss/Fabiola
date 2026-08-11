"""Gera a versão para Artifact a partir de index.html (fonte da verdade)."""
import re, pathlib

src = pathlib.Path('/home/user/Fabiola/index.html').read_text(encoding='utf-8')

title = re.search(r'<title>.*?</title>', src, re.S).group(0)
style = re.search(r'<style>.*?</style>', src, re.S).group(0)
body  = re.search(r'<body>(.*?)</body>', src, re.S).group(1)

# O Artifact é uma página única e não serve arquivos irmãos, então o vídeo
# do hero entra embutido como data URI só na versão de preview. O index.html
# do repositório continua apontando para os arquivos .webm/.mp4, que é o que
# rende no Netlify (streaming, cache e HTML leve).
import base64
video = pathlib.Path(__file__).with_name('hero-bg.webm')
if video.exists():
    b64 = base64.b64encode(video.read_bytes()).decode()
    body = re.sub(r'\s*<source src="hero-bg\.mp4"[^>]*>', '', body)
    body = body.replace('src="hero-bg.webm"', 'src="data:video/webm;base64,' + b64 + '"')
    print(f'video embutido no preview: {len(b64)/1024:.0f} KB em base64')

out = ('<meta name="viewport" content="width=device-width, initial-scale=1">\n'
       + title + '\n\n' + style + '\n' + body.strip() + '\n')

dst = pathlib.Path('/tmp/claude-0/-home-user-Fabiola/e908ad52-172a-5b9b-bd5e-d9e959d86c52/scratchpad/criar-estudio-lp.html')
dst.write_text(out, encoding='utf-8')

import re as _re
forbidden = _re.compile(r'<!doctype|</?(html|head|body)(\s|>)', _re.I)
hit = forbidden.search(out)
assert hit is None, 'tag de wrapper encontrada: ' + hit.group(0)
print('bytes:', len(out), '| wrapper removido: ok | title/style/conteudo:',
      '<title>' in out, '<style>' in out, 'site-header' in out)
