# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1A3PAuF3Swh8gJYL79rAZKyaHainQsYqR
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Assuming you have the Iris dataset in a CSV file named "iris.csv"
# Adjust the path if needed.
iris_data = pd.read_csv("/content/Iris.csv")

# Separate the features (sepal and petal measurements) and labels (species)
X = iris_data.drop("Species", axis=1)
y = iris_data["Species"]
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Standardize the features to have zero mean and unit variance
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Choose the value of k (number of neighbors) for the k-NN algorithm
k_neighbors = 3
# Create the k-NN classifier
knn_classifier = KNeighborsClassifier(n_neighbors=k_neighbors)
# Train the classifier using the training data
knn_classifier.fit(X_train, y_train)

# Predict the species for the test set
y_pred = knn_classifier.predict(X_test)
# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
# Generate a classification report
print("Classification Report:")
print(classification_report(y_test, y_pred))
# Generate a confusion matrix
confusion_mat = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(confusion_mat)