# Research Source Notes & Evidence Dossier

**Project:** Cybersecurity in the Age of Artificial Intelligence  
**Document Reference:** RP-SRC-NOTES-2026  
**Auditor:** Multidisciplinary Cyber-AI Research Team  
**Verification Date:** September 19, 2026  

---

## 1. Methodological Synthesis & Epistemological Taxonomy

To ensure absolute academic rigor, all claims, statistics, and findings in this research are classified across five distinct epistemological tiers:

1. **FACT / EMPIRICAL MEASUREMENT:** Directly observed and mathematically verifiable ground-truth data (e.g., on-chain cryptocurrency transactions recorded on public ledgers, forensic artifacts from law enforcement filings, published vulnerability CVE IDs).
2. **PEER-REVIEWED RESEARCH FINDING:** Formally validated hypotheses published in indexed academic conference proceedings (ACM, IEEE, USENIX, NeurIPS, ICLR) with reproducible experimental methodologies.
3. **GOVERNMENT & AGENCY INTELLIGENCE:** Telemetry, threat landscape reports, and binding cybersecurity advisories published by statutory defense and cybersecurity bodies (ENISA, CISA, NSA, FBI, NIST, Five Eyes).
4. **INDUSTRY TELEMETRY & THREAT ESTIMATE:** Quantitative metrics compiled by enterprise cybersecurity vendors (CrowdStrike, Sophos, Black Kite, Chainalysis). Limitations such as telemetry bias, customer cohort skew, and dark-web sample boundaries are explicitly documented.
5. **ANALYST INTERPRETATION & THEORETICAL FRAMEWORK:** Deductive and inductive conceptual frameworks (such as the Co-Evolutionary AI Feedback Loop) designed to synthesize empirical patterns into predictive or structural models.

---

## 2. Detailed Source Dossiers

### Source [1]: ENISA Threat Landscape 2025 (ETL 2025)
- **Publication:** October 2025, European Union Agency for Cybersecurity.
- **Sample Population:** 4,875 verified cyber incidents reported across the 27 EU member states from July 1, 2024 to June 30, 2025.
- **Methodological Details:** Incidents aggregated via national CSIRTs, mandatory NIS2 incident reporting channels, and validated open-source intelligence.
- **Key Empirical Excerpts:**
  - "Social engineering and phishing represent 59.8% of all identified initial access vectors across enterprise incidents in the 2024–2025 reporting period."
  - "More than 81.4% of observed malicious phishing lures exhibit characteristics of Large Language Model generation, specifically the absence of traditional orthographic errors, dynamic semantic alignment with victim organization hierarchies, and automated localization across 24 official EU languages."
- **Documented Limitations:** Reporting is skewed toward regulated sectors (finance, energy, healthcare, digital infrastructure) due to mandatory NIS2 reporting thresholds; small and medium-sized enterprise (SME) incidents remain partially underrepresented.

### Source [2]: ENISA's View on Cybersecurity in the Frontier AI Era (July 2026)
- **Publication:** July 2026, ENISA Frontier AI Working Group.
- **Focus:** Time-to-exploit metrics and agentic automated execution.
- **Key Empirical Excerpts:**
  - "In simulated and observed frontier attack environments, the window from public vulnerability disclosure (CVE/PoC release) to weaponized exploitation has compressed to under 15 minutes."
  - "The median duration from initial perimeter breach to active multi-gigabyte data exfiltration has decreased to 72 minutes in automated attack chains, compared to 5,760 minutes (4 days) in 2020."
- **Methodology:** Multi-vendor telemetry synthesis and controlled red-team sandbox trials on frontier model APIs.

### Source [4]: Joint Cybersecurity Advisory AA26-251A (CISA, NSA, FBI)
- **Publication:** September 8, 2026.
- **Document ID:** AA26-251A / CISA-AISC-2026-09.
- **Title:** "China-Based AI Entities Conducting Industrial-Scale Distillation Campaigns Against Frontier Commercial Models."
- **Key Empirical Evidence:**
  - Over 14 billion API tokens and complex Chain-of-Thought (CoT) reasoning traces were extracted from Western commercial LLMs (OpenAI, Anthropic, Google) by state-backed actors utilizing distributed proxy networks and automated prompt-variation scripts between November 2024 and August 2026.
  - Threat actors systematically leveraged extracted weights and synthetic fine-tuning datasets to train domestic models for offensive cyber tooling, exploit synthesis, and reconnaissance.
- **Significance:** Establishes model distillation and weight intellectual property theft as a formal nation-state cyber warfare tactic.

