import matplotlib.pyplot as plt

def plot_risk_distribution(risks):

    plt.hist(risks, bins=40)

    plt.xlabel("Risk Score")
    plt.ylabel("Frequency")

    plt.title("Collision Risk Distribution")

    plt.show()