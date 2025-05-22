import pandas as pd
import numpy as np

cubs_batting = pd.read_csv("cubs_standard_batting_team_totals_clean.csv")
cubs_pitching = pd.read_csv("cubs_standard_pitching_team_totals_clean.csv")
whitesox_batting = pd.read_csv("whitesox_standard_batting_team_totals_clean.csv")
whitesox_pitching = pd.read_csv("whitesox_standard_pitching_team_totals_clean.csv")

# Reload with correct columns specified
cubs_schedule = pd.read_csv("2025_Cubs_schedule.csv")
whitesox_schedule = pd.read_csv("2025_CWS_schedule.csv")

# Extract OPS and ERA from team stats
cubs_ops = cubs_batting['OPS'].iloc[0]
cubs_era = cubs_pitching['ERA'].iloc[0]
whitesox_ops = whitesox_batting['OPS'].iloc[0]
whitesox_era = whitesox_pitching['ERA'].iloc[0]

# Team strength score
cubs_strength = cubs_ops / cubs_era
whitesox_strength = whitesox_ops / whitesox_era
average_opponent_strength = 0.055  # neutral benchmark

# Simulation settings
num_simulations = 1000
cubs_wins = []
whitesox_wins = []

def calculate_win_probability(team_strength, opponent_strength):
    return team_strength / (team_strength + opponent_strength)

for _ in range(num_simulations):
    cubs_win_count = 0
    whitesox_win_count = 0

    for opponent in cubs_schedule['Opp'].astype(str):
        if "White" in opponent:
            win_prob = calculate_win_probability(cubs_strength, whitesox_strength)
        else:
            win_prob = calculate_win_probability(cubs_strength, average_opponent_strength)
        cubs_win_count += np.random.rand() < win_prob

    for opponent in whitesox_schedule['Opp'].astype(str):
        if "Cubs" in opponent:
            win_prob = calculate_win_probability(whitesox_strength, cubs_strength)
        else:
            win_prob = calculate_win_probability(whitesox_strength, average_opponent_strength)
        whitesox_win_count += np.random.rand() < win_prob

    cubs_wins.append(cubs_win_count)
    whitesox_wins.append(whitesox_win_count)

# Results summary
results_df = pd.DataFrame({
    "Cubs Wins": cubs_wins,
    "White Sox Wins": whitesox_wins
})

results_df