**Classification metrics** are quantitative measures used to evaluate the performance of machine learning models that predict categorical outcomes. They answer critical questions like: *"How accurate is my model?"*, *"What types of mistakes does it make?"*, and *"Can I trust its predictions in production?"*

While accuracy is the most intuitive metric, it often tells an incomplete story—especially when dealing with **imbalanced datasets** or when **different types of errors have vastly different consequences**.

**The Core Principle:** *No single metric captures everything. Understanding the trade-offs is the key to building trustworthy models.*

**Why Classification Metrics Matter in Aquaculture:**

Aquaculture, particularly **Atlantic salmon farming**, generates massive amounts of data from:
- **Sensors** (oxygen, temperature, pH, salinity)
- **Video feeds** (fish counting, behavior analysis)
- **Health records** (disease outbreaks, parasite loads)
- **Feeding systems** (automated feeders, consumption rates)

**Machine learning models are increasingly deployed to classify:**

| Application | Classification Task | Business Impact |
|:---|:---|:---|
|  **Disease Detection** | Identify if a fish has *ISA virus* or *PD* (Positive/Negative) | Early detection saves millions in stock loss |
|  **Sea Lice Monitoring** | Classify lice load as *Low/Medium/High* | Determines treatment timing and costs |
|  **Feeding Optimization** | Predict if fish are *Hungry/Neutral/Full* | Reduces feed waste (30% of operational cost) |
|  **Mortality Prediction** | Flag *At-Risk* fish pens | Enables proactive intervention |
|  **Harvest Quality** | Grade salmon as *Premium/Standard/Reject* | Maximizes export revenue |
|  **Sex Classification** | Classify *Male/Female* using genetic markers | Optimizes breeding programs |

**The stakes are high:**
- A **False Negative** in disease detection means a sick fish spreads infection, potentially wiping out an entire pen.
- A **False Positive** in feeding means wasting expensive feed and polluting the water.
- A **False Negative** in mortality prediction delays intervention, increasing mortality rates.

Choosing the right metric directly impacts **profitability, sustainability, and animal welfare**.

**Foundation:** Every classification metric is derived from the **confusion matrix**, a 2×2 table that cross-tabulates actual vs. predicted classes.

**Binary Classification Example**: *Sea Lice Detection*

**Task: Predict if a salmon has a high sea lice load (>0.5 lice/g) requiring treatment.**

| | **Predicted: High Lice** | **Predicted: Low Lice** |
|:---|:---|:---|
| **Actual: High Lice** | **TP = 80** <br> *(Correctly identified infected fish)* | **FN = 20** <br> *(Missed infected fish: **dangerous**)* |
| **Actual: Low Lice** | **FP = 15** <br> *(Unnecessary treatment: **costly**)* | **TN = 85** <br> *(Correctly identified healthy fish)* |

**Terminology:**
- **True Positive (TP):** Correctly predicted positive class.
- **False Negative (FN):** Missed positive (Type II error).
- **False Positive (FP):** False alarm (Type I error).
- **True Negative (TN):** Correctly predicted negative class.

## Types

### 1. Accuracy
**Formula:** `(TP + TN) / (TP + TN + FP + FN)`

**Interpretation:** "Of all fish, what percentage did I classify correctly?"

**Salmon Example:**
- If you test 1,000 fish for ISA virus, and 950 are correctly classified → Accuracy = 95%.
- **However:** If only 2% of fish are infected, a model that always predicts "Healthy" would be 98% accurate—completely useless for disease control.

**When to use:** Balanced datasets where misclassification costs are equal.

**When to avoid:** Imbalanced data (common in aquaculture health monitoring).

---
### 2. Precision (Positive Predictive Value)
**Formula:** `TP / (TP + FP)`

**Interpretation:** "Of all the fish I flagged for treatment, how many were actually infected?"

**Salmon Example:**
- You flag 100 fish for sea lice treatment.
- Only 85 actually have high lice loads.
- **Precision = 85%** → 15 fish received unnecessary treatment (wasted medication, added stress).

**When to prioritize:** When **False Positives are expensive** (treating healthy fish with chemicals, quarantine costs).

