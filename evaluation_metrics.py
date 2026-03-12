from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay

import matplotlib.pyplot as plt


def evaluate_model(true_labels, predicted_labels):

    accuracy = accuracy_score(true_labels, predicted_labels)

    precision = precision_score(
        true_labels,
        predicted_labels,
        average="weighted",
        zero_division=0
    )

    recall = recall_score(
        true_labels,
        predicted_labels,
        average="weighted",
        zero_division=0
    )

    f1 = f1_score(
        true_labels,
        predicted_labels,
        average="weighted",
        zero_division=0
    )

    accuracy_percent = accuracy * 100

    print("\nMODEL EVALUATION METRICS")

    print("Accuracy :", round(accuracy_percent, 2), "%")
    print("Precision:", round(precision, 3))
    print("Recall   :", round(recall, 3))
    print("F1 Score :", round(f1, 3))

    # Expected accuracy derived from model performance
    lower_bound = max(0, accuracy_percent - 5)
    upper_bound = min(100, accuracy_percent + 5)

    print("\nExpected Accuracy Range (Model Dependent):",
          round(lower_bound,2), "% -", round(upper_bound,2), "%")

    
    # Confusion Matrix

    cm = confusion_matrix(true_labels, predicted_labels)

    disp = ConfusionMatrixDisplay(
        confusion_matrix=cm,
        display_labels=["CRITICAL","HIGH","MEDIUM","LOW"]
    )

    disp.plot(cmap="Blues")

    plt.title("Collision Risk Prediction Confusion Matrix")

    plt.show()

    
    # Performance Graph

    metrics = ["Accuracy","Precision","Recall","F1 Score"]

    values = [
        accuracy,
        precision,
        recall,
        f1
    ]

    plt.figure()

    plt.bar(metrics, values)

    plt.ylim(0,1)

    plt.title("AI Model Performance")

    plt.ylabel("Score")

    plt.show()

    return accuracy, precision, recall, f1