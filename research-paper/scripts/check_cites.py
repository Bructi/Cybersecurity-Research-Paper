import re

with open("D:/Full Stack Codes/Work/Demo Research Paper/research-paper/paper/main.tex", "r", encoding="utf-8") as f:
    tex = f.read()

with open("D:/Full Stack Codes/Work/Demo Research Paper/research-paper/paper/references.bib", "r", encoding="utf-8") as f:
    bib = f.read()

tex_cites = re.findall(r"\\cite\{([^}]+)\}", tex)
all_cites = set()
for c in tex_cites:
    for item in c.split(","):
        all_cites.add(item.strip())

bib_keys = set(re.findall(r"@\w+\{([^,]+),", bib))

missing = all_cites - bib_keys
print("Total cites in main.tex:", len(all_cites))
print("Total keys in references.bib:", len(bib_keys))
print("Missing keys in bib:", sorted(list(missing)))
print("\nBib keys containing partial matches:")
for m in sorted(list(missing)):
    matches = [k for k in bib_keys if m[:5] in k or k[:5] in m]
    print(f"  Missing: {m} -> Suggestions in bib: {matches}")