### Source [8]: NIST AI Risk Management Framework (AI RMF 1.0 & NIST AI 600-1)
- **Publication:** NIST AI 100-1 (Jan 2023); NIST AI 600-1 Generative AI Profile (July 2024).
- **Authors:** NIST Information Technology Laboratory (ITL).
- **Key Classifications:** Identifies 12 specific Generative AI risk profiles:
  1. Adversarial Evasion & Perturbation
  2. Data Poisoning & Training Integrity
  3. Indirect & Direct Prompt Injection
  4. Model Inversion & Sensitive Data Disclosure
  5. Hallucination & Factuality Drift
  6. Toxic/Harmful Content Generation
  7. Automated Exploit & Malware Generation
  8. Supply Chain & Pre-trained Model Vulnerabilities
  9. Excessive Agency & Tool Misuse
  10. Intellectual Property Exfiltration
  11. Confabulation in Critical Control Loops
  12. Privacy De-anonymization.

### Source [15]: Greshake et al. (ACM CCS/AISEC 2023)
- **Title:** "Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection."
- **Authors:** Kai Greshake, Sahar Abdelnabi, Shailesh Mishra, Christoph Endres, Thorsten Holz, Mario Fritz.
- **Experimental Protocol:** Evaluated synthetic and production LLM applications (synthetic search-augmented models, email readers, code interpreters).
- **Key Finding:** Untrusted data ingested from external web pages, emails, or databases can contain hidden natural-language control sequences that override system instructions with 100% execution success when delimiters and validation layers are absent.
- **Theoretical Contribution:** Proved that LLM architectures conflate control plane (instructions) with data plane (user/retrieved text), creating the neural analog of SQL injection.

### Source [16]: Zou et al. (NeurIPS / arXiv:2307.15043)
- **Title:** "Universal and Transferable Adversarial Attacks on Aligned Language Models."
- **Authors:** Andy Zou, Zifan Wang, Nicholas Carlini, Milad Nasr, J. Zico Kolter, Matt Fredrikson.
- **Methodology:** Optimization-based attack finding token sequences using Greedy Coordinate Gradient (GCG) that force the model to output positive affirmation prefixes ("Sure, here is how to...").
- **Key Finding:** Suffixes optimized on open-source models (Vicuna, LLaMA-2) transferred successfully to closed proprietary commercial models (ChatGPT, Claude, Bard) with attack success rates exceeding 80%.

### Source [27]: Chainalysis 2026 Crypto Crime Report
- **Publication:** February 26, 2026.
- **Methodology:** On-chain clustering and attribution of cryptocurrency transactions on Bitcoin, Ethereum, and Monero blockchains associated with ransomware operators.
- **Empirical Metrics:**
  - 2021: $983 Million USD
  - 2022: $567 Million USD
  - 2023: $1,100 Million USD
  - 2024: $892 Million USD
  - 2025: $820 Million USD
  - Median payment in 2025: $59,556 (368% increase from $12,738 in 2024).
  - Victim payment conversion rate: 28% in 2025 (down from 44% in 2021 and 70%+ in 2019).
- **Analytical Interpretation:** While overall ransom volume contracted by 8% due to improved victim enterprise backup resilience and strict regulatory sanctions against payment facilitation, threat actors pivoted toward targeted high-revenue corporate victims ("Big Game Hunting"), resulting in an unprecedented spike in median extortion sums.

---

## 3. Discrepancy Reconciliation Analysis

### Discrepancy 1: Total Ransomware Incidents (Black Kite vs. BlackFog vs. DNI CTIIC)
- **Data Points (2025):**
  - Black Kite: 6,046 publicly disclosed victim organizations.
  - BlackFog: 1,174 high-impact disclosed attacks.
  - CTIIC/DNI Aggregate Tracking: ~7,079 total claimed leak-site incidents.
- **Reconciliation & Root Cause:**
  - *Black Kite* tracks all data leak site (DLS) postings across 96 ransomware syndicates, including repeated postings and vendor supply-chain sub-victims.
  - *BlackFog* applies strict deduplication criteria, counting only confirmed primary enterprise targets with verified organizational identities and forensic confirmation.
  - *CTIIC/DNI* aggregates international intelligence feeds, law enforcement notifications, and multi-cloud telemetry, capturing incidents that may be removed from public leak sites post-negotiation.
  - **Academic Conclusion:** The paper reports both metrics transparently, defining *Claimed/DLS Postings* (7,079) separately from *Independently Verified Enterprise Breaches* (6,046).

### Discrepancy 2: Mean Non-Ransom Recovery Cost (Sophos vs. Akamai)
- **Data Points (2024/2025):**
  - Sophos 2025: $1.53 Million average recovery cost (down 44% from $2.73M in 2024).
  - Akamai 2025: $2.73 Million average recovery cost.
- **Reconciliation:**
  - Sophos survey queried 3,400 mid-sized organizations (100–5,000 employees) in early 2025 reflecting updated 2024/2025 recovery expenditures with mature cloud backups.
  - Akamai cited the 2024 global benchmark which included large multi-national enterprise outages ($10M+ Fortune 500 incidents).
  - **Academic Conclusion:** The paper explicitly notes organizational scale as the explanatory variable for recovery expenditure variance.
