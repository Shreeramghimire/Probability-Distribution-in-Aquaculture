import numpy as np
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    fbeta_score, matthews_corrcoef, roc_auc_score,
    average_precision_score, log_loss, brier_score_loss,
    cohen_kappa_score, confusion_matrix, classification_report
)

# Example: Salmon disease detection
y_true = np.array([1, 0, 1, 1, 0, 1, 0, 0, 1, 0])  # 1 = diseased
y_pred = np.array([1, 0, 1, 0, 0, 1, 0, 1, 1, 0])  # Binary predictions
y_proba = np.array([0.9, 0.1, 0.8, 0.4, 0.2, 0.95, 0.15, 0.55, 0.85, 0.05])

# Core metrics
print("Confusion Matrix:\n", confusion_matrix(y_true, y_pred))
print(f"Accuracy: {accuracy_score(y_true, y_pred):.3f}")
print(f"Precision: {precision_score(y_true, y_pred):.3f}")
print(f"Recall: {recall_score(y_true, y_pred):.3f}")
print(f"Specificity: {recall_score(y_true, y_pred, pos_label=0):.3f}")
print(f"F1-Score: {f1_score(y_true, y_pred):.3f}")
print(f"F2-Score: {fbeta_score(y_true, y_pred, beta=2):.3f}")
print(f"MCC: {matthews_corrcoef(y_true, y_pred):.3f}")
print(f"Cohen's Kappa: {cohen_kappa_score(y_true, y_pred):.3f}")

# Threshold-agnostic
print(f"ROC-AUC: {roc_auc_score(y_true, y_proba):.3f}")
print(f"PR-AUC: {average_precision_score(y_true, y_proba):.3f}")
print(f"Log-Loss: {log_loss(y_true, y_proba):.3f}")
print(f"Brier Score: {brier_score_loss(y_true, y_proba):.3f}")

# Complete summary
print("\nClassification Report:\n", classification_report(y_true, y_pred))

# Custom Salmon Metric Function
def salmon_health_metrics(y_true, y_pred, y_proba):
    from sklearn.metrics import (
        accuracy_score, precision_score, recall_score, f1_score,
        fbeta_score, matthews_corrcoef, roc_auc_score,
        average_precision_score, log_loss, brier_score_loss,
        cohen_kappa_score
    )
    
    metrics = {
        'Accuracy': accuracy_score(y_true, y_pred),
        'Precision': precision_score(y_true, y_pred),
        'Recall (Sensitivity)': recall_score(y_true, y_pred),
        'Specificity': recall_score(y_true, y_pred, pos_label=0),
        'F1-Score': f1_score(y_true, y_pred),
        'F2-Score (Recall-focused)': fbeta_score(y_true, y_pred, beta=2),
        'F0.5-Score (Precision-focused)': fbeta_score(y_true, y_pred, beta=0.5),
        'MCC': matthews_corrcoef(y_true, y_pred),
        "Cohen's Kappa": cohen_kappa_score(y_true, y_pred),
        'ROC-AUC': roc_auc_score(y_true, y_proba),
        'PR-AUC': average_precision_score(y_true, y_proba),
        'Log-Loss': log_loss(y_true, y_proba),
        'Brier Score': brier_score_loss(y_true, y_proba),
    }
    
    return metrics

# Usage
results = salmon_health_metrics(y_true, y_pred, y_proba)
for metric, value in results.items():
    print(f"{metric}: {value:.3f}")

#
