# Appendix A: Mathematical Formulations of Adversarial AI and Defensive Machine Learning

**Project:** Cybersecurity in the Age of Artificial Intelligence  
**Document Reference:** RP-APP-A  
**Auditor:** Cyber-AI Research Consortium  

---

## 1. Adversarial Evasion and Perturbation Formulations

### 1.1 Fast Gradient Sign Method (FGSM)
Goodfellow et al. (2015) established that neural network vulnerability to adversarial perturbation arises primarily from linear behavior in high-dimensional spaces. Given an input sample $x \in \mathbb{R}^d$, true label $y$, loss function $J(\theta, x, y)$, and perturbation budget $\epsilon$, the adversarial perturbation $\delta$ is computed as:

$$\delta = \epsilon \cdot \text{sign}\left(\nabla_x J(\theta, x, y)\right)$$

The perturbed adversarial sample $x_{\text{adv}}$ is defined as:

$$x_{\text{adv}} = x + \delta = x + \epsilon \cdot \text{sign}\left(\nabla_x J(\theta, x, y)\right)$$

Subject to the $L_\infty$ norm constraint: $\|x_{\text{adv}} - x\|_\infty \le \epsilon$.

---

### 1.2 Projected Gradient Descent (PGD)
Madry et al. (2018) formalized adversarial robustness as a saddle-point (min-max) optimization problem. The multi-step Projected Gradient Descent adversary computes iterative updates:

$$x^{(t+1)} = \Pi_{x + \mathcal{S}} \left( x^{(t)} + \alpha \cdot \text{sign}\left(\nabla_x J(\theta, x^{(t)}, y)\right) \right)$$

where:
- $\Pi_{x + \mathcal{S}}$ denotes the projection operator onto the allowable perturbation ball $\mathcal{S} = \{ \delta : \|\delta\|_p \le \epsilon \}$,
- $\alpha$ is the step size ($\alpha < \epsilon$),
- $t \in \{0, 1, \dots, T-1\}$ represents the optimization iteration step.

Robust training minimizes the empirical adversarial risk:

$$\min_\theta \mathbb{E}_{(x, y) \sim \mathcal{D}} \left[ \max_{\delta \in \mathcal{S}} J(\theta, x + \delta, y) \right]$$

---

### 1.3 Greedy Coordinate Gradient (GCG) for Discrete LLM Token Optimization
Zou et al. (2023) generalized gradient-based adversarial optimization to discrete token sequences in Large Language Models. Let $x_{1:n}$ represent a prompt token sequence, and $p(x_{n+1:n+H} | x_{1:n})$ denote the probability of generating target affirmative tokens (e.g., "Sure, here is how to...").

The objective is to find an adversarial suffix $p_{1:k}$ that minimizes the negative log-likelihood of target response tokens $y_{1:H}$:

$$\mathcal{L}(p_{1:k}) = -\sum_{j=1}^H \log P\left(y_j \mid x_{1:n}, p_{1:k}, y_{1:j-1}\right)$$

For each position $i \in \{1, \dots, k\}$ in the adversarial suffix, the linearized gradient with respect to the one-hot token embedding $e_{p_i}$ is computed:

$$\nabla_{e_{p_i}} \mathcal{L}(p_{1:k})$$

The top-$K$ candidate replacement tokens with the largest negative gradients are selected:

$$\mathcal{C}_i = \text{Top-}K \left( -\nabla_{e_{p_i}} \mathcal{L}(p_{1:k}) \right)$$

Subsets of candidate tokens are evaluated in parallel batches, greedily selecting the discrete replacement token that yields the maximal reduction in the loss function $\mathcal{L}$.

---

## 2. Defensive Anomaly Detection & Telemetry Scoring

### 2.1 Deep Autoencoder Reconstruction Error
In enterprise telemetry anomaly detection, deep autoencoders map high-dimensional audit logs $x \in \mathbb{R}^d$ through an encoder $f_\phi: \mathbb{R}^d \to \mathbb{R}^k$ ($k \ll d$) to a latent bottleneck $z$, and reconstruct the input via decoder $g_\psi: \mathbb{R}^k \to \mathbb{R}^d$:

$$\hat{x} = g_\psi(f_\phi(x))$$

The anomaly score $\mathcal{A}(x)$ is computed as the Euclidean or Mahalanobis reconstruction loss:

$$\mathcal{A}(x) = \|x - \hat{x}\|_2^2 = \sum_{i=1}^d (x_i - \hat{x}_i)^2$$

An alert is triggered when $\mathcal{A}(x) > \tau$, where the threshold $\tau = \mu_{\text{train}} + k \cdot \sigma_{\text{train}}$ is calibrated to bound false positive rates under baseline traffic.

