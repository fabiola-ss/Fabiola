"""Gera index-unico.html: o index.html com o vídeo do hero embutido, para
publicar arrastando UM arquivo só.

Embute os dois codecs — WebM/VP9 primeiro (menor) e MP4/H.264 como reserva,
que é o que garante aparelhos antigos. Rode de novo sempre que editar o
index.html."""
import re, base64, pathlib

raiz  = pathlib.Path(__file__).parent
fonte = raiz / 'index.html'
saida = raiz / 'index-unico.html'

s = fonte.read_text(encoding='utf-8')

bloco = re.search(r'\s*<source src="hero-bg\.webm".*?<source src="hero-bg\.mp4"[^>]*>', s, re.S)
assert bloco, 'não encontrei os <source> do vídeo no index.html'

fontes = []
for nome, mime in (('hero-bg-inline.webm', 'video/webm'), ('hero-bg-inline.mp4', 'video/mp4')):
    dados = (raiz / nome).read_bytes()
    b64 = base64.b64encode(dados).decode()
    fontes.append(f'\n        <source src="data:{mime};base64,{b64}" type="{mime}">')
    print(f'  {nome}: {len(dados)/1024:.0f} KB -> {len(b64)/1024:.0f} KB em base64')

s = s.replace(bloco.group(0), ''.join(fontes))
saida.write_text(s, encoding='utf-8')
print(f'{saida.name}: {len(s)/1024:.0f} KB')
