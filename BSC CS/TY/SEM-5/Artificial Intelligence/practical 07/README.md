## Practical 07

## Problem Statement

**Naive Bayes' Classifier**

1. Implement the Naive Bayes' algorithm for classification.
1. Train a Naive Bayes' model using a given dataset and calculate class probabilities.
1. Evaluate the accuracy of the model on test data and analyze the results.

---

Naive Baye’s Classifier is a classification technique based on Bayes’ Theorem. Naive Bayes classifier assumes that the presence of a particular feature in a class is unrelated to the presence of any other feature. Bayes theorem provides a way of calculating posterior probability $P(c|x)$ from $P(c)$, $P(x)$ and $P(x|c)$. Look at the equation below

$$
P(c|x) = \frac{P(x|c)P(c)}{P(x)}
$$



$$
P(c|x) = P(x_1|c) \times P(x_2|c) \times ... \times P(x_n|c) \times P(c)
$$

$P(c|x)$ is the posterior probability of class ($c$ - target) given predictor ($x$ - attributes).

$P(c)$ is the prior probability of class.

$P(x|c)$ is the likelihood which is the probability of predictor given class. 

$P(x)$ is the prior probability of predictor.

---

## Algorithm

Naive Bayes classifier calculates the probability of an event in the following steps:

**Step 1**: Start.

**Step 2**: Calculate the prior probability for given class labels

**Step 3**: Find Likelihood probability with each attribute for each class

**Step 4**: Put these value in Bayes Formula and calculate posterior probability.

**Step 5**: See which class has a higher probability, given the input belongs to the higher probability class.

**Step 6**: End.

---

