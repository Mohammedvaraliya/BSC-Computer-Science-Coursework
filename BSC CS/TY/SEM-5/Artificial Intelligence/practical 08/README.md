## Practical 08

## Problem Statement

**K-Nearest Neighbors (K-NN)**

1. Implement the K-NN algorithm for classification or regression.
1. Apply the K-NN algorithm to a given dataset and predict the class or value for test data.
1. Evaluate the accuracy or error of the predictions and analyze the results.

---

K Nearest Neighbor algorithm falls under the Supervised Learning category and is used for classification (most commonly) and regression. It is a versatile algorithm also used for imputing missing values and resampling datasets. As the name (K Nearest Neighbor) suggests it considers K Nearest Neighbors (Data points) to predict the class or continuous value for the new Datapoint.

The algorithm’s learning is:

1. Instance-based learning: Here we do not learn weights from training data to predict output (as in model-based algorithms) but use entire training instances to predict output for unseen data.
2. Lazy Learning: Model is not learned using training data prior and the learning process is postponed to a time when prediction is requested on the new instance.
3. Non -Parametric: In KNN, there is no predefined form of the mapping function.

---

## Algorithm

**Step 1**: Start

**Step 2**: Load the training data.

**Step 3**: Prepare data by scaling, missing value treatment, and dimensionality reduction as required.

**Step 4**: Find the optimal value for K:

**Step 5**: Predict a class value for new data:

**Step 5.1**: Calculate distance(X, Xi) from i=1,2,3,….,n.where X= new data point, Xi= training data, distance as per your chosen distance metric.

**Step 5.2**: Sort these distances in increasing order with corresponding train data.

**Step 5.3**: From this sorted list, select the top ‘K’ rows.

**Step 5.4**: Find the most frequent class from these chosen ‘K’ rows. This will be your predicted class.

**Step 6**: End.

---