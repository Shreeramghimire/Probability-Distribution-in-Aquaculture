Probability metrics, also known as **scoring rules**, are essential for evaluating the quality of probabilistic forecasts. 

Unlike simple accuracy, which only determines whether a prediction was correct or incorrect, these metrics evaluate both the **predicted outcome and the confidence associated with that prediction**. 

A strong probabilistic forecast should therefore be **reliable**, meaning its predicted probabilities are well-calibrated, and **sharp**, meaning it provides confident predictions when the available information supports them.

## 1. Brier Score (or Quadratic Score)
The Brier score is one of the most widely used metrics for evaluating binary (yes/no) probability forecasts. It is essentially the Mean Squared Error (MSE) of the probability forecast.

**What it measures:** The average squared difference between the predicted probability and the actual outcome (0 or 1). The score ranges from 0 to 1, with 0 being a perfect score.

For a set of $n$ predictions, the Brier Score is calculated as:

$$
BS = \frac{1}{n} \sum_{i=1}^{n} (p_i - y_i)^2
$$

where:

$p_i$ is the predicted probability for event $i$

$y_i$ is the actual outcome for event $i$ (1 if the event happened, 0 if it did not)

**Example:**

Forecast for rain: 90% (p=0.9). It rains (y=1): (0.9 - 1)² = 0.01

Forecast for rain: 90% (p=0.9). It does not rain (y=0): (0.9 - 0)² = 0.81

Interpretation: The Brier score heavily penalizes forecasts that are both wrong and very confident. It is popular because of its straightforward interpretation and its decomposition into metrics measuring calibration and discrimination.

## 2. Log Loss

The Logarithmic Score, commonly known as Log Loss or Cross-Entropy Loss, is one of the most important scoring rules for evaluating probabilistic forecasts. It is often considered a gold-standard metric because of its strong theoretical foundations in information theory and its close connection to maximum likelihood estimation.

Unlike accuracy, which only considers whether the predicted class is correct, Log Loss evaluates how much probability the model assigned to the outcome that actually occurred. It therefore rewards models that are both accurate and appropriately confident, while strongly penalizing predictions that assign very low probability to events that actually occur.


\[
\text{Log Score} = -\frac{1}{n} \sum_{i=1}^{n} \left[ o_i \ln(f_i) + (1 - o_i) \ln(1 - f_i) \right]
\]
