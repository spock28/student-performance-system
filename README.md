# Student Performance Prediction System

## Objective

This project predicts student performance using a hybrid intelligent system combining fuzzy logic concepts and a neural network model.

---

## Inputs

* Attendance
* Assignment Marks
* Test Marks

---

## Output

* Performance Level:

  * Poor
  * Average
  * Good

---

## Technologies Used

* Python
* NumPy
* Scikit-learn (MLPClassifier)

---

## Implementation

The system uses a dataset of student records:

```python
X = [
    [90, 85, 88],
    [60, 65, 70],
    [30, 40, 35],
    [80, 78, 82],
    [50, 55, 60]
]

y = ["Good", "Average", "Poor", "Good", "Average"]
```

A neural network (MLPClassifier) is trained on this data to classify performance levels.

---

## Output Example

```bash
Performance: Average
```

---

## Hybrid System Explanation

### Fuzzy Logic Concept:

* Student performance is categorized into:

  * Poor
  * Average
  * Good
* Inputs like attendance, assignment, and test marks can belong to multiple categories partially.
* This reflects real-world uncertainty and reasoning.

### Neural Network Learning:

* A Multi-Layer Perceptron (MLPClassifier) is used.
* It learns patterns from input data automatically.
* No manual rule-writing is required.

### Integration:

* Fuzzy logic provides the conceptual classification framework.
* The neural network learns and replaces fuzzy rules from data.
* This creates a hybrid intelligent system combining:

  * Human-like reasoning (fuzzy logic)
  * Machine learning (neural network)

---

## Conclusion

This project demonstrates how fuzzy logic concepts and neural networks can be combined to build an intelligent system for predicting student performance.
