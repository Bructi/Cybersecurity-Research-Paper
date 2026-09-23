#!/usr/bin/env python3
"""
Scientific Visualization Script: Cybersecurity in the Age of AI
Generates publication-quality charts from verified empirical datasets.
Optimized for high-clarity A4 printout with large bold fonts.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Configure aesthetics for academic publication print
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['DejaVu Sans', 'Arial', 'Helvetica', 'Liberation Sans'],
    'font.size': 10.5,
    'axes.labelsize': 11.5,
    'axes.titlesize': 12.5,
    'axes.titleweight': 'bold',
    'axes.labelweight': 'bold',
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 9.5,
    'figure.titlesize': 13,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight'
})

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "figures", "data")
OUTPUT_DIR = os.path.join(BASE_DIR, "figures")

os.makedirs(OUTPUT_DIR, exist_ok=True)

def plot_figure_01():
    """Figure 1: Longitudinal Growth of Ransomware Incidents (2020-2025)"""
    csv_path = os.path.join(DATA_DIR, "figure01_ransomware_victim_volume.csv")
    df = pd.read_csv(csv_path)

    fig, ax = plt.subplots(figsize=(7.2, 4.2))
    
    x = df['Year']
    y_total = df['Total_Claimed_Victims']
    y_disclosed = df['Disclosed_Victims']
    
    width = 0.35
    ax.bar(x - width/2, y_total, width, label='Total Claimed / Leak Site Victims', color='#1e40af', edgecolor='black', linewidth=1.2, alpha=0.9)
    ax.bar(x + width/2, y_disclosed, width, label='Confirmed Disclosed Victims', color='#ea580c', edgecolor='black', linewidth=1.2, alpha=0.9)
    
    for i, val in enumerate(y_total):
        ax.text(x[i] - width/2, val + 120, f"{val:,}", ha='center', va='bottom', fontsize=9.2, fontweight='bold', color='#1e3a8a')
    for i, val in enumerate(y_disclosed):
        ax.text(x[i] + width/2, val + 120, f"{val:,}", ha='center', va='bottom', fontsize=9.2, fontweight='bold', color='#9a3412')

    ax.set_title("Longitudinal Growth of Ransomware Victim Volume (2020–2025)", pad=12)
    ax.set_xlabel("Calendar Year")
    ax.set_ylabel("Documented Victim Organizations")
    ax.set_ylim(0, 8500)
    ax.legend(loc='upper left', frameon=True, framealpha=0.95)
    
    fig.text(0.08, -0.06, "Data Source: DNI CTIIC Worldwide Threat Assessments, Black Kite 2025, Chainalysis 2026.", 
             fontsize=8.5, style='italic', color='#334155')
    
    out_path = os.path.join(OUTPUT_DIR, "figure01_ransomware_trends.png")
    plt.savefig(out_path)
    plt.close()
    print(f"Generated: {out_path}")

def plot_figure_02():
    """Figure 2: Attack Lifecycle Temporal Compression (Log Scale)"""
    csv_path = os.path.join(DATA_DIR, "figure02_attack_lifecycle_compression.csv")
    df = pd.read_csv(csv_path)

    fig, ax = plt.subplots(figsize=(7.5, 4.4))
    
    metrics = [
        "Vulnerability Weaponization",
        "Initial Access to Exfiltration",
        "Phishing Campaign Generation",
        "Traditional SOC MTTD",
        "AI-Augmented SOC MTTD"
    ]
    
    values_2020 = df['Year_2020_Minutes'].values
    values_2022 = df['Year_2022_Minutes'].values
    values_2024 = df['Year_2024_Minutes'].values
    values_2026 = df['Year_2026_Frontier_Minutes'].values

    y_pos = np.arange(len(metrics))
    bar_height = 0.18
    
    ax.barh(y_pos + 1.5*bar_height, values_2020, bar_height, label='2020 Baseline', color='#6366f1', edgecolor='black', linewidth=0.8, alpha=0.9)
    ax.barh(y_pos + 0.5*bar_height, values_2022, bar_height, label='2022 GenAI Inflection', color='#0d9488', edgecolor='black', linewidth=0.8, alpha=0.9)
    ax.barh(y_pos - 0.5*bar_height, values_2024, bar_height, label='2024 LLM Tooling', color='#db2777', edgecolor='black', linewidth=0.8, alpha=0.9)
    ax.barh(y_pos - 1.5*bar_height, values_2026, bar_height, label='2026 Frontier Autonomous', color='#d97706', edgecolor='black', linewidth=0.8, alpha=0.9)

    ax.set_xscale('log')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(metrics, fontweight='bold')
    ax.set_xlabel("Duration in Minutes (Logarithmic Scale)")
    ax.set_title("Attack & Defensive Lifecycle Temporal Compression (2020–2026)", pad=12)
    ax.legend(loc='lower left', frameon=True, framealpha=0.95)
    
    fig.text(0.08, -0.06, "Data Source: ENISA Frontier AI Assessment, CrowdStrike Global Threat Report, Mandiant.", 
             fontsize=8.5, style='italic', color='#334155')
    
    out_path = os.path.join(OUTPUT_DIR, "figure02_lifecycle_compression.png")
    plt.savefig(out_path)
    plt.close()
    print(f"Generated: {out_path}")

def plot_figure_03():
    """Figure 3: Initial Access Vectors and AI Adoption Penetration"""
    csv_path = os.path.join(DATA_DIR, "figure03_initial_access_vectors.csv")
    df = pd.read_csv(csv_path)

    fig, ax1 = plt.subplots(figsize=(7.2, 4.2))

    x = np.arange(len(df['Vector_Name']))
    labels = [v.replace('_', ' ') for v in df['Vector_Name']]
    
    color_share = '#2563eb'
    color_ai = '#dc2626'
    
    rects1 = ax1.bar(x - 0.18, df['Percentage_Share'], 0.36, label='Share of Total Intrusions (%)', color=color_share, edgecolor='black', linewidth=1.0, alpha=0.9)
    rects2 = ax1.bar(x + 0.18, df['AI_Integration_Rate_Percent'], 0.36, label='AI Integration Rate in Vector (%)', color=color_ai, edgecolor='black', linewidth=1.0, alpha=0.9)

    ax1.set_ylabel('Percentage (%)')
    ax1.set_title('Primary Intrusion Vectors vs. AI Adoption Penetration', pad=12)
    ax1.set_xticks(x)
    ax1.set_xticklabels(labels, rotation=12, ha='right', fontweight='bold')
    ax1.set_ylim(0, 100)
    ax1.legend(loc='upper right', frameon=True, framealpha=0.95)

    for r in rects1:
        h = r.get_height()
        ax1.annotate(f'{h:.1f}%', xy=(r.get_x() + r.get_width()/2, h), xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=8.8, fontweight='bold', color='#1e3a8a')
    for r in rects2:
        h = r.get_height()
        ax1.annotate(f'{h:.1f}%', xy=(r.get_x() + r.get_width()/2, h), xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=8.8, color='#991b1b', fontweight='bold')

    fig.text(0.08, -0.08, "Data Source: ENISA Threat Landscape 2025 (4,875 incidents evaluated), CISA Advisories.", 
             fontsize=8.5, style='italic', color='#334155')

    out_path = os.path.join(OUTPUT_DIR, "figure03_initial_access_vectors.png")
    plt.savefig(out_path)
    plt.close()
    print(f"Generated: {out_path}")

def plot_figure_04():
    """Figure 4: Ransomware Extortion Economics: Payments vs Median Ransom Size"""
    csv_path = os.path.join(DATA_DIR, "figure04_ransomware_economics.csv")
    df = pd.read_csv(csv_path)

    fig, ax1 = plt.subplots(figsize=(7.2, 4.2))

    x = df['Year']
    ax2 = ax1.twinx()

    line1 = ax1.plot(x, df['Total_OnChain_Payments_USD_Millions'], 'o-', color='#1e40af', linewidth=2.8, markersize=7, label='Total On-Chain Payments ($M USD)')
    line2 = ax2.plot(x, df['Median_Payment_USD'], 's--', color='#ea580c', linewidth=2.8, markersize=7, label='Median Ransom Payment ($ USD)')

    ax1.set_xlabel('Calendar Year')
    ax1.set_ylabel('Total Extortion Payments ($M USD)', color='#1e40af', fontweight='bold')
    ax2.set_ylabel('Median Ransom Payment ($ USD)', color='#ea580c', fontweight='bold')
    
    ax1.tick_params(axis='y', labelcolor='#1e40af')
    ax2.tick_params(axis='y', labelcolor='#ea580c')
    ax1.set_ylim(400, 1300)
    ax2.set_ylim(0, 75000)

    lines = line1 + line2
    labels = [l.get_label() for l in lines]
    ax1.legend(lines, labels, loc='upper left', frameon=True, framealpha=0.95)

    plt.title('Ransomware Macroeconomics: Total Volume vs. Median Payment (2021–2025)', pad=12)
    
    fig.text(0.08, -0.06, "Data Source: Chainalysis 2026 Crypto Crime Report, Sophos State of Ransomware 2025.", 
             fontsize=8.5, style='italic', color='#334155')

    out_path = os.path.join(OUTPUT_DIR, "figure04_ransomware_macroeconomics.png")
    plt.savefig(out_path)
    plt.close()
    print(f"Generated: {out_path}")

if __name__ == '__main__':
    print("Generating academic figures...")
    plot_figure_01()
    plot_figure_02()
    plot_figure_03()
    plot_figure_04()
    print("All figures successfully generated in figures/ directory.")
