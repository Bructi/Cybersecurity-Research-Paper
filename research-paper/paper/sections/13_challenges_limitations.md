# 13. Technical Challenges and Systemic Limitations

Despite substantial advances in defensive machine learning and automated cybersecurity tooling, operational deployment faces profound technical bottlenecks, mathematical vulnerabilities, and organizational limitations [8], [10], [18]. Recognizing these constraints is essential to prevent dangerous over-reliance on autonomous security systems.

---

### 13.1 Non-Deterministic Reasoning and Model Hallucinations
Large Language Models and deep neural networks are probabilistic statistical token predictors rather than deterministic logic engines [8], [15].
- **Hallucinated Threat Indicators:** In automated threat intelligence synthesis, LLMs frequently hallucinate CVE numbers, misattribute threat actor group names, or invent non-existent IP addresses and malicious domains [9], [14].
- **Destructive Triage Actions:** If an unconstrained agentic SOAR system hallucinates an intrusion in a core Active Directory domain controller or database cluster, automated remediation playbooks can mistakenly sever critical enterprise infrastructure, inducing self-inflicted denial-of-service conditions [5], [9].

---

### 13.2 "Black-Box" Interpretability and Explainable AI (XAI) Bottlenecks
Deep neural networks and Graph Neural Networks operate across multi-thousand-dimensional latent embedding spaces containing hundreds of millions to billions of learned parameters [10], [19].
- **Lack of Causal Auditability:** When an autoencoder flags an anomalous network flow with a high reconstruction loss $\mathcal{A}(x)$, it does not natively provide a human-readable causal explanation for why the packet was deemed malicious [19].
- **Regulatory and Legal Compliance Gaps:** Under the EU AI Act (Article 13) and NIS2 directive, critical infrastructure operators must be capable of providing transparent explanations for automated risk decisions [3]. Post-hoc interpretability techniques (such as SHAP values, Integrated Gradients, or attention heatmaps) provide approximations of feature importance but are computationally expensive and can themselves be manipulated by adversarial perturbations [10], [21].

---

### 13.3 Adversarial Fragility and Concept Drift
Defensive machine learning models are fundamentally susceptible to adversarial evasion and environmental concept drift [10], [21].
- **Adversarial Noise Vulnerability:** As established by Szegedy et al. and Goodfellow et al., minute, imperceptible gradient perturbations added to input features can cause high-confidence classification inversion [21], [22].
- **Temporal Concept Drift:** Enterprise IT environments are non-stationary: software stacks update, user habits shift, and network topologies evolve continuously. A behavioral anomaly baseline trained on historical telemetry degrades rapidly over time, leading to rising false-positive rates unless continuously retrained on fresh, validated ground-truth data [10], [19].

---

### 13.4 Compute Asymmetry and Environmental Economics
Operating state-of-the-art defensive AI models imposes massive capital and energy overhead [8], [9].
- **Inference Latency vs. Throughput:** Running deep transformer inspection models over high-speed 100 Gbps network backbones creates severe computational bottlenecks, requiring multi-million-dollar GPU cluster deployments and specialized edge accelerators [9], [19].
- **Asymmetric Economics:** While an attacker requires only minimal compute to execute a single successful jailbroken prompt or phishing generation script, defenders must evaluate every packet, email, and process execution across millions of enterprise endpoints 24/7/365, imposing an overwhelming economic advantage on offensive actors [8], [9].

---

### 13.5 Data Provenance and Training Set Poisoning
Defensive AI systems are only as resilient as the data pipelines used to train and calibrate them [10], [12].
- **Supply-Chain Insecurity:** Threat actors who successfully poison open-source vulnerability databases (e.g., NVD, GitHub advisories) or security forum threads can degrade the detection capabilities of all downstream models fine-tuned on those datasets [8], [12].
- **Scarcity of Ground-Truth Malicious Telemetry:** Real-world enterprise breach datasets containing full packet captures, process memory dumps, and command-and-control logs are heavily restricted due to privacy, intellectual property, and liability concerns. Consequently, researchers frequently rely on synthetic or outdated benchmark datasets (e.g., DARPA 1999, NSL-KDD, CIC-IDS2017) that fail to reflect modern cloud-native threat environments [10], [19].
