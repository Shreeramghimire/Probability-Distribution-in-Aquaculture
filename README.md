# Probability Distribution (PD) in Aquaculture
This repository presents theory on probability distribution, different toolset, metrics, and process that help to understand the aquauculture in a better way. 

**Written by: Shreeram Ghimire**

**Start Date: 21 August 2026**

## Definition
Probability distribution is a mathematical function that describes the likelihood of different possible outcomes occurring in a random experiment or process.

It is about answering these two questions:

1. What are all the possible values that could happen?

2. What is the probability (the chance) of each of those specific values happening?

Instead of just saying, "A fish might weigh something," a probability distribution gives the full picture: "There is a 10% chance the fish weighs less than 450g, a 50% chance it weighs between 450g and 550g, and a 15% chance it weighs over 600g."

## Two types

### 1. Discrete PD
The outcome can only be specific, separate, whole-number values that satisfy the concept of a discrete distribution. 

Example: Number of fish that die in a tank (0, 1, 2, 3...), the number of disease outbreaks in a year

It is often visualized as a bar chart, where each bar represents a specific outcome, and the height of the bar is its probability. All the bars add up to 100% (or 1.0).

***Common examples***: Binomial distribution (success/failure counts), Poisson distribution (counting rare events over time).

### 2. Continious PD
When the outcome can be any number within a range, the distribution of such data is called continuous. 

Example: The exact weight of a salmon (500.2g, 500.21g, 500.215g...), water temperature, dissolved oxygen levels, or growth rate.

Because there are infinite possible values, the probability of any single exact number (like exactly 500.0000g) is practically zero. Instead, we visualize it as a smooth curve (called a Probability Density Function, or PDF). The total area underneath the entire curve equals 100% (or 1.0). The probability of a range (e.g., between 500g and 600g) is the area under the curve between those two points.

***Common examples***: Normal distribution (the classic "bell curve"), Exponential distribution (time until an event occurs), Uniform distribution (all values equally likely).

## Basic Assumption
1. All probabilities must be between 0 and 1 (or 0% and 100%). You can never have a negative chance, and you can never have a chance greater than 100%.
2. The total probability must sum to exactly 1. If you add up the probabilities of all possible outcomes (the heights of all the bars, or the total area under the curve), it must equal 100%. This means the distribution covers every possible thing that could happen.

## Defining the Distribution 

Distributions are usually summarized by two key numbers that tell you its shape:

1. Central Tendency (Where is the middle?): This is often the Mean (the average) or the Median (the exact middle point). In aquaculture, this tells you the "expected" weight of a fish at harvest.

2. Spread / Variability (How wide is it?): This is often the Variance or Standard Deviation. This tells you how much uncertainty there is. A small spread means all the fish are roughly the same size (consistent). A large spread means some fish are tiny and some are huge (inconsistent).
