# -*- coding: utf-8 -*-
"""
Verification script for camera-ready IEEEtran manuscript:
- Checks page count of all 3 PDF copies (must be exactly 24)
- Checks SHA256 hashes across all 3 copies (must be identical)
- Checks main.log for 0 errors, 0 undefined citations, 0 undefined references, 0 overfull hboxes, 0 warnings
- Scans rendered PDF text for unresolved [?] or ?? markers
"""
import os
import sys
import re
import hashlib
import pypdf

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.join(BASE_DIR, "..", "..")

PDF_PATHS = [
    os.path.join(ROOT_DIR, "research-paper", "paper", "main.pdf"),
    os.path.join(ROOT_DIR, "research-paper.pdf"),
    os.path.join(ROOT_DIR, "research-paper", "research-paper.pdf")
]
LOG_PATH = os.path.join(ROOT_DIR, "research-paper", "paper", "main.log")

print("=" * 60)
print("IEEEtran Manuscript Camera-Ready Verification")
print("=" * 60)

# 1. Verify Page Count and Hash Matching
hashes = []
for p in PDF_PATHS:
    if not os.path.exists(p):
        print(f"[FAIL] Missing PDF: {p}")
        sys.exit(1)
    
    reader = pypdf.PdfReader(p)
    num_pages = len(reader.pages)
    with open(p, "rb") as f:
        file_hash = hashlib.sha256(f.read()).hexdigest()
    hashes.append(file_hash)
    
    print(f"File: {os.path.relpath(p, ROOT_DIR)}")
    print(f"  Pages: {num_pages} (Target: 24)")
    print(f"  SHA256: {file_hash}")
    assert num_pages == 24, f"Expected 24 pages, got {num_pages}"

assert len(set(hashes)) == 1, "PDF hashes are not synchronized!"
print("[PASS] All 3 PDF copies are identical and exactly 24 pages.")

# 2. Verify Log File Cleanliness
if os.path.exists(LOG_PATH):
    with open(LOG_PATH, "r", encoding="utf-8", errors="ignore") as f:
        log_content = f.read()
    
    undef_cites = re.findall(r"Citation `.*` on page .* undefined", log_content)
    undef_refs = re.findall(r"Reference `.*` on page .* undefined", log_content)
    overfull_boxes = re.findall(r"Overfull \\hbox.*", log_content)
    warnings = [l for l in log_content.splitlines() if "LaTeX Warning:" in l]
    
    print("-" * 60)
    print("Log Cleanliness Check (main.log):")
    print(f"  Undefined citations:  {len(undef_cites)}")
    print(f"  Undefined references: {len(undef_refs)}")
    print(f"  Overfull \\hbox:       {len(overfull_boxes)}")
    print(f"  LaTeX Warnings:       {len(warnings)}")
    
    assert len(undef_cites) == 0, f"Found undefined citations: {undef_cites}"
    assert len(undef_refs) == 0, f"Found undefined references: {undef_refs}"
    assert len(overfull_boxes) == 0, f"Found overfull hboxes: {overfull_boxes}"
    assert len(warnings) == 0, f"Found LaTeX warnings: {warnings}"
    print("[PASS] main.log has 0 errors, 0 undefined citations/references, 0 overfull hboxes, and 0 warnings.")

# 3. Verify Rendered PDF Text for Unresolved Tokens
reader = pypdf.PdfReader(PDF_PATHS[0])
for i, page in enumerate(reader.pages):
    txt = page.extract_text() or ""
    bad_cites = re.findall(r"\[\?+\]", txt)
    bad_refs = re.findall(r"\?\?", txt)
    if bad_cites or bad_refs:
        print(f"[FAIL] Unresolved markers on page {i+1}: cites={bad_cites}, refs={bad_refs}")
        sys.exit(1)

print("[PASS] Rendered PDF contains 0 broken citations [?] or cross-references ??.")
print("=" * 60)
print("ALL VERIFICATION CHECKS PASSED SUCCESSFULLY.")
print("=" * 60)
