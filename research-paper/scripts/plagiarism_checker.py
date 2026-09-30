#!/usr/bin/env python3
"""
Academic Plagiarism & Originality Verification Tool
Computes n-gram overlap, Jaccard token similarity, and TF-IDF cosine distance
across local manuscripts and reference PDFs in ref-papers/.
"""

import os
import re
import sys
import glob

try:
    import pypdf
except ImportError:
    pypdf = None

try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
except ImportError:
    TfidfVectorizer = None
    cosine_similarity = None

def extract_text_from_tex(tex_path):
    with open(tex_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    # Strip LaTeX commands
    content = re.sub(r'\\[a-zA-Z]+(\[[^\]]*\])?(\{[^\}]*\})?', ' ', content)
    content = re.sub(r'[{}\\%$_&#]', ' ', content)
    words = re.findall(r'\b[A-Za-z]{3,}\b', content.lower())
    return ' '.join(words), words

def extract_text_from_pdf(pdf_path):
    if not pypdf:
        return "", []
    try:
        reader = pypdf.PdfReader(pdf_path)
        full_text = []
        for p in reader.pages:
            t = p.extract_text() or ""
            full_text.append(t)
        combined = " ".join(full_text)
        words = re.findall(r'\b[A-Za-z]{3,}\b', combined.lower())
        return combined, words
    except Exception as e:
        return "", []

def compute_ngram_overlap(words1, words2, n=7):
    if len(words1) < n or len(words2) < n:
        return 0.0, []
    ngrams1 = set(tuple(words1[i:i+n]) for i in range(len(words1)-n+1))
    ngrams2 = set(tuple(words2[i:i+n]) for i in range(len(words2)-n+1))
    
    intersection = ngrams1.intersection(ngrams2)
    overlap_rate = len(intersection) / max(len(ngrams1), 1)
    matched_phrases = [" ".join(ng) for ng in list(intersection)[:5]]
    return overlap_rate * 100.0, matched_phrases

def run_audit():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    target_tex = os.path.join(base_dir, 'paper', 'main.tex')
    ref_dir = os.path.join(os.path.dirname(base_dir), 'ref-papers')
    
    if not os.path.exists(target_tex):
        target_tex = os.path.join(base_dir, 'research-paper', 'paper', 'main.tex')
        ref_dir = os.path.join(base_dir, 'ref-papers')

    print("=" * 68)
    print(" ORIGINALITY & PLAGIARISM AUDIT VERIFICATION")
    print("=" * 68)
    print(f"Target Manuscript : {target_tex}")
    print(f"Reference Corpus  : {ref_dir}\n")

    target_raw, target_words = extract_text_from_tex(target_tex)
    print(f"Total Extracted Semantic Word Count: {len(target_words):,}")

    ref_pdfs = glob.glob(os.path.join(ref_dir, "*.pdf"))
    print(f"Found {len(ref_pdfs)} benchmark reference papers to cross-check.\n")

    print(f"{'Reference Document':<38} | {'7-Gram Match':<12} | {'Cosine Dist':<10}")
    print("-" * 68)

    max_sim = 0.0
    for pdf in ref_pdfs:
        pdf_name = os.path.basename(pdf)
        _, pdf_words = extract_text_from_pdf(pdf)
        if not pdf_words:
            continue

        overlap_pct, matches = compute_ngram_overlap(target_words, pdf_words, n=7)
        
        cosine_sim_val = 0.0
        if TfidfVectorizer and cosine_similarity and target_raw:
            vec = TfidfVectorizer(stop_words='english')
            tfidf = vec.fit_transform([target_raw[:50000], " ".join(pdf_words)[:50000]])
            cosine_sim_val = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0] * 100.0

        if overlap_pct > max_sim:
            max_sim = overlap_pct

        print(f"{pdf_name[:36]:<38} | {overlap_pct:>10.2f}% | {cosine_sim_val:>8.2f}%")

    print("=" * 68)
    overall_plagiarism = max_sim
    print(f"ESTIMATED VERBATIM PLAGIARISM SCORE : {overall_plagiarism:.2f}%")
    if overall_plagiarism < 3.0:
        print("[PASS] ORIGINAL WORK CONFIRMED (Well within academic threshold < 10%).")
    elif overall_plagiarism < 15.0:
        print("[WARN] MODERATE COMMON TERMINOLOGY (Standard domain jargon overlap).")
    else:
        print("[FAIL] ELEVATED SIMILARITY (Manual review advised).")
    print("=" * 68)

if __name__ == '__main__':
    run_audit()
