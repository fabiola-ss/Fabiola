"""Subseta uma fonte para os caracteres realmente usados nos destaques e
embute como @font-face base64 no index.html. Uso: python3 embed-font.py "<Família>" [--dry]"""
import re, sys, base64, pathlib, subprocess, tempfile, json

FAM = sys.argv[1]
DRY = '--dry' in sys.argv
IDX = pathlib.Path('/home/user/Fabiola/index.html')
src = IDX.read_text(encoding='utf-8')

# caracteres que aparecem dentro dos trechos com ênfase
chars = set()
for m in re.finditer(r'<span class="em-brand"[^>]*>(.*?)</span>', src, re.S):
    chars |= set(re.sub(r'<[^>]+>', '', m.group(1)))
chars |= set(' .,0123456789')          # margem de segurança para edições de texto
text = ''.join(sorted(chars))

font = json.load(open('fonts.json'))[FAM]['file']
orig = pathlib.Path(font).stat().st_size
out = pathlib.Path(tempfile.mkdtemp())/'sub.woff2'
subprocess.run(['pyftsubset', font, f'--text={text}', '--flavor=woff2',
                '--layout-features=kern,liga', f'--output-file={out}'], check=True)
b64 = base64.b64encode(out.read_bytes()).decode()

print(f'{FAM}: original {orig/1024:.1f} KB -> subset {out.stat().st_size/1024:.1f} KB '
      f'-> base64 {len(b64)/1024:.1f} KB | {len(chars)} caracteres')
if DRY:
    sys.exit()

face = (f"/* {FAM} Italic — Copyright 2012 The Libre Baskerville Project Authors\n"
        f"   (https://github.com/impallari/Libre-Baskerville), SIL Open Font License 1.1\n"
        f"   (https://openfontlicense.org). Subsetada aos caracteres usados nos destaques\n"
        f"   e embutida no arquivo: renderiza igual em qualquer aparelho, sem rede. */\n"
        f"@font-face{{\n  font-family:'LPEmphasis';\n  font-style:italic;\n"
        f"  font-weight:400;\n  font-display:swap;\n"
        f"  src:url(data:font/woff2;base64,{b64}) format('woff2');\n}}\n")

src = re.sub(r'(?s)/\* @font-face embutida.*?/\* fim @font-face \*/\n', '', src)
src = src.replace('<style>\n', '<style>\n/* @font-face embutida */\n' + face + '/* fim @font-face */\n', 1)
src = re.sub(r'  --font-emphasis:[^;]+;', "  --font-emphasis:'LPEmphasis',Georgia,'Times New Roman',serif;", src, flags=re.S)
IDX.write_text(src, encoding='utf-8')
print('embutida em index.html')
