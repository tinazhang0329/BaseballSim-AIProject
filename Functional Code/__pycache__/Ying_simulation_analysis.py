import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

RESULTS_PATH = "Result/simulation_results.csv"
PLOT_DIR = "Result/"
HIST_FILE = "win_distribution_histogram.png"
BOX_FILE = "win_distribution_boxplot.png"
KDE_FILE = "win_distribution_density.png"

if not os.path.exists(RESULTS_PATH):
    raise FileNotFoundError(f"CSV file not found at: {RESULTS_PATH}")

os.makedirs(PLOT_DIR, exist_ok=True)

df = pd.read_csv(RESULTS_PATH)

required_columns = ["Cubs Wins", "White Sox Wins"]
for col in required_columns:
    if col not in df.columns:
        raise ValueError(f"Missing column: '{col}'")

plt.figure(figsize=(10, 6))
sns.histplot(df["Cubs Wins"], color="blue", kde=True, label="Cubs", bins=20)
sns.histplot(df["White Sox Wins"], color="red", kde=True, label="White Sox", bins=20)
plt.title("Simulated Win Distribution")
plt.xlabel("Number of Wins")
plt.ylabel("Frequency")
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(PLOT_DIR, HIST_FILE))
plt.close()

plt.figure(figsize=(6, 5))
sns.boxplot(data=df[["Cubs Wins", "White Sox Wins"]])
plt.title("Boxplot of Simulated Wins")
plt.tight_layout()
plt.savefig(os.path.join(PLOT_DIR, BOX_FILE))
plt.close()

plt.figure(figsize=(10, 5))
sns.kdeplot(df["Cubs Wins"], label="Cubs", shade=True)
sns.kdeplot(df["White Sox Wins"], label="White Sox", shade=True)
plt.title("Win Distribution Density")
plt.xlabel("Number of Wins")
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(PLOT_DIR, KDE_FILE))
plt.close()
