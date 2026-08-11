"""Gera a versão para Artifact a partir de index.html (fonte da verdade)."""
import re, pathlib

src = pathlib.Path('/home/user/Fabiola/index.html').read_text(encoding='utf-8')

title = re.search(r'<title>.*?</title>', src, re.S).group(0)
style = re.search(r'<style>.*?</style>', src, re.S).group(0)
body  = re.search(r'<body>(.*?)</body>', src, re.S).group(1)

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
