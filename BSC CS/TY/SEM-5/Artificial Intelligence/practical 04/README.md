## Practical 04

## Problem Statement

**Feed Forward Backpropagation Neural Network**

1. Implement the Feed Forward Backpropagation algorithm to train a neural network.
2. Use a given dataset to train the neural network for a specific task.
3. Evaluate the performance of the trained network on test data

---

The backpropagation algorithm is a type of supervised learning algorithm for artificial neural networks where we fine-tune the weight functions and improve the accuracy of the model. It employs the gradient descent method to reduce the cost function. It reduces the mean-squared distance between the predicted and the actual data. This type of algorithm is generally used for training feed-forward neural networks for a given data whose classifications are known to us.

## **Advantages of Backpropagation**

It is relatively faster and simple algorithm to implement. Extensively used in the field of face recognition and speech recognition.Moreover, it is a flexible method as no prior knowledge of the neural network is needed.

## **Disdavantages of Backpropagation**

The algorithm is advantageous for noisy and irregular data. However, the performance of backpropagation depends highly on the input.

## Algorithm

**Step 1**: Start

**Step 2**:The input layer receives the input.

**Step 3:**The input is then averaged overweights.

**Step 4**:Each hidden layer processes the output. Each output is referred to as “Error” here which is actually the difference between the actual output and the desired output.

**Step 5**:In this step, the algorithm moves back to the hidden layers again to optimize the weights and reduce the error.

**Step 6:** End

---