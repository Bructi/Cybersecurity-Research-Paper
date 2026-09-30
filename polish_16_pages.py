with open("research-paper/paper/main.tex", "r", encoding="utf-8") as f:
    tex = f.read()

# Replace variables with escaped underscores
replacements = {
    "flow_duration_ms": r"flow\_duration\_ms",
    "fwd_packet_count": r"fwd\_packet\_count",
    "bwd_packet_count": r"bwd\_packet\_count",
    "flow_bytes_per_sec": r"flow\_bytes\_per\_sec",
    "flow_pkts_per_sec": r"flow\_pkts\_per\_sec",
    "syn_flag_count": r"syn\_flag\_count",
    "ack_flag_count": r"ack\_flag\_count",
    "rst_flag_count": r"rst\_flag\_count",
    "psh_flag_count": r"psh\_flag\_count",
    "urg_flag_count": r"urg\_flag\_count",
    "pkt_len_mean": r"pkt\_len\_mean",
    "pkt_len_std": r"pkt\_len\_std",
    "avg_bwd_segment_size": r"avg\_bwd\_segment\_size",
    "init_win_bytes_fwd": r"init\_win\_bytes\_fwd",
    "init_win_bytes_bwd": r"init\_win\_bytes\_bwd",
}

for k, v in replacements.items():
    tex = tex.replace(f"\text{{{k}}}", f"\text{{{v}}}")

# Fix table tab:ids_benchmarks cleanly
clean_table = r"""\begin{table}[t]
\caption{Empirical ML Performance Benchmarks ($N=5,000$ Held-Out Test Set)}
\label{tab:ids_benchmarks}
\centering
\small
\begin{tabular}{lcc}
\hline\noalign{\smallskip}
\textbf{Evaluation Metric} & \textbf{Random Forest} & \textbf{Gradient Boosting} \
\noalign{\smallskip}\hline\noalign{\smallskip}
Accuracy                    & \textbf{97.50\%}       & 97.32\% \
Precision                   & 94.54\%                & \textbf{95.28\%} \
Recall (Sensitivity)        & \textbf{84.53\%}       & 82.25\% \
F1-Score                    & \textbf{0.8925}        & 0.8829 \
ROC-AUC                     & \textbf{0.9786}        & 0.9754 \
PR-AUC                      & \textbf{0.9386}        & 0.9125 \
\noalign{\smallskip}\hline
\end{tabular}
\end{table}"""

# Find and replace table
start_marker = r"\begin{table}[t]"
end_marker = r"\end{table}"
if "tab:ids_benchmarks" in tex:
    pos = tex.find("tab:ids_benchmarks")
    tbl_start = tex.rfind(r"\begin{table}", 0, pos)
    tbl_end = tex.find(r"\end{table}", pos) + len(r"\end{table}")
    tex = tex[:tbl_start] + clean_table + tex[tbl_end:]

with open("research-paper/paper/main.tex", "w", encoding="utf-8") as f:
    f.write(tex)

print("Polish completed.")
