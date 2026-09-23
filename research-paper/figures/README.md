# Figures and Empirical Datasets Documentation

## Project: Cybersecurity in the Age of Artificial Intelligence
**Repository Subdirectory:** `/figures/data/`  
**Date of Audit:** September 18, 2026  

---

### Overview

This directory preserves all raw quantitative datasets used to generate visual figures and statistical analysis for the research paper. Every dataset corresponds strictly to verified government reports (ENISA, CTIIC/DNI, NIST, CISA) or methodologically transparent industry threat telemetry (Black Kite, Chainalysis, Sophos, BlackFog, GuidePoint GRIT).

---

### Dataset Inventory and Metadata

#### 1. `figure01_ransomware_victim_volume.csv`
- **Metric:** Annual volume of claimed and publicly disclosed ransomware victims (2020–2025).
- **Primary Sources:**
  - U.S. Office of the Director of National Intelligence (ODNI) - Cyber Threat Intelligence Integration Center (CTIIC), *Worldwide Ransomware 2024*.
  - Black Kite Research Group, *2025 Ransomware Report*.
  - BlackFog, *2025 State of Ransomware Report*.
  - Chainalysis, *2026 Crypto Crime Report (Ransomware Section)*.
- **Methodology & Harmonization:**
  - Data points reflect dark-web data leak site postings and confirmed public victim disclosures.
  - Undisclosed victims (attacks where negotiations occur without leak site postings) are estimated to represent 86% of total operational activity (BlackFog 2025).
- **Key Trend:** Total claimed victims grew from 2,593 in 2022 to 7,079 in 2025, driven by RaaS fragmentation and automated reconnaissance tooling.

#### 2. `figure02_attack_lifecycle_compression.csv`
- **Metric:** Attack lifecycle temporal compression (in minutes) across 2020, 2022, 2024, and 2026 frontier environments.
- **Primary Sources:**
  - European Union Agency for Cybersecurity (ENISA), *ENISA's View on Cybersecurity in the Frontier AI Era* (July 2026).
  - ENISA Threat Landscape 2025 (October 2025).
  - NIST Cybersecurity Framework Profile for AI (*NIST IR 8596*).
  - Industry telemetry benchmarks (CrowdStrike, Mandiant, SANS SOC surveys).
- **Key Metrics:**
  - Vulnerability-to-Exploit Window: Compressed from ~10,080 minutes (7 days) in 2020 to under 15 minutes in 2026 frontier AI environments.
  - Median Intrusion-to-Exfiltration: Compressed from 5,760 minutes (4 days) in 2020 to 72 minutes in 2026.
  - AI-Augmented Mean Time to Detect (MTTD): Reduced from 480 minutes in 2020 to ~8 minutes in 2026 AI-assisted SOCs.

#### 3. `figure03_initial_access_vectors.csv`
- **Metric:** Distribution of initial access vectors in global cyber incidents and corresponding rate of AI integration.
- **Primary Sources:**
  - ENISA Threat Landscape (ETL) 2025 (Sample: 4,875 curated European and global incidents, July 2024–June 2025).
  - CISA Joint Advisories (AA26-251A).
- **Key Finding:** Phishing and social engineering comprise 59.8% of primary intrusion vectors; over 81.4% of observed phishing campaigns utilize LLM generation for multi-lingual and personalized lure crafting.

#### 4. `figure04_ransomware_economics.csv`
- **Metric:** Macroeconomic dynamics of ransomware extortion: Total on-chain cryptocurrency payments, median ransom payment, average demand, and average non-ransom recovery cost (USD, 2021–2025).
- **Primary Sources:**
  - Chainalysis, *2026 Crypto Crime Report*.
  - Sophos, *State of Ransomware 2025* (Survey of 3,400 IT/security leaders across 17 countries).
- **Key Trend:** Total annual on-chain payments declined slightly from $892M (2024) to $820M (2025), but median ransom payment size surged 368% to $59,556 as threat actors optimized targeting toward high-liquidity victims while automating low-cost extortion.

---

### Reproducibility & Generation Instructions

To generate the figures and vector visualizations from these datasets:
```bash
python scripts/generate_charts.py
```
This script requires `matplotlib`, `seaborn`, and `pandas`. Output figures are rendered to `/figures/*.png` and `/figures/*.svg`.
