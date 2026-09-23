#!/usr/bin/env python3
"""
Master Visualization Pipeline: Cybersecurity in the Age of AI
Executes both quantitative chart generation and conceptual diagram rendering.
"""

import os
import subprocess
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SCRIPTS_DIR = os.path.join(BASE_DIR, "scripts")

def run_pipeline():
    print("=" * 60)
    print("RUNNING MASTER VISUALIZATION AND FIGURE PIPELINE")
    print("=" * 60)
    
    chart_script = os.path.join(SCRIPTS_DIR, "generate_charts.py")
    diagram_script = os.path.join(SCRIPTS_DIR, "generate_diagrams.py")
    
    print(f"Executing: {chart_script}")
    subprocess.check_call([sys.executable, chart_script])
    
    print(f"Executing: {diagram_script}")
    subprocess.check_call([sys.executable, diagram_script])
    
    print("=" * 60)
    print("ALL 4 QUANTITATIVE FIGURES AND 4 CONCEPTUAL DIAGRAMS GENERATED")
    print("=" * 60)

if __name__ == '__main__':
    run_pipeline()
