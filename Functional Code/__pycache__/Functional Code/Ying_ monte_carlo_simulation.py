import pandas as pd
import numpy as np
import os

cubs_strength = 1.05
whitesox_strength = 0.95
average_opponent_strength = 0.055

cubs_schedule = ["White Sox"] + ["Other"] * 161
whitesox_schedule = ["Cubs"] + ["Other"] * 161

num_simulations = 1000
cubs_wins = []
whitesox_wins = []

def calculate_win_probability(team_strength, opponent_strength):
    return team_strength / (team_strength + opponent_strength)

for _ in range(num_simulations):
    cubs_win = 0
    whitesox_win = 0

    for opponent in cubs_schedule:
        prob = calculate_win_probability(cubs_strength, whitesox_strength) if opponent == "White Sox" else calculate_win_probability(cubs_strength, average_opponent_strength)
        cubs_win += np.random.rand() < prob

    for opponent in whitesox_schedule:
        prob = calculate_win_probability(whitesox_strength, cubs_strength) if opponent == "Cubs" else calculate_win_probability(whitesox_strength, average_opponent_strength)
        whitesox_win += np.random.rand() < prob

    cubs_wins.append(cubs_win)
    whitesox_wins.append(whitesox_win)

os.makedirs("Result", exist_ok=True)

results_df = pd.DataFrame({
    "Cubs Wins": cubs_wins,
    "White Sox Wins": whitesox_wins
})
results_df.to_csv("Result/simulation_results.csv", index=False)
results_df.describe().to_csv("Result/simulation_summary.csv")
