import numpy as np
from sklearn.datasets import load_iris

class Node:
    def __init__(self, feature=None, threshold=None, left=None, right=None, *, value=None):
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        self.value = value

class DecisionTree:
    def __init__(self, max_depth=None):
        self.max_depth = max_depth

    def fit(self, X, y):
        self.n_classes = len(set(y))
        self.n_features = X.shape[1]
        self.tree = self._grow_tree(X, y)

    def _grow_tree(self, X, y, depth=0):
        n_samples_per_class = [np.sum(y == i) for i in range(self.n_classes)]
        predicted_class = np.argmax(n_samples_per_class)
        node = Node(value=predicted_class)

        if depth < self.max_depth:
            best_gain = 0
            best_feature = None
            best_threshold = None

            for feature in range(self.n_features):
                thresholds = np.unique(X[:, feature])
                for threshold in thresholds:
                    gain = self._information_gain(X, y, feature, threshold)
                    if gain > best_gain:
                        best_gain = gain
                        best_feature = feature
                        best_threshold = threshold

            if best_gain > 0:
                left_indices = X[:, best_feature] <= best_threshold
                right_indices = X[:, best_feature] > best_threshold
                left = self._grow_tree(X[left_indices], y[left_indices], depth + 1)
                right = self._grow_tree(X[right_indices], y[right_indices], depth + 1)
                node = Node(feature=best_feature, threshold=best_threshold, left=left, right=right)

        return node

    def _gini(self, y):
        m = len(y)
        return 1.0 - sum((np.sum(y == c) / m) ** 2 for c in range(self.n_classes))

    def _information_gain(self, X, y, feature, threshold):
        left_indices = X[:, feature] <= threshold
        right_indices = X[:, feature] > threshold

        n = len(y)
        nl = np.sum(left_indices)
        nr = np.sum(right_indices)

        if nl == 0 or nr == 0:
            return 0

        left_gini = self._gini(y[left_indices])
        right_gini = self._gini(y[right_indices])
        ig = self._gini(y) - (nl / n) * left_gini - (nr / n) * right_gini
        return ig

    def predict(self, X):
        return [self._predict(x) for x in X]

    def _predict(self, x):
        node = self.tree
        while node.left:
            if x[node.feature] <= node.threshold:
                node = node.left
            else:
                node = node.right
        return node.value

# Testing the Decision Tree
iris = load_iris()
X, y = iris.data, iris.target

tree = DecisionTree(max_depth=3)
tree.fit(X, y)

# Predictions
predictions = tree.predict(X)
print("Predictions:", predictions)
