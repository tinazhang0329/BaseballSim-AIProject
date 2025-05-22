import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

RESULTS_PATH = "Result/simulation_results.csv"
PLOT_DIR = "Result/"

os.makedirs(PLOT_DIR, exist_ok=True)


df = pd.read_csv(RESULTS_PATH)

plt.figure(figsize=(10, 6))
sns.histplot(df["Cubs Wins"], color="blue", kde=True, label="Cubs", bins=20)
sns.histplot(df["White Sox Wins"], color="red", kde=True, label="White Sox", bins=20)
plt.title("Simulated Win Distribution")
plt.xlabel("Number of Wins")
plt.ylabel("Frequency")
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(PLOT_DIR, "win_distribution_histogram.png"))
plt.close()


plt.figure(figsize=(6, 5))
sns.boxplot(data=df[["Cubs Wins", "White Sox Wins"]])
plt.title("Boxplot of Simulated Wins")
plt.tight_layout()
plt.savefig(os.path.join(PLOT_DIR, "win_distribution_boxplot.png"))
plt.close()


plt.figure(figsize=(10, 5))
sns.kdeplot(df["Cubs Wins"], label="Cubs", shade=True)
sns.kdeplot(df["White Sox Wins"], label="White Sox", shade=True)
plt.title("Win Distribution Density")
plt.xlabel("Number of Wins")
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(PLOT_DIR, "win_distribution_density.png"))
plt.close()

