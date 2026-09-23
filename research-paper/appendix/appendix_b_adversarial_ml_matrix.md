# Appendix B: MITRE ATLAS & NIST Adversarial ML Threat Mapping Matrix

**Project:** Cybersecurity in the Age of Artificial Intelligence  
**Document Reference:** RP-APP-B  
**Standards Corroborated:** MITRE ATLAS v2026.05 | NIST AI 100-2e2025 | OWASP Top 10 for LLMs  

---

### Adversarial AI Tactical Mapping Matrix

| ATLAS Tactic ID | Tactical Objective | Specific AI Attack Technique | NIST AI 100-2 Classification | OWASP LLM Mapping | Documented Real-World Threat / Vulnerability |
|---|---|---|---|---|---|
| **AML.TA0000** | Initial Access | LLM-Assisted Spearphishing & Synthetic Personas | Evasion / Social Engineering | N/A | High-fidelity phishing lures eliminating orthographic markers (ENISA ETL 2025: >80% adoption). |
| **AML.TA0001** | Reconnaissance | Automated AI Model Discovery & Architecture Probing | Privacy / Model Extraction | N/A | Probing model latency and token probabilities to reconstruct hyperparameter topologies. |
| **AML.TA0002** | Resource Development | Acquiring Adversarial LLM Tooling / Jailbreak Datasets | Capability Acquisition | LLM03: Supply Chain | Sourcing uncensored darkweb models (e.g., WormGPT, FraudGPT) and GCG adversarial suffixes. |
| **AML.TA0003** | Execution | Direct & Indirect Prompt Injection (IPI) | Evasion / Control Hijacking | LLM01: Prompt Injection | Injecting malicious Markdown instructions into data feeds to trigger unauthorized tool calls (Greshake et al. 2023). |
| **AML.TA0004** | Persistence | Backdoor & Trojan Weight Implantation | Model Poisoning | LLM04: Model Poisoning | Embedding triggered sub-networks into open-source foundation model checkpoints on public model hubs. |
| **AML.TA0005** | Privilege Escalation | Excessive Agency & Tool Abuse | Autonomous Control Hijacking | LLM06: Excessive Agency | Tricking tool-enabled LLM agents into executing shell commands or modifying file access permissions without human gates. |
| **AML.TA0006** | Defense Evasion | Adversarial Perturbations (FGSM / PGD / Suffixes) | Evasion / Robustness Failure | LLM01: Prompt Injection | Optimizing gradient perturbations on malware binaries to bypass deep-learning-based EDR classification models. |
| **AML.TA0007** | Credential Access | In-Context Secret & Token Extraction | Sensitive Data Extraction | LLM02: Sensitive Info Disclosure | Prompting LLMs to reveal API keys, credentials, or session cookies ingested during RAG context retrieval. |
| **AML.TA0008** | Discovery | Automated Vulnerability & Code Fuzzing | Automated Exploitation | N/A | Machine-speed scanning of open-source repositories to discover zero-day memory bugs (DARPA AIxCC). |
| **AML.TA0009** | Collection | Automated Document Triage & Exfiltration Filtering | Autonomous Data Triage | LLM02: Sensitive Info Disclosure | Using LLMs to parse terabytes of stolen corporate files, tagging high-value IP while discarding system noise. |
| **AML.TA0010** | ML Model Access | Industrial Model Distillation & API Scraping | Model Inversion / IP Theft | N/A | Extracting billions of tokens and hidden Chain-of-Thought reasoning from commercial APIs (CISA Advisory AA26-251A). |
| **AML.TA0011** | Exfiltration | Steganographic LLM Token Exfiltration | Covert Channel Communication | N/A | Embedding exfiltrated data into generated natural language outputs using semantic synonym substitution. |
| **AML.TA0012** | Impact | Data & Training Pipeline Poisoning | Training Data Poisoning | LLM04: Data Poisoning | Injecting subtle bias or corrupted telemetry into SIEM training data to blind defensive anomaly detection models. |
| **AML.TA0013** | Lateral Movement | Multi-Hop Autonomous Agent Pivoting | Autonomous Cyber Operations | LLM06: Excessive Agency | Deploying autonomous LLM agents that navigate internal corporate networks via SSH and living-off-the-land commands. |
