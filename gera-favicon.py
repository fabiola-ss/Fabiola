"""Gera os ícones do site a partir do símbolo da logo.

O favicon não pode ser a logo inteira: em 16px a palavra "CRIAR ESTÚDIO" vira
uma mancha cinza. Então recorta só a marca — a seta roxa com a ponta verde —
que é o que se reconhece pequeno.
"""
import pathlib
from PIL import Image

ORIGEM = pathlib.Path('logo.png')
CAIXA = (4, 4, 139, 142)      # a marca, sem o texto (medido no alfa da imagem)
MARGEM = 0.07                 # respiro em volta, senão o ícone encosta na borda


def quadrado(lado, fundo=None):
    """A marca centralizada num quadrado, com margem."""
    marca = Image.open(ORIGEM).convert('RGBA').crop(CAIXA)
    util = round(lado * (1 - 2 * MARGEM))
    escala = min(util / marca.width, util / marca.height)
    marca = marca.resize((round(marca.width * escala), round(marca.height * escala)),
                         Image.LANCZOS)
    tela = Image.new('RGBA', (lado, lado), fundo or (0, 0, 0, 0))
    tela.paste(marca, ((lado - marca.width) // 2, (lado - marca.height) // 2), marca)
    return tela


# .ico com três tamanhos dentro: o navegador escolhe o que precisa em cada lugar
# (aba, favoritos, atalho na área de trabalho) sem reamostrar de um só.
quadrado(48).save('favicon.ico', sizes=[(16, 16), (32, 32), (48, 48)])

# PNG grande para Android e para a aba em telas retina
quadrado(192).save('icon-192.png')

# iOS achata transparência em preto, então este vai com fundo branco sólido.
quadrado(180, (255, 255, 255, 255)).save('apple-touch-icon.png')

# Este entra embutido no HTML, como data URI: sem requisição e sobrevive no
# index-unico.html, que precisa continuar sendo um arquivo só.
quadrado(64).save('/tmp/icon-64.png')

for f in ['favicon.ico', 'icon-192.png', 'apple-touch-icon.png']:
    print(f, pathlib.Path(f).stat().st_size, 'bytes')
