import re
import os

with open("research-paper/paper/main.tex", "r", encoding="utf-8") as f:
    text = f.read()

# Create a clean directory for original drafts
os.makedirs("research-paper/paper/original_drafts", exist_ok=True)

# Split by \section{...}
parts = re.split(r'(\section\{.*?\})', text)

# The first part contains everything before the first \section
with open("research-paper/paper/original_drafts/00_preamble.tex", "w", encoding="utf-8") as f:
    f.write(parts[0])

# Parts contain alternating section titles and contents
for i in range(1, len(parts), 2):
    title = parts[i]
    content = parts[i+1]
    
    # clean title name for file
    m = re.search(r'\section\{(.*?)\}', title)
    if m:
        clean_name = m.group(1).replace(" ", "_").replace("/", "_").replace(".", "")
        # keep it alphanumeric
        clean_name = "".join(c for c in clean_name if c.isalnum() or c == '_').lower()
        filename = f"research-paper/paper/original_drafts/{i//2 + 1:02d}_{clean_name}.tex"
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(title + content)

print("Split complete!")
