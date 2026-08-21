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
