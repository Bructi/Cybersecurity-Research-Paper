#!/usr/bin/env python3
"""
Publication-Grade High-Legibility Diagram Generator for AI-Cybersecurity Research Paper.
Specifically optimized for high-clarity A4 physical printout:
- Large, bold, high-contrast typography (clearly readable with naked eyes on A4 paper).
- Exact aspect ratio matching LaTeX textwidth / columnwidth.
- Rich distinct color coding (WCAG AAA contrast).
- High resolution 300+ DPI PNG + scalable SVG.
"""

import os
import textwrap
import matplotlib.pyplot as plt
import matplotlib.patches as patches

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIAGRAMS_DIR = os.path.join(BASE_DIR, "diagrams")
FIGURES_DIR = os.path.join(BASE_DIR, "figures")

os.makedirs(DIAGRAMS_DIR, exist_ok=True)
os.makedirs(FIGURES_DIR, exist_ok=True)

# Global styling optimized for high-clarity print
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['DejaVu Sans', 'Arial', 'Helvetica', 'Liberation Sans'],
    'font.size': 11,
    'font.weight': 'medium',
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight'
})

def create_diagram_a_attack_lifecycle():
    """Diagram A: AI-Enhanced Cyber Attack Lifecycle (Optimized for full-width print)"""
    fig, ax = plt.subplots(figsize=(13.5, 6.2))
    ax.set_xlim(0, 13.5)
    ax.set_ylim(0, 6.5)
    ax.axis('off')

    # Main Title
    ax.text(6.75, 6.15, "AI-Enhanced Cyber Attack Lifecycle & Temporal Acceleration", 
            fontsize=15, fontweight='bold', ha='center', color='#0f172a')
    ax.text(6.75, 5.75, "Machine-Speed Adversarial Progression Across the Cyber Kill Chain (Reconnaissance to Impact)", 
            fontsize=11.5, style='italic', ha='center', color='#334155')

    stages = [
        ("1. RECON", "• OSINT Scraping\n• LLM Target Profiling\n• Subdomain Probing", "#e0f2fe", "#0284c7", "#0369a1"),
        ("2. WEAPONIZE", "• Polymorphic Code\n• AI Obfuscation\n• Anti-EDR Payloads", "#e0f2fe", "#0284c7", "#0369a1"),
        ("3. SOCIAL ENG.", "• Deepfake Audio/Video\n• Context Phishing\n• Multilingual Lures", "#fee2e2", "#dc2626", "#b91c1c"),
        ("4. EXPLOIT", "• <15m PoC Synthesis\n• Zero-Day Guidance\n• Smart Fuzzing", "#fee2e2", "#dc2626", "#b91c1c"),
        ("5. PERSIST", "• Living-off-the-Land\n• Adaptive C2 Beacons\n• Self-Healing Bots", "#fef3c7", "#d97706", "#b45309"),
        ("6. EXFILTRATE", "• Auto File Triage\n• Encrypted Tunnels\n• 72m Breach Window", "#dcfce7", "#16a34a", "#15803d"),
        ("7. IMPACT", "• Triple Extortion\n• Auto-Negotiation\n• Model Weight Theft", "#f3e8ff", "#9333ea", "#7e22ce")
    ]

    box_width = 1.55
    box_height = 3.4
    gap = 0.28
    start_x = 0.45

    for i, (title, ai_role, bg_color, border_color, text_color) in enumerate(stages):
        x = start_x + i * (box_width + gap)
        y = 1.85
        
        # Container box
        rect = patches.FancyBboxPatch((x, y), box_width, box_height,
                                      boxstyle="round,pad=0.04,rounding_size=0.12",
                                      facecolor=bg_color, edgecolor=border_color, linewidth=2.2)
        ax.add_patch(rect)

        # Stage Header Box
        header_rect = patches.FancyBboxPatch((x + 0.04, y + box_height - 0.65), box_width - 0.08, 0.6,
                                             boxstyle="round,pad=0.02,rounding_size=0.08",
                                             facecolor=border_color, edgecolor=border_color)
        ax.add_patch(header_rect)
        ax.text(x + box_width/2, y + box_height - 0.35, title,
                fontsize=10.5, fontweight='bold', color='white', ha='center', va='center')

        # Subtitle badge
        ax.text(x + box_width/2, y + box_height - 0.95, "AI CAPABILITIES",
                fontsize=8.5, fontweight='bold', color=text_color, ha='center')

        # Content text
        ax.text(x + 0.12, y + 1.25, ai_role,
                fontsize=9.2, fontweight='medium', color='#0f172a', ha='left', va='center', linespacing=1.45)

        # Transition arrow
        if i < len(stages) - 1:
            ax.annotate('', xy=(x + box_width + gap - 0.03, y + box_height/2),
                        xytext=(x + box_width + 0.03, y + box_height/2),
                        arrowprops=dict(arrowstyle="-|>", color="#1e293b", lw=2.2, mutation_scale=16))

    # Bottom summary banner
    summary_rect = patches.FancyBboxPatch((0.45, 0.35), 12.6, 1.15,
                                          boxstyle="round,pad=0.05,rounding_size=0.10",
                                          facecolor="#f8fafc", edgecolor="#94a3b8", linewidth=1.8)
    ax.add_patch(summary_rect)
    ax.text(6.75, 1.12, "KEY MEASURABLE TEMPORAL COMPRESSION METRICS", 
            fontsize=11.0, fontweight='bold', color='#0f172a', ha='center')
    ax.text(6.75, 0.65, 
            "Vulnerability Weaponization: < 15 Min (ENISA)  |  Breakout Time: 72 Min Median (CrowdStrike)\n"
            "Social Engineering Automation: 81.4% Adoption in Active Phishing (ENISA ETL / SlashNext)",
            fontsize=9.8, fontweight='medium', ha='center', color='#1e293b', linespacing=1.35)

    plt.tight_layout()
    for dest_dir in [DIAGRAMS_DIR, FIGURES_DIR]:
        plt.savefig(os.path.join(dest_dir, "diagram_a_attack_lifecycle.png"), dpi=300)
        plt.savefig(os.path.join(dest_dir, "diagram_a_attack_lifecycle.svg"))
    plt.close()
    print("Generated Diagram A: Attack Lifecycle (High-Legibility)")


