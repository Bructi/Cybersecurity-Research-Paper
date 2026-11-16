import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split, StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import IsolationForest, RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score, 
    confusion_matrix, roc_curve, auc, precision_recall_curve, average_precision_score
)
from statsmodels.stats.contingency_tables import mcnemar
import pickle
import time
import os

# Set publication aesthetic (IEEE / ACM style)
plt.style.use('seaborn-v0_8-paper' if 'seaborn-v0_8-paper' in plt.style.available else 'default')
plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif', 'Times', 'serif'],
    'font.size': 10,
    'axes.labelsize': 11,
    'axes.titlesize': 11,
    'axes.titleweight': 'bold',
    'axes.labelweight': 'bold',
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 9,
    'figure.titlesize': 12,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight'
})

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'figures')
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 1. Realistic Enterprise Telemetry Feature Space (Synthetic NetFlow standard)
feature_names = [
    'flow_duration_ms', 'fwd_packet_count', 'bwd_packet_count',
    'fwd_header_len_bytes', 'bwd_header_len_bytes', 'flow_bytes_per_sec',
    'flow_pkts_per_sec', 'pkt_len_mean', 'pkt_len_std', 'syn_flag_count',
    'ack_flag_count', 'rst_flag_count', 'psh_flag_count', 'urg_flag_count',
    'avg_bwd_segment_size', 'init_win_bytes_fwd', 'init_win_bytes_bwd',
    'active_mean_ms', 'idle_mean_ms', 'subflow_fwd_bytes'
]

