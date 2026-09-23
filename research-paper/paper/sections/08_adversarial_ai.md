# 8. Adversarial AI and AI-Specific Security Risks

Integrating machine learning algorithms and foundation Large Language Models into enterprise software stacks establishes an entirely new, highly complex attack surface [8], [10], [12]. Unlike deterministic software systems whose vulnerabilities stem from memory errors or logic bugs (e.g., buffer overflows, SQL injections), AI systems suffer from **intrinsic mathematical, statistical, and semantic vulnerabilities** inherent to high-dimensional optimization and neural architecture design [10], [12], [21].

As categorized in **Diagram C** (*AI Cybersecurity Threat Taxonomy*) and mapped against **MITRE ATLAS** and **NIST AI 100-2e2025** (see Appendix B), adversarial AI risks span three critical operational domains:

---

### 8.1 Adversarial Evasion & Gradient Perturbations
Adversarial evasion attacks occur at inference time, where an adversary crafts subtle, often human-imperceptible perturbations to input data that cause a trained neural network to make confident classification errors [10], [21], [22].
- **Gradient Optimization (FGSM & PGD):** By calculating the gradient of the model's loss function with respect to the input vector ($\nabla_x J(\theta, x, y)$), an adversary projects optimal mathematical noise within an $L_\infty$ or $L_2$ perturbation budget $\epsilon$ [22], [23]. In cybersecurity contexts, adversaries apply adversarial perturbations to Portable Executable (PE) binary headers, PDF documents, or network flow packet distributions to successfully blind deep-learning-based malware and intrusion detection systems without breaking binary executable functionality [10], [21].
- **Universal Jailbreak Suffixes (GCG):** In generative language models, Zou et al. (2023) proved that discrete token optimization (Greedy Coordinate Gradient) can construct universal token suffixes that force aligned foundation models to bypass safety guardrails and output prohibited exploit instructions, transferring successfully across diverse model architectures [16].

---

### 8.2 Direct and Indirect Prompt Injection Attacks
Prompt injection represents the quintessential security boundary failure of Large Language Model architectures [8], [15], [18].
- **Structural Conflation of Control and Data Planes:** In classical computing, the Von Neumann architecture separates code (instructions) from data in memory. Transformer-based LLMs, however, process system instructions (e.g., Developer system prompts) and untrusted user/external inputs as a single, concatenated sequence of tokens [15], [18].
- **Indirect Prompt Injection (IPI):** As formalized by Greshake et al. (2023), when an LLM agent is granted access to tools (web browsing, email reading, database querying), an adversary can embed malicious natural language control strings into public web pages, document attachments, or database records [15]. When the agent ingests this untrusted content, the hidden prompt overrides the original system instructions, commandeering the agent to execute unauthorized tool calls, delete data, or exfiltrate private session context to adversary-controlled servers [15], [18].
- **Defensive Mitigation Limitations:** Heuristic prompt filtering and guardrail fine-tuning offer only partial, non-deterministic protection. Robust mitigation requires architectural privilege separation, dual-LLM execution pipelines, and cryptographic context boundary tagging (Hines et al. 2024; Xiang et al. 2026) [18], [20].

---

### 8.3 Data Poisoning & Training Pipeline Compromise
Poisoning attacks target the integrity of machine learning models during the pre-training, fine-tuning, or retrieval-augmented generation (RAG) ingestion phases [8], [10], [12].
- **Training Data Poisoning:** By injecting a small fraction (e.g., <0.1%) of maliciously labeled or crafted samples into open-source web-scraped training datasets, an adversary can manipulate the decision boundary of a defensive classifier [10], [21].
- **Backdoors and Neural Trojans:** Adversaries embed latent triggers (e.g., a specific benign string in a network packet or a specific visual watermark) into training data. The poisoned model performs with high baseline accuracy on normal validation tests, but predictably classifies malicious inputs as benign whenever the secret trigger is present, effectively disabling intrusion detection during active attacks [10], [12].
- **RAG Knowledge Base Poisoning (Slopsquatting):** Adversaries publish malicious documentation on public repositories or Wikipedia. When enterprise RAG pipelines automatically ingest this data into vector embeddings, the retrieval mechanism serves poisoned instructions to internal corporate agents [8], [15].

---

### 8.4 Model Inversion, Training Extraction, and Privacy Leaks
Machine learning models inherently memorize statistical properties of their training distributions [10], [17].
- **Training Data Extraction:** Carlini et al. (2021) demonstrated that targeted querying of foundation models can extract verbatim sequences of sensitive training data, including Personally Identifiable Information (PII), proprietary source code, cryptographic keys, and medical records [17].
- **Membership Inference Attacks (MIA):** By analyzing output prediction confidence scores and loss differentials, an attacker can determine with high statistical significance whether a specific record was included in the proprietary training set, violating regulatory privacy mandates (e.g., GDPR, HIPAA) [10], [17].

---

### 8.5 Model Extraction & Industrial-Scale Distillation
As foundation models become primary commercial assets requiring hundreds of millions of dollars in compute, model extraction and intellectual property theft have emerged as prominent state-sponsored threats [4], [17].
- **API Scraping & Reverse Engineering:** By programmatically querying a target model API with millions of diverse prompts and capturing the generated responses, an adversary can train a student model that matches the capability of the proprietary teacher model at a tiny fraction of the cost [4], [17].
- **CISA Advisory AA26-251A Case:** As documented in Joint Cybersecurity Advisory AA26-251A (Sept. 2026), state-nexus entities systematically extracted over 14 billion tokens and hidden multi-step reasoning traces (Chain-of-Thought) from Western commercial APIs, leveraging residential proxy networks to evade rate limits and incorporating the stolen reasoning logic into domestic cyber warfare models [4].

---

### 8.6 Excessive Agency & Autonomous Tool Abuse
When LLMs are deployed as autonomous agents with direct execution privileges (such as modifying databases, executing shell commands, or managing cloud infrastructure), any failure in reasoning or security boundary validation can lead to catastrophic operational failure [5], [8], [18].
- **Unconstrained Tool Calling:** An agent tricked via prompt injection or reasoning hallucination can execute destructive commands (e.g., `rm -rf /` or dropping customer production tables) without human validation [5], [18].
- **Five Eyes Directives:** In May 2026, CISA and Five Eyes cyber agencies issued binding guidance mandating strict least-privilege scoping, sandbox isolation, and mandatory Human-in-the-Loop (HITL) gates for all agentic AI services deployed across enterprise and government infrastructure [5].