---

### 2.2 Isolation Forest Anomaly Scoring
Isolation Forest isolates anomalies by recursively partitioning feature space using random hyperplanes. The anomaly score $s(x, n)$ for an instance $x$ across an ensemble of $n$ isolation trees is formulated as:

$$s(x, n) = 2^{-\frac{\mathbb{E}(h(x))}{c(n)}}$$

where:
- $h(x)$ is the path length (number of splits required to isolate sample $x$),
- $\mathbb{E}(h(x))$ is the expected path length over all trees in the forest,
- $c(n)$ is the average path length of unsuccessful searches in a Binary Search Tree (BST), defined analytically as:

$$c(n) = 2 \ln(n - 1) + 0.5772156649 \text{ (Euler-Mascheroni constant)} - \frac{2(n - 1)}{n}$$

- When $\mathbb{E}(h(x)) \to 0 \implies s \to 1$ (high anomaly confidence; instance is isolated near tree root).
- When $\mathbb{E}(h(x)) \to c(n) \implies s \to 0.5$ (structural normality).
- When $\mathbb{E}(h(x)) \to n - 1 \implies s \to 0$ (centralized cluster).

---

### 2.3 Graph Neural Network Node Classification on Provenance Graphs
Heterogeneous Graph Neural Networks (Jiang et al., 2025) represent enterprise host events as a directed acyclic graph $G = (\mathcal{V}, \mathcal{E}, \mathcal{T}_v, \mathcal{T}_e)$, where nodes $v \in \mathcal{V}$ denote processes, sockets, or files, and edges $e \in \mathcal{E}$ denote system operations (`fork`, `read`, `connect`).

The node embedding update at layer $l+1$ for target node $v$ of type $\tau \in \mathcal{T}_v$ aggregates neighboring messages across edge relation types $r \in \mathcal{T}_e$:

$$h_v^{(l+1)} = \sigma \left( W_\tau \cdot h_v^{(l)} + \sum_{r \in \mathcal{T}_e} \sum_{u \in \mathcal{N}_r(v)} \alpha_{uv}^r \cdot W_r \cdot h_u^{(l)} \right)$$

where:
- $\mathcal{N}_r(v)$ denotes neighbors of node $v$ under relation $r$,
- $\alpha_{uv}^r$ represents the attention weight parameterized by relational similarity,
- $W_\tau, W_r$ are learnable projection matrices,
- $\sigma(\cdot)$ is a non-linear activation function (e.g., LeakyReLU).

---

## 3. Game-Theoretic Co-Evolutionary Dynamics

The dynamic interaction between an adversarial AI agent and an AI-augmented defensive system is modeled as a two-player, zero-sum Partially Observable Stochastic Game (POSG):

$$\mathcal{M} = \langle \mathcal{S}, \mathcal{A}_{\text{att}}, \mathcal{A}_{\text{def}}, \mathcal{T}, \mathcal{R}_{\text{att}}, \mathcal{R}_{\text{def}}, \Omega_{\text{att}}, \Omega_{\text{def}}, \mathcal{O}_{\text{att}}, \mathcal{O}_{\text{def}}, \gamma \rangle$$

- **State Space $\mathcal{S}$:** Global enterprise network configuration, credential states, and compromise topology.
- **Action Spaces:** $\mathcal{A}_{\text{att}}$ (exploits, obfuscation, lateral pivots); $\mathcal{A}_{\text{def}}$ (microsegmentation, telemetry rate limits, honeytokens).
- **Payoff Matrix:** $\mathcal{R}_{\text{def}} = -\mathcal{R}_{\text{att}}$, reflecting asset compromise vs. operational availability preservation.

The minimax value of the cyber conflict at equilibrium satisfies the Bellman optimality condition:

$$V^*(s) = \max_{\pi_{\text{att}}} \min_{\pi_{\text{def}}} \sum_{a_{\text{att}}, a_{\text{def}}} \pi_{\text{att}}(a_{\text{att}}|s) \pi_{\text{def}}(a_{\text{def}}|s) \left[ \mathcal{R}(s, a_{\text{att}}, a_{\text{def}}) + \gamma \sum_{s'} \mathcal{T}(s'|s, a_{\text{att}}, a_{\text{def}}) V^*(s') \right]$$

This formulation demonstrates mathematically that when an adversary reduces action latency ($\Delta t_{\text{att}} \to 0$ via AI automation), the defender must achieve parity ($\Delta t_{\text{def}} \le \Delta t_{\text{att}}$) to prevent the state value $V^*(s)$ from monotonically transitioning into an unrecoverable compromise state.
