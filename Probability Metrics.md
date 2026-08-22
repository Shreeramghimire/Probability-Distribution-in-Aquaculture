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


$$
\text{Log Score} = -\frac{1}{n} \sum_{i=1}^{n} \left[ y_i \ln(p_i) + (1 - y_i) \ln(1 - p_i) \right]
$$

$p_i$ is the predicted probability for event i.

$y_i$ is the actual outcome for event i (1 if the event happened, 0 if it did not)

**Example:**

Forecast for rain: 90% (p=0.9). It rains (y=1): - [1 * ln(0.9)] = 0.105

Forecast for rain: 90% (p=0.9). It does not rain (y=0): - [0 * ln(0.9) + 1 * ln(0.1)] = 2.303

**Interpretation**

Lower Log Loss is better. A model receives a small penalty when it assigns a high probability to the outcome that actually occurs. However, it receives a very large penalty when it is highly confident but wrong.

For example, suppose a model predicts that a salmon farm has a 90% probability of experiencing high lice infestation:

- If high infestation occurs → the model is rewarded with a low loss.

- If high infestation does not occur → the model receives a large penalty.

This makes Log Loss particularly useful for applications such as sea-lice forecasting, where the probability and confidence of future infestation are often more informative than simply predicting whether infestation will or will not occur.

## 3. Continuous Ranked Probability Score (CRPS)

The Continuous Ranked Probability Score (CRPS) is a widely used scoring rule for evaluating probabilistic forecasts of continuous or numeric quantities. It can be viewed as a generalization of the Brier Score from binary or categorical outcomes to continuous variables.

Unlike a point forecast, which predicts a single value, CRPS evaluates the entire probability distribution predicted by the model. This makes it particularly useful when we want to assess not only the expected value of a forecast but also its uncertainty and spread.

CRPS measures the difference between the predicted cumulative distribution function (CDF) and the CDF of the actual observation.

Mathematically, it is defined as:

$$
\text{CRPS} = \int_{-\infty}^{\infty} (F(x) - \mathbf{1}_{y \leq x})^2 \, dx
$$

where:

$F(x)$ = predicted cumulative distribution function (CDF)

$y$ = observed value

$\mathbf{1}(x\geq y)$ = indicator function representing the CDF of the observed value

In simpler terms, CRPS measures the distance between the forecast probability distribution and the actual observed value.

#### Interpretation

**Lower CRPS is better.** A forecast receives a low score when its probability distribution is concentrated around the value that actually occurs. Forecasts that are poorly centered or excessively uncertain receive higher scores.

For example, suppose a model predicts the number of sea lice per salmon for the following week. Instead of predicting only:

> **Expected lice count = 0.8**

the model might produce a probability distribution showing the likelihood of different lice counts.

CRPS evaluates how well this entire predicted distribution corresponds to the actual lice count observed the following week.

**For Salmon Lice:** The main advantage of CRPS is that it evaluates both the accuracy and uncertainty of a continuous probabilistic forecast. This makes it particularly suitable for sea-lice forecasting when the objective is to predict not just a single future lice count, but the range of possible infestation levels and their associated probabilities.

## 4. Winkler Score (for Prediction Intervals)

The Winkler Score is a scoring rule specifically designed to evaluate the quality of prediction intervals. A prediction interval provides a range of values within which the true outcome is expected to fall with a specified probability, such as 90% or 95%.

Unlike metrics that evaluate only the predicted value, the Winkler Score considers both the width of the interval and whether the observed value falls within the interval.

**What It Measures**

The Winkler Score rewards narrow prediction intervals when they successfully contain the observed value. However, if the observation falls outside the interval, the score applies a penalty. The farther the observation is from the interval, the larger the penalty.

For a prediction interval with lower bound $l$, upper bound $u$, midpoint $m$, significance level $\alpha$, and observed value $y$, the Winkler Score can be expressed as:

$$
W =
\begin{cases}
|y-m|, & l \leq y \leq u \[6pt]
|y-m| + \frac{2}{\alpha}(l-y), & y < l \[6pt]
|y-m| + \frac{2}{\alpha}(y-u), & y > u
\end{cases}
$$

where:

- $y$ = observed value
  
- $l$ = lower bound of the prediction interval
  
- $u$ = upper bound of the prediction interval
  
- $m$ = midpoint of the prediction interval
$\alpha$ = significance level
$1-\alpha$ = nominal coverage of the interval