def create_diagram_b_defense_lifecycle():
    """Diagram B: AI-Enhanced Cyber Defense Lifecycle (Optimized for full-width print)"""
    fig, ax = plt.subplots(figsize=(13.5, 6.4))
    ax.set_xlim(0, 13.5)
    ax.set_ylim(0, 6.7)
    ax.axis('off')

    # Main Title
    ax.text(6.75, 6.35, "AI-Enhanced Autonomous Cyber Defense Architecture", 
            fontsize=15, fontweight='bold', ha='center', color='#0f172a')
    ax.text(6.75, 5.95, "Continuous Streaming Telemetry, Graph Anomaly Detection, Machine-Speed Containment & Feedback", 
            fontsize=11.5, style='italic', ha='center', color='#334155')

    stages = [
        ("1. TELEMETRY", "• Multi-Source Logs\n• Streaming Parsers\n• Provenance Graphs", "#e0f2fe", "#0284c7", "#0369a1"),
        ("2. ANOMALY DET.", "• Deep Autoencoders\n• Isolation Forests\n• Sub-Second Alerts", "#e0f2fe", "#0284c7", "#0369a1"),
        ("3. CLASSIFY", "• Graph Neural Nets\n• MITRE ATLAS Tactic\n• Noise Filtering", "#ccfbf1", "#0d9488", "#0f766e"),
        ("4. INTEL FUSION", "• Automated IoCs\n• Dark-Web Parsing\n• Synthetic Feeds", "#ccfbf1", "#0d9488", "#0f766e"),
        ("5. AUTO-ACTION", "• Host Isolation\n• Dynamic ACL Push\n• Session Revocation", "#ffedd5", "#ea580c", "#c2410c"),
        ("6. REMEDIATION", "• Auto-Patching\n• State Rollbacks\n• AIxCC Reasoning", "#dcfce7", "#16a34a", "#15803d"),
        ("7. RETRAINING", "• Adversarial Updates\n• Drift Monitoring\n• Model Fine-Tuning", "#f3e8ff", "#9333ea", "#7e22ce")
    ]

    box_width = 1.55
    box_height = 3.4
    gap = 0.28
    start_x = 0.45

    for i, (title, def_role, bg_color, border_color, text_color) in enumerate(stages):
        x = start_x + i * (box_width + gap)
        y = 1.95
        
        rect = patches.FancyBboxPatch((x, y), box_width, box_height,
                                      boxstyle="round,pad=0.04,rounding_size=0.12",
                                      facecolor=bg_color, edgecolor=border_color, linewidth=2.2)
        ax.add_patch(rect)

        header_rect = patches.FancyBboxPatch((x + 0.04, y + box_height - 0.65), box_width - 0.08, 0.6,
                                             boxstyle="round,pad=0.02,rounding_size=0.08",
                                             facecolor=border_color, edgecolor=border_color)
        ax.add_patch(header_rect)
        ax.text(x + box_width/2, y + box_height - 0.35, title,
                fontsize=10.2, fontweight='bold', color='white', ha='center', va='center')

        ax.text(x + box_width/2, y + box_height - 0.95, "DEFENSIVE CORE",
                fontsize=8.5, fontweight='bold', color=text_color, ha='center')

        ax.text(x + 0.12, y + 1.25, def_role,
                fontsize=9.2, fontweight='medium', color='#0f172a', ha='left', va='center', linespacing=1.45)

        if i < len(stages) - 1:
            ax.annotate('', xy=(x + box_width + gap - 0.03, y + box_height/2),
                        xytext=(x + box_width + 0.03, y + box_height/2),
                        arrowprops=dict(arrowstyle="-|>", color="#0369a1", lw=2.2, mutation_scale=16))

    # Feedback loop arrow from stage 7 back to stage 1
    ax.annotate('', xy=(start_x + box_width/2, 1.85),
                xytext=(start_x + 6 * (box_width + gap) + box_width/2, 1.85),
                arrowprops=dict(arrowstyle="-|>", color="#7e22ce", lw=2.6, linestyle="--",
                                connectionstyle="arc3,rad=-0.14", mutation_scale=18))
    ax.text(6.75, 1.25, "CONTINUOUS ADVERSARIAL RETRAINING & MODEL DRIFT MITIGATION LOOP",
            fontsize=9.8, fontweight='bold', color='#6b21a8', ha='center')

    # Bottom summary banner
    summary_rect = patches.FancyBboxPatch((0.45, 0.3), 12.6, 0.75,
                                          boxstyle="round,pad=0.05,rounding_size=0.10",
                                          facecolor="#f8fafc", edgecolor="#94a3b8", linewidth=1.8)
    ax.add_patch(summary_rect)
    ax.text(6.75, 0.67, 
            "SOC Mean Time to Detect (MTTD): 480 min (Manual) → 8 min (AI-Augmented Streaming)  |  NIST CSF 2.0 AI Profile",
            fontsize=9.8, fontweight='bold', ha='center', color='#0f172a')

    plt.tight_layout()
    for dest_dir in [DIAGRAMS_DIR, FIGURES_DIR]:
        plt.savefig(os.path.join(dest_dir, "diagram_b_defense_lifecycle.png"), dpi=300)
        plt.savefig(os.path.join(dest_dir, "diagram_b_defense_lifecycle.svg"))
    plt.close()
    print("Generated Diagram B: Defense Lifecycle (High-Legibility)")


