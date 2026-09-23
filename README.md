# Cybersecurity in the Age of Artificial Intelligence: Complete Academic Research Project

**Title:** Cybersecurity in the Age of Artificial Intelligence: The Rise of AI-Driven Cyber Threats, Defensive Intelligence, and the Changing Global Security Landscape  
**Author:** Multidisciplinary Academic Research Consortium  

---

### Overview

The convergence of artificial intelligence (AI) with global cyberspace has initiated a profound paradigm shift in information security. This repository contains a comprehensive **21-page academic research monograph** evaluating how foundation models, automated reasoning agents, and generative synthetic media transform both offensive exploitation vectors and defensive security capabilities.

The final, print-ready document formatted to IEEE Transactions standard is located in the root as **`research-paper.pdf`**.

### Master Repository Guide

1. **Master Paper PDF:** `research-paper.pdf` (Final 21-page Academic PDF with vector graphics and formulas).
2. **LaTeX Source:** `research-paper/paper/main.tex` (IEEE LaTeX including native `TikZ` architectural diagrams).
3. **Verified Bibliography:** `research-paper/paper/references.bib` (32 focused, high-value academic and empirical entries).
4. **Reference PDFs:** `ref-papers/` (Original downloads of the 10 most critical source papers, e.g., Goodfellow, Szegedy, Carlini).
5. **Modular Paper Sections (Markdown):** `research-paper/paper/sections/` (18 modular markdown sections, for quick reading without PDF compilation).
6. **Primary Sources & Evidentiary Notes:** `research-paper/sources/sources.md` & `research-paper/sources/source_notes.md`.
7. **In-Depth Case Studies:** `research-paper/case-studies/` (4 documented real-world case studies including HK deepfake fraud and API hijacking).
8. **Supplementary Appendices:** `research-paper/appendix/` (Mathematical formulations, MITRE ATLAS matrix, Regulatory comparison).
9. **Research Audit Report:** `research-paper/research-audit.md` (Systematic verification and citation audit).
10. **Peer Review & Revision Report:** `research-paper/peer-review-report.md` (Formal peer-review evaluation).

### Visualizations & Diagnostics

*   **TikZ Architectural Diagrams:** Box and flow diagrams are built directly into the LaTeX document using `TikZ` to guarantee mathematical precision and A4 print clarity.
*   **Charts & Quantitative Assets:** Plot outputs tracking ransomware volume, temporal compression, initial access vectors, and extortion macroeconomics are stored in `research-paper/figures/`.
*   **Reproducible Datasets:** `research-paper/figures/data/` (Original CSVs used for quantitative charting).

### Compilation (Local)
To compile the PDF locally with TeX Live:
```bash
cd research-paper/paper
pdflatex -interaction=nonstopmode main.tex
bibtex main
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```
