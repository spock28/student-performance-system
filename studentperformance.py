import numpy as np
from sklearn.neural_network import MLPClassifier

# Input: Attendance, Assignment, Test
X = np.array([
    [90, 85, 88],
    [60, 65, 70],
    [30, 40, 35],
    [80, 78, 82],
    [50, 55, 60]
])

# Output labels: 0=Poor, 1=Average, 2=Good
y = np.array([2, 1, 0, 2, 1])

model = MLPClassifier(hidden_layer_sizes=(5,), max_iter=1000)
model.fit(X, y)

test = [[75, 70, 72]]
pred = model.predict(test)

labels = ["Poor", "Average", "Good"]
print("Performance:", labels[pred[0]])