---

### 3. Recall / Sensitivity (True Positive Rate)
**Formula:** `TP / (TP + FN)`

**Interpretation:** "Of all the truly infected fish, how many did I catch?"

**Salmon Example:**
- There are 100 fish with *Pancreas Disease (PD)* in a pen.
- Your model detects 90 of them.
- **Recall = 90%** → 10 infected fish slip through, potentially spreading disease.

**When to prioritize:** When **False Negatives are catastrophic** (contagious diseases, food safety risks).

---
### 4. Specificity (True Negative Rate)
**Formula:** `TN / (TN + FP)`

**Interpretation:** "Of all the healthy fish, how many did I correctly leave alone?"

**Salmon Example:**
- 900 healthy fish, 855 correctly classified as healthy.
- **Specificity = 95%** → 45 healthy fish were unnecessarily stressed by handling/treatment.

**When to prioritize:** When confirming negatives is critical (screening blood donors, ensuring safe harvest).

---

### 5. F1-Score
**Formula:** `2 × (Precision × Recall) / (Precision + Recall)`

**Interpretation:** The **harmonic mean** of Precision and Recall—balances both.

**Salmon Example:**
- Model A: Precision = 90%, Recall = 50% → F1 = 64% (too many missed sick fish).
- Model B: Precision = 70%, Recall = 80% → F1 = 75% (better balance for disease detection).

**When to use:** When you need a single metric for imbalanced data and care equally about FP and FN.

---

### 6. Fβ-Score (Family of F-Scores)
**Formula:** `(1 + β²) × (Precision × Recall) / ((β² × Precision) + Recall)`

**Common Variants:**
- **F0.5-Score** (β=0.5): Precision weighs **twice** as much as Recall.
- **F2-Score** (β=2): Recall weighs **twice** as much as Precision.

**Salmon Example:**
- **F2-Score** is ideal for disease surveillance—missing a sick fish (FN) is far worse than treating a healthy one (FP).
- **F0.5-Score** is ideal for feeding optimization—overfeeding (FP) wastes money and pollutes; underfeeding (FN) is less critical.

---
### 7. Matthews Correlation Coefficient (MCC)
**Formula:** `(TP×TN - FP×FN) / sqrt((TP+FP)(TP+FN)(TN+FP)(TN+FN))`

**Range:** -1 (complete disagreement) to +1 (perfect), 0 = random guessing.

**Why it matters:** The **only** binary metric that considers all four cells of the confusion matrix. It's robust to class imbalance and provides a **balanced single-number summary**.

**Salmon Example:**
- Accuracy says 95%, but MCC might reveal the model is only marginally better than random because it's just guessing "Healthy" most of the time.
- **Goal:** MCC > 0.6 for reliable deployment.

**When to use:** The **best overall metric** for comparing binary classifiers, especially on imbalanced aquaculture datasets.

---

### 8. ROC-AUC (Area Under the Receiver Operating Characteristic Curve)
- **Plot:** True Positive Rate (Recall) vs. False Positive Rate (1 - Specificity) across all thresholds.
- **Range:** 0.5 (random) to 1.0 (perfect).

**Salmon Example:**
- You're comparing 3 models for mortality prediction.
- Model A AUC = 0.92, Model B AUC = 0.88, Model C AUC = 0.78.
- Choose Model A: it distinguishes at-risk from healthy pens best.

**When to use:** General model comparison when classes are relatively balanced.

**Caveat:** Can overestimate performance on highly imbalanced data (e.g., 1% mortality rate).

---

### 9. PR-AUC (Precision-Recall Area Under Curve)
- **Plot:** Precision vs. Recall across all thresholds.
- More sensitive to imbalanced data than ROC-AUC.

**Salmon Example:**
- Disease prevalence is 2% (98% healthy).
- ROC-AUC might show 0.90, but PR-AUC reveals 0.45—the model isn't actually useful for detection.
- **Action:** Choose PR-AUC over ROC-AUC for rare events (disease outbreaks, mortality).

**When to use:** **Mandatory** for imbalanced aquaculture datasets (most health and behavior data).

---