def create_diagram_c_threat_taxonomy():
    """Diagram C: AI Cybersecurity Threat Taxonomy (High-Contrast 3-Column Layout)"""
    fig, ax = plt.subplots(figsize=(13.5, 7.8))
    ax.set_xlim(0, 13.5)
    ax.set_ylim(0, 8.2)
    ax.axis('off')

    # Header
    ax.text(6.75, 7.85, "Comprehensive AI-Cybersecurity Threat & Vulnerability Taxonomy", 
            fontsize=15, fontweight='bold', ha='center', color='#0f172a')
    ax.text(6.75, 7.45, "Structured Classification Across Generative Attacks, Model Vulnerabilities, and Agentic Infrastructure", 
            fontsize=11.5, style='italic', ha='center', color='#334155')

    columns = [
        ("1. GENERATIVE OFFENSIVE ATTACKS", 
         "#b91c1c", "#fef2f2", "#991b1b",
         [
             ("Hyper-Realistic Phishing", "Context-aware, multilingual spearphishing lures generated at scale (81.4% adoption)."),
             ("Multi-Modal Deepfakes", "Real-time acoustic voice cloning and video synthesis for executive fraud."),
             ("Polymorphic Malware", "Automated code synthesis dynamically modifying binary signatures to evade EDR."),
             ("Automated Reconnaissance", "LLM-driven OSINT aggregation, network perimeter scans, and target profiling."),
             ("15-Min Exploit Generation", "Automated synthesis of functional exploits from public CVE advisory text.")
         ]),
        ("2. ADVERSARIAL ML & MODEL ATTACKS", 
         "#c2410c", "#fff7ed", "#9a3412",
         [
             ("Direct / Indirect Prompt Injection", "Hijacking model execution flow via malicious untrusted data tokens (OWASP LLM01)."),
             ("Training Data & Model Poisoning", "Injecting stealthy backdoors into training corpuses and fine-tuning datasets."),
             ("Adversarial Evasion (FGSM/GCG)", "Gradient-optimized input perturbations forcing deliberate misclassification."),
             ("Model Extraction & Distillation", "Exfiltrating billions of tokens to reverse-engineer model weights and CoT reasoning."),
             ("Membership Inference & Inversion", "Reconstructing confidential PII and training records from output logits.")
         ]),
        ("3. AGENTIC & INFRASTRUCTURE RISKS", 
         "#1d4ed8", "#eff6ff", "#1e40af",
         [
             ("Excessive Agent Autonomy", "Tool-calling agents executing irreversible writes/deletions without human gates."),
             ("AI Supply Chain Poisoning", "Tampered foundation weights on public hubs and compromised LoRA adapters."),
             ("Vector DB & RAG Hijacking", "Corrupting semantic vector embeddings to induce malicious retrieval execution."),
             ("Shadow AI & Token Leakage", "Unsanctioned internal enterprise tool usage exfiltrating sensitive IP."),
             ("Autonomous Agent Swarms", "Coordinated multi-agent networks executing distributed cyber intrusion pipelines.")
         ])
    ]

    col_width = 3.9
    col_gap = 0.35
    start_x = 0.5

    for col_idx, (col_title, header_bg, card_bg, border_color, items) in enumerate(columns):
        col_x = start_x + col_idx * (col_width + col_gap)
        
        # Column Header Box
        header_rect = patches.FancyBboxPatch((col_x, 6.55), col_width, 0.65,
                                             boxstyle="round,pad=0.03,rounding_size=0.08",
                                             facecolor=header_bg, edgecolor=header_bg)
        ax.add_patch(header_rect)
        ax.text(col_x + col_width/2, 6.88, col_title,
                fontsize=10.5, fontweight='bold', color='white', ha='center', va='center')

        # Items in column
        card_height = 1.05
        card_gap = 0.18
        for item_idx, (item_title, item_desc) in enumerate(items):
            item_y = 6.55 - (item_idx + 1) * (card_height + card_gap) + 0.12
            
            card_rect = patches.FancyBboxPatch((col_x, item_y), col_width, card_height,
                                               boxstyle="round,pad=0.03,rounding_size=0.08",
                                               facecolor=card_bg, edgecolor=border_color, linewidth=1.5)
            ax.add_patch(card_rect)
            
            # Item Title
            ax.text(col_x + 0.12, item_y + card_height - 0.26, f"• {item_title}",
                    fontsize=9.5, fontweight='bold', color=border_color, ha='left', va='center')
            
            # Item Description (wrapped cleanly)
            wrapped_desc = textwrap.fill(item_desc, width=44)
            ax.text(col_x + 0.12, item_y + 0.38, wrapped_desc,
                    fontsize=8.5, fontweight='medium', color='#1e293b', ha='left', va='center', linespacing=1.3)

    plt.tight_layout()
    for dest_dir in [DIAGRAMS_DIR, FIGURES_DIR]:
        plt.savefig(os.path.join(dest_dir, "diagram_c_threat_taxonomy.png"), dpi=300)
        plt.savefig(os.path.join(dest_dir, "diagram_c_threat_taxonomy.svg"))
    plt.close()
    print("Generated Diagram C: Threat Taxonomy (High-Legibility)")


