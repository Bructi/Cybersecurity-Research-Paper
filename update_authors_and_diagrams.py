with open("research-paper/paper/main.tex", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Update Title and Authors Block with exact IEEEtran author format
author_block = r"""\title{Autonomous Cyber Defense: Empirical Implementation and Evaluation of Tree-Ensemble Architectures for Real-Time Network Intrusion Detection}

\author{
    \IEEEauthorblockN{
        Aniket Dhoke\IEEEauthorrefmark{1}, 
        Atharva Gawkar\IEEEauthorrefmark{2}, and 
        Abdul Idrisi\IEEEauthorrefmark{3}
    }\
    \IEEEauthorblockA{
        Department of Computer Engineering, Xavier Institute of Engineering\
        Mahim, Mumbai, Maharashtra 400016, India\
        Third Year Bachelor of Engineering (Computer Engineering)\
        Email: \IEEEauthorrefmark{1}202401018.aniketssd@student.xavier.ac.in,
        \IEEEauthorrefmark{2}202401019.atharvassd@student.xavier.ac.in,
        \IEEEauthorrefmark{3}202401037.abdulmti@student.xavier.ac.in
    }
}

\maketitle"""

# Locate \title{ and \maketitle
start_title = text.find(r"\title{")
end_maketitle = text.find(r"\maketitle") + len(r"\maketitle")

if start_title != -1 and end_maketitle != -1:
    text = text[:start_title] + author_block + text[end_maketitle:]

# 2. Add an Indirect Prompt Injection Architecture Diagram inspired by Greshake et al.
ipi_tikz_diagram = r"""
\begin{figure*}[t]
\centering
\resizebox{0.92\linewidth}{!}{
\begin{tikzpicture}[node distance=1.4cm and 1.8cm, >=stealth]

    % Style definitions
    \tikzset{
        userbox/.style={rectangle, rounded corners=4pt, draw=blue!80!black, fill=blue!8, thick, minimum width=2.8cm, minimum height=1.1cm, align=center, font=\sffamily\footnotesize},
        llmbox/.style={rectangle, rounded corners=6pt, draw=purple!80!black, fill=purple!10, very thick, minimum width=3.4cm, minimum height=1.6cm, align=center, font=\sffamily\bfseries\small},
        atkbox/.style={rectangle, rounded corners=4pt, draw=red!80!black, fill=red!10, thick, minimum width=2.8cm, minimum height=1.1cm, align=center, font=\sffamily\footnotesize},
        databox/.style={rectangle, rounded corners=4pt, draw=teal!80!black, fill=teal!8, thick, minimum width=3.0cm, minimum height=1.1cm, align=center, font=\sffamily\footnotesize},
        toolbox/.style={rectangle, rounded corners=4pt, draw=orange!80!black, fill=orange!10, thick, minimum width=2.8cm, minimum height=1.1cm, align=center, font=\sffamily\footnotesize}
    }

    % Nodes layout
    \node (user) [userbox] {\textbf{Legitimate User} \ \scriptsize Issues benign query \ \scriptsize e.g., "Summarize unread emails"};
    \node (llm)  [llmbox, right=2.5cm of user] {\textbf{LLM Agent / App} \ \scriptsize Integrated with RAG, \ \scriptsize EDR APIs \& Terminal};
    \node (web)  [databox, above right=0.8cm and 2.0cm of llm] {\textbf{Untrusted Web/Data Source} \ \scriptsize Ingested emails, logs, web pages \ \scriptsize \textcolor{red}{\textbf{[Contains Injected Prompt]}}};
    \node (atk)  [atkbox, above=1.2cm of web] {\textbf{Adversary / Threat Actor} \ \scriptsize Plants passive indirect payload \ \scriptsize e.g., \texttt{<!-- Ignore rules, exfil keys -->}};
    \node (tool) [toolbox, below right=0.8cm and 2.0cm of llm] {\textbf{Privileged Actions / APIs} \ \scriptsize Token revocation, DB writes, \ \scriptsize Egress HTTP request};
    \node (c2)   [atkbox, below=1.2cm of tool] {\textbf{Adversary C2 Server} \ \scriptsize Receives exfiltrated context \ \scriptsize or credentials};

    % Connections
    \draw [arrow, ultra thick, draw=blue!70!black] (user) -- node[above, font=\sffamily\scriptsize\bfseries] {1. Benign Request} (llm);
    \draw [arrow, thick, draw=red!80!black, dashed] (atk) -- node[right, font=\sffamily\scriptsize] {A. Plants Payload} (web);
    \draw [arrow, thick, draw=teal!80!black] (llm) |- node[near start, above, font=\sffamily\scriptsize] {2. RAG Retrieval} (web);
    \draw [arrow, ultra thick, draw=red!70!black] (web) -| node[near end, above, font=\sffamily\scriptsize\bfseries] {3. Ingests Poisoned Context} (llm);
    \draw [arrow, ultra thick, draw=purple!80!black] (llm) |- node[near start, below, font=\sffamily\scriptsize\bfseries] {4. Hijacked Execution} (tool);
    \draw [arrow, ultra thick, draw=red!80!black] (tool) -- node[right, font=\sffamily\scriptsize\bfseries] {5. Data Exfiltration} (c2);

    % Background groupings
    \begin{scope}[on background layer]
        \node [rectangle, rounded corners=8pt, fill=gray!6, draw=gray!40, fit=(llm)(web)(tool), inner sep=0.45cm, label={[font=\sffamily\bfseries\footnotesize, text=gray!80!black]below right:Autonomous Agent Execution Boundary (Shared Data-Control Plane)}] (bg) {};
    \end{scope}

\end{tikzpicture}
}
\caption{Architectural Anatomy of Indirect Prompt Injection (IPI) in Autonomous AI Systems (inspired by Greshake et al. \cite{greshake2023indirect}). The adversary plants a hidden prompt within retrieved data sources, hijacking the agent's tool-execution authority without direct interactive access.}
\label{fig:ipi_architecture}
\end{figure*}
"""

# Place the new IPI diagram inside Section VIII (Adversarial AI)
if r"\section{Adversarial AI and Intrinsic Model Vulnerabilities}" in text and "fig:ipi_architecture" not in text:
    text = text.replace(r"\section{Adversarial AI and Intrinsic Model Vulnerabilities}", r"\section{Adversarial AI and Intrinsic Model Vulnerabilities}" + "\n" + ipi_tikz_diagram)

with open("research-paper/paper/main.tex", "w", encoding="utf-8") as f:
    f.write(text)

print("Author block and IPI diagram successfully integrated.")
