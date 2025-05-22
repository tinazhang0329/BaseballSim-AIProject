import pytest
import numpy as np
import pandas as pd
from baseball_monte_carlo_simulation import calculate_win_probability  # adjust import path

# -------- UNIT TESTS --------

def test_calculate_win_probability_typical():
    result = calculate_win_probability(0.8, 0.2)
    assert 0.79 < result < 0.81

def test_calculate_win_probability_equal_strength():
    result = calculate_win_probability(1.0, 1.0)
    assert result == 0.5

def test_calculate_win_probability_zero_opponent():
    result = calculate_win_probability(0.5, 0.0)
    assert result == 1.0

def test_calculate_win_probability_zero_team():
    result = calculate_win_probability(0.0, 0.5)
    assert result == 0.0

# -------- INTEGRATION TEST --------

def test_mini_season_simulation():
    team_strength = 0.6
    opponent_strength = 0.4
    games = 100
    wins = 0

    for _ in range(games):
        win_prob = calculate_win_probability(team_strength, opponent_strength)
        wins += np.random.rand() < win_prob

    assert 50 < wins < 90  # check plausible bounds
