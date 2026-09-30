import urllib.request
import urllib.parse
import os

with open('main.tex', 'r', encoding='utf-8') as f:
    tex = f.read()

url = "https://latexonline.cc/compile?text=" + urllib.parse.quote(tex)
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as response, open('main.pdf', 'wb') as out_file:
        out_file.write(response.read())
    print("PDF compiled successfully via latexonline.cc")
except Exception as e:
    print("Error compiling via API:", e)
