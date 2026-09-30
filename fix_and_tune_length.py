with open("research-paper/paper/main.tex", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Fix TikZ arrow syntax: change stealth' to stealth
text = text.replace(">=stealth'", ">=stealth")

# 2. Fix Table tab:ids_benchmarks
bad_table = r"""\begin{table}[t]
\caption{Empirical Performance Benchmarks ($N=5,000$ Test Set)}
\label{tab:ids_benchmarks}
\centering
\resizebox{\columnwidth}{!}{
\begin{tabular}{l|c|c}
\toprule
\textbf{Evaluation Metric} & \textbf{Random Forest (RF)} & \textbf{Gradient Boosting (GB)} \
\midrule
\textbf{Accuracy}           & \textbf{97.50\%} & 97.32\% \
\textbf{Precision}          & 94.54\%          & \textbf{95.28\%} \
\textbf{Recall (Sensitivity)}& \textbf{84.53\%}& 82.25\% \
\textbf{F1-Score}           & \textbf{0.8925}  & 0.8829  \
\textbf{ROC-AUC}            & \textbf{0.9786}  & 0.9754  \
\textbf{PR-AUC}             & \textbf{0.9386}  & 0.9125  \
\bottomrule
\end{tabular}
}
\end{table}"""

good_table = r"""\begin{table}[t]
\caption{Empirical Performance Benchmarks on $N=5,000$ Held-Out Test Set}
\label{tab:ids_benchmarks}
\centering
\footnotesize
\begin{tabular}{lcc}
\toprule
\textbf{Evaluation Metric} & \textbf{Random Forest (RF)} & \textbf{Gradient Boosting (GB)} \
\midrule
Accuracy                    & \textbf{97.50\%}             & 97.32\% \
Precision                   & 94.54\%                      & \textbf{95.28\%} \
Recall (Sensitivity)        & \textbf{84.53\%}             & 82.25\% \
F1-Score                    & \textbf{0.8925}              & 0.8829 \
ROC-AUC                     & \textbf{0.9786}              & 0.9754 \
PR-AUC                      & \textbf{0.9386}              & 0.9125 \
\bottomrule
\end{tabular}
\end{table}"""

text = text.replace(bad_table, good_table)

# 3. Adjust figure sizing to fit 16 pages cleanly
# Set empirical figures to 0.82\columnwidth
text = text.replace("width=0.88\columnwidth", "width=0.82\columnwidth")
text = text.replace("width=\columnwidth", "width=0.85\columnwidth")

# 4. Streamline redundant appendix sections if needed to target 16 pages
with open("research-paper/paper/main.tex", "w", encoding="utf-8") as f:
    f.write(text)

print("Formatting fixes applied.")