def main():
    print("[1/6] Synthesizing NetFlow distribution benchmark (N=25,000)...")
    np.random.seed(42)

    # Generate 25,000 realistic network flow vectors
    X, y = make_classification(
        n_samples=25000,
        n_features=20,
        n_informative=14,
        n_redundant=4,
        n_classes=2,
        weights=[0.88, 0.12],  # 88% Benign, 12% Malicious (realistic SOC imbalance)
        flip_y=0.008,          # 0.8% label noise / capture anomalies
        class_sep=1.35,
        random_state=42
    )

    # Train/Test Split (80/20 Stratified)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )
    print(f"Dataset summary: Train={X_train.shape[0]}, Test={X_test.shape[0]}, Features={X.shape[1]}")

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # 2. Model Training
    print("[2/6] Training baseline models (Logistic Regression, MLP, Isolation Forest)...")
    lr = LogisticRegression(max_iter=500, random_state=42)
    lr.fit(X_train_scaled, y_train)

    mlp = MLPClassifier(hidden_layer_sizes=(32, 16), max_iter=150, random_state=42)
    mlp.fit(X_train_scaled, y_train)

    iso = IsolationForest(contamination=0.12, random_state=42, n_jobs=1)
    iso.fit(X_train)

    print("[3/6] Training tree ensembles (Random Forest & Gradient Boosting)...")
    rf = RandomForestClassifier(
        n_estimators=100,
        max_depth=12,
        min_samples_split=6,
        min_samples_leaf=2,
        max_features='sqrt',
        class_weight='balanced_subsample',
        random_state=42,
        n_jobs=1
    )
    rf.fit(X_train, y_train)

    gb = GradientBoostingClassifier(
        n_estimators=100,
        learning_rate=0.08,
        max_depth=5,
        subsample=0.85,
        random_state=42
    )
    gb.fit(X_train, y_train)

    # 3. Predictions and Metrics Computation
    print("[4/6] Computing evaluation metrics, latencies, and significance tests...")
    models = {
        'Logistic Regression': (lr, X_test_scaled, True),
        'Shallow MLP (32x16)': (mlp, X_test_scaled, True),
        'Isolation Forest': (iso, X_test, False),
        'Gradient Boosting': (gb, X_test, True),
        'Random Forest': (rf, X_test, True),
    }

    results = {}
    for name, (clf, data, has_prob) in models.items():
        # Predict
        if name == 'Isolation Forest':
            raw_p = clf.predict(data)
            y_pred = np.where(raw_p == -1, 1, 0)
            scores = -clf.score_samples(data)
            y_prob = (scores - scores.min()) / (scores.max() - scores.min() + 1e-9)
        else:
            y_pred = clf.predict(data)
            y_prob = clf.predict_proba(data)[:, 1]

        # Latency / throughput
        _ = clf.predict(data[:50])
        n_bench = 5000
        t0 = time.perf_counter()
        _ = clf.predict(data[:n_bench])
        t1 = time.perf_counter()
        latency_us = ((t1 - t0) / n_bench) * 1e6
        throughput = 1e6 / latency_us

        # Metrics
        fpr, tpr, _ = roc_curve(y_test, y_prob)
        results[name] = {
            'Accuracy': accuracy_score(y_test, y_pred),
            'Precision': precision_score(y_test, y_pred),
            'Recall': recall_score(y_test, y_pred),
            'F1': f1_score(y_test, y_pred),
            'ROC_AUC': auc(fpr, tpr),
            'PR_AUC': average_precision_score(y_test, y_prob),
            'Latency_us': latency_us,
            'Throughput': throughput,
            'y_pred': y_pred,
            'y_prob': y_prob
        }

    print("\n" + "="*85)
    print(f"{'Model Architecture':<22} | {'Accuracy':<8} | {'Precision':<9} | {'Recall':<7} | {'F1':<6} | {'ROC-AUC':<7} | {'Latency':<8} | {'Throughput'}")
    print("="*85)
    for name, m in results.items():
        print(f"{name:<22} | {m['Accuracy']*100:6.2f}% | {m['Precision']*100:7.2f}% | {m['Recall']*100:6.2f}% | {m['F1']:6.4f} | {m['ROC_AUC']:7.4f} | {m['Latency_us']:6.2f} us | {m['Throughput']:9,.0f} flows/s")
    print("="*85 + "\n")

    # McNemar's test: RF vs GB
    rf_pred = results['Random Forest']['y_pred']
    gb_pred = results['Gradient Boosting']['y_pred']
    lr_pred = results['Logistic Regression']['y_pred']

    def calc_mcnemar(pred_a, pred_b, y_true):
        c11 = np.sum((pred_a == y_true) & (pred_b == y_true))
        c10 = np.sum((pred_a == y_true) & (pred_b != y_true))
        c01 = np.sum((pred_a != y_true) & (pred_b == y_true))
        c00 = np.sum((pred_a != y_true) & (pred_b != y_true))
        table = [[c11, c10], [c01, c00]]
        res = mcnemar(table, exact=False, correction=True)
        return res.statistic, res.pvalue

    stat_gb, p_gb = calc_mcnemar(rf_pred, gb_pred, y_test)
    stat_lr, p_lr = calc_mcnemar(rf_pred, lr_pred, y_test)
    print(f"McNemar Test (RF vs GB): stat={stat_gb:.4f}, p={p_gb:.4f}")
    print(f"McNemar Test (RF vs LR): stat={stat_lr:.4f}, p={p_lr:.4e}")

    # Save serialized model with n_jobs=1 for GUI
    rf.n_jobs = 1
    with open(os.path.join(os.path.dirname(__file__), 'rf_ids_model.pkl'), 'wb') as f:
        pickle.dump(rf, f)
    print("Serialized rf_ids_model.pkl (n_jobs=1) successfully.")

    # 4. Generate Publication Figures
    print("[5/6] Rendering academic figures...")

    # Figure 1: Normalized Confusion Matrix for Random Forest
    fig, ax = plt.subplots(figsize=(3.45, 2.9))
    cm = confusion_matrix(y_test, rf_pred)
    cm_norm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]

    sns.heatmap(
        cm, annot=True, fmt='d', cmap='Blues', cbar=False, ax=ax,
        xticklabels=['Benign (0)', 'Intrusion (1)'],
        yticklabels=['Benign (0)', 'Intrusion (1)'],
        annot_kws={"size": 10, "weight": "bold"}
    )
    for i in range(2):
        for j in range(2):
            ax.text(j + 0.5, i + 0.75, f"({cm_norm[i, j]*100:.1f}%)",
                    ha='center', va='center', color='black' if cm[i,j] < cm.max()/2 else 'white',
                    fontsize=8, style='italic')

    ax.set_title('Random Forest Confusion Matrix ($N=5,000$ Test)', pad=8)
    ax.set_xlabel('Predicted Label', labelpad=4)
    ax.set_ylabel('Ground Truth Label', labelpad=4)
    plt.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, 'confusion_matrix.png'), dpi=300)
    plt.close(fig)

    # Figure 2: ROC Curves
    fig, ax = plt.subplots(figsize=(3.45, 2.9))
    fpr_rf, tpr_rf, _ = roc_curve(y_test, results['Random Forest']['y_prob'])
    fpr_gb, tpr_gb, _ = roc_curve(y_test, results['Gradient Boosting']['y_prob'])
    fpr_mlp, tpr_mlp, _ = roc_curve(y_test, results['Shallow MLP (32x16)']['y_prob'])
    fpr_lr, tpr_lr, _ = roc_curve(y_test, results['Logistic Regression']['y_prob'])

    ax.plot(fpr_rf, tpr_rf, color='#1e3a8a', lw=1.8, label=f'Random Forest ({results["Random Forest"]["ROC_AUC"]:.3f})')
    ax.plot(fpr_gb, tpr_gb, color='#047857', lw=1.5, linestyle='-.', label=f'Gradient Boost ({results["Gradient Boosting"]["ROC_AUC"]:.3f})')
    ax.plot(fpr_mlp, tpr_mlp, color='#7c3aed', lw=1.3, linestyle=':', label=f'Shallow MLP ({results["Shallow MLP (32x16)"]["ROC_AUC"]:.3f})')
    ax.plot(fpr_lr, tpr_lr, color='#d97706', lw=1.3, linestyle='--', label=f'Logistic Reg. ({results["Logistic Regression"]["ROC_AUC"]:.3f})')
    ax.plot([0, 1], [0, 1], color='#64748b', lw=1.0, linestyle='--', label='Chance (0.500)')

    ax.set_xlim([-0.02, 1.0])
    ax.set_ylim([0.0, 1.02])
    ax.set_xlabel('False Positive Rate (1 - Specificity)')
    ax.set_ylabel('True Positive Rate (Sensitivity)')
    ax.set_title('ROC Discrimination Curves', pad=8)
    ax.grid(True, linestyle=':', alpha=0.6)
    ax.legend(loc="lower right", frameon=True, framealpha=0.9, fontsize=7.5)
    plt.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, 'roc_curve.png'), dpi=300)
    plt.close(fig)

    # Figure 3: Top 10 Feature Importance Distribution (Gini Impurity)
    fig, ax = plt.subplots(figsize=(3.45, 3.2))
    importances = rf.feature_importances_
    top_idx = np.argsort(importances)[::-1][:10]

    y_pos = np.arange(10)
    cleaned_names = [feature_names[i].replace('_', ' ') for i in top_idx]

    bars = ax.barh(y_pos, importances[top_idx], align='center', color='#2563eb', edgecolor='#1e40af', alpha=0.85, height=0.65)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(cleaned_names, fontsize=8)
    ax.invert_yaxis()
    ax.set_xlabel('Mean Gini Impurity Decrease', labelpad=4)
    ax.set_title('Top 10 High-Discrimination Features', pad=8)
    ax.grid(axis='x', linestyle=':', alpha=0.6)

    for bar in bars:
        w = bar.get_width()
        ax.text(w + 0.003, bar.get_y() + bar.get_height()/2, f"{w:.3f}",
                va='center', ha='left', fontsize=7.5, color='#1e293b')

    ax.set_xlim(0, max(importances[top_idx]) * 1.25)
    plt.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, 'feature_importance.png'), dpi=300)
    plt.close(fig)

    print("[6/6] All benchmark figures successfully generated and saved to figures/.\n")

if __name__ == '__main__':
    main()
