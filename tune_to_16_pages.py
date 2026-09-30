with open("research-paper/paper/main.tex", "r", encoding="utf-8") as f:
    text = f.read()

# Add standard space compression commands in preamble for academic formatting
preamble_addition = r"""
\setlength{\textfloatsep}{8pt plus 1.0pt minus 1.5pt}
\setlength{\floatsep}{8pt plus 1.0pt minus 1.5pt}
\setlength{\intextsep}{8pt plus 1.0pt minus 1.5pt}
\setlength{\dbltextfloatsep}{9pt plus 1.0pt minus 1.5pt}
\setlength{\dblfloatsep}{9pt plus 1.0pt minus 1.5pt}
"""

if r"\begin{document}" in text and r"\setlength{\textfloatsep}" not in text:
    text = text.replace(r"\begin{document}", preamble_addition + "\n" + r"\begin{document}")

# Set subfigures and standalone figures width cleanly
text = text.replace("width=0.88\columnwidth", "width=0.78\columnwidth")
text = text.replace("width=0.85\columnwidth", "width=0.78\columnwidth")
text = text.replace("width=0.82\columnwidth", "width=0.78\columnwidth")

with open("research-paper/paper/main.tex", "w", encoding="utf-8") as f:
    f.write(text)

print("Tuning applied.")