def create_diagram_d_feedback_framework():
    """Diagram D: Co-Evolutionary Feedback Loop Framework (Clear Axis & Flow for Print)"""
    fig, ax = plt.subplots(figsize=(13.5, 7.8))
    ax.set_xlim(0, 13.5)
    ax.set_ylim(0, 8.2)
    ax.axis('off')

    # Header
    ax.text(6.75, 7.85, "The Co-Evolutionary AI-Cybersecurity Feedback Loop Framework", 
            fontsize=15, fontweight='bold', ha='center', color='#0f172a')
    ax.text(6.75, 7.45, "Theoretical Dynamics of Asymmetric Offensive Velocity, Defensive Adaptation, and Counter-AI Subversion", 
            fontsize=11.5, style='italic', ha='center', color='#334155')

    # 4 Quadrants / Core Nodes
    nodes = [
        ("OFFENSIVE SPEED ACCELERATION", 
         "• Weaponization in <15 minutes\n• Mass autonomous spearphishing\n• Automated vulnerability chaining\n• Polymorphic evasion payloads",
         0.6, 4.0, 5.6, 2.8, "#fee2e2", "#dc2626", "#991b1b"),
        
        ("DEFENSIVE MACHINE-SPEED RESPONSE", 
         "• MTTD compressed (480m → 8m)\n• Real-time graph neural correlation\n• Autonomous SOAR microsegmentation\n• DARPA AIxCC auto-patching",
         7.3, 4.0, 5.6, 2.8, "#e0f2fe", "#0284c7", "#0369a1"),
        
        ("ADVERSARIAL COUNTER-AI SUBVERSION", 
         "• Direct / indirect prompt injection\n• Gradient evasion (FGSM / GCG)\n• Industrial model distillation\n• Training set poisoning",
         0.6, 0.7, 5.6, 2.8, "#ffedd5", "#ea580c", "#c2410c"),
        
        ("RESILIENT ZERO-TRUST AI ARCHITECTURE", 
         "• Dual-LLM context isolation\n• Cryptographic AIBOM verification\n• Strict Human-in-the-Loop gates\n• Hardware neural enclave security",
         7.3, 0.7, 5.6, 2.8, "#dcfce7", "#16a34a", "#15803d")
    ]

    for title, desc, x, y, w, h, bg, border, title_col in nodes:
        rect = patches.FancyBboxPatch((x, y), w, h,
                                      boxstyle="round,pad=0.04,rounding_size=0.10",
                                      facecolor=bg, edgecolor=border, linewidth=2.0)
        ax.add_patch(rect)
        
        # Header banner inside box
        header_rect = patches.FancyBboxPatch((x + 0.04, y + h - 0.55), w - 0.08, 0.5,
                                             boxstyle="round,pad=0.02,rounding_size=0.06",
                                             facecolor=border, edgecolor=border)
        ax.add_patch(header_rect)
        ax.text(x + w/2, y + h - 0.30, title,
                fontsize=10.5, fontweight='bold', color='white', ha='center', va='center')
        
        # Description bullets
        ax.text(x + 0.2, y + 1.1, desc,
                fontsize=9.5, fontweight='medium', color='#0f172a', ha='left', va='center', linespacing=1.45)

    # Dynamic connecting arrows
    # 1. Offense -> Defense (Forces machine-speed defense)
    ax.annotate('', xy=(7.2, 5.4), xytext=(6.3, 5.4),
                arrowprops=dict(arrowstyle="-|>", color="#0f172a", lw=2.8, mutation_scale=18))
    ax.text(6.75, 5.65, "Forces", fontsize=9.5, fontweight='bold', color='#0f172a', ha='center')

    # 2. Defense -> Counter-AI (Drives adversary to target defense ML)
    ax.annotate('', xy=(3.4, 3.6), xytext=(7.5, 3.9),
                arrowprops=dict(arrowstyle="-|>", color="#c2410c", lw=2.8, mutation_scale=18,
                                connectionstyle="arc3,rad=-0.12"))
    ax.text(5.5, 3.75, "Triggers Adversarial Subversion", fontsize=9.2, fontweight='bold', color='#c2410c', ha='center')

    # 3. Counter-AI -> Zero-Trust (Mandates robust isolation)
    ax.annotate('', xy=(7.2, 2.1), xytext=(6.3, 2.1),
                arrowprops=dict(arrowstyle="-|>", color="#0f172a", lw=2.8, mutation_scale=18))
    ax.text(6.75, 2.35, "Mandates", fontsize=9.5, fontweight='bold', color='#0f172a', ha='center')

    # 4. Zero-Trust -> Offense (Constrains attack surface)
    ax.annotate('', xy=(3.4, 4.0), xytext=(7.5, 3.6),
                arrowprops=dict(arrowstyle="-|>", color="#15803d", lw=2.8, linestyle="--", mutation_scale=18,
                                connectionstyle="arc3,rad=-0.12"))
    ax.text(5.5, 3.4, "Constrains Attack Surface", fontsize=9.2, fontweight='bold', color='#15803d', ha='center')

    plt.tight_layout()
    for dest_dir in [DIAGRAMS_DIR, FIGURES_DIR]:
        plt.savefig(os.path.join(dest_dir, "diagram_d_feedback_framework.png"), dpi=300)
        plt.savefig(os.path.join(dest_dir, "diagram_d_feedback_framework.svg"))
    plt.close()
    print("Generated Diagram D: Feedback Framework (High-Legibility)")

if __name__ == "__main__":
    create_diagram_a_attack_lifecycle()
    create_diagram_b_defense_lifecycle()
    create_diagram_c_threat_taxonomy()
    create_diagram_d_feedback_framework()
