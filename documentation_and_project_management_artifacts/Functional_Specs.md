# Functional Specifications – Baseball Season Simulation

This document defines the core functionality and system behavior for a baseball season simulation tool that uses Monte Carlo methods and real-world data to model game outcomes.

---

## Objective

Simulate full baseball seasons using team-level statistical inputs and official schedule data to estimate expected win totals for each team. The simulation outputs probabilistic season outcomes for analysis or visualization.

---

## User Story

> As a user, I want to upload cleaned data and simulate a full season so I can evaluate team performance and forecast win outcomes.

**Acceptance Criteria:**
- The system accepts structured input files (team stats and game schedules)
- A Monte Carlo engine simulates many full seasons
- Final output includes win distribution summaries and exportable results

---

## System Overview

The system processes structured inputs, calculates team strength metrics, and uses probabilistic models to simulate game outcomes over multiple iterations. Output includes team win distributions and statistical summaries.

---

## Core Functions

### `calculate_win_probability(team_strength, opponent_strength)`
- **Purpose:** Estimate win chance based on relative strength
- **Inputs:**  
  - `team_strength` (float)  
  - `opponent_strength` (float)  
- **Output:** float between 0 and 1  
- **Logic:** Uses ratio transformation or logistic model

---

### `simulate_season(schedule, strength_lookup)`
- **Purpose:** Run one full season simulation for a single team
- **Inputs:**  
  - `schedule`: list of opponents  
  - `strength_lookup`: dict of team names to strength values  
- **Output:** int (number of wins)

---

### `run_simulations(num_simulations, all_schedules, strength_lookup)`
- **Purpose:** Simulate multiple full seasons for multiple teams
- **Inputs:**  
  - `num_simulations`: int  
  - `all_schedules`: dict of team → schedule  
  - `strength_lookup`: dict of team → strength  
- **Output:** DataFrame with simulated win totals

---

## Inputs

- `*.csv` file with team schedule (columns: date, opponent, etc.)
- `*.csv` file with team-level statistics (OPS, ERA, or similar)

---

## Outputs

- DataFrame or CSV with simulation results per team
- Summary stats: mean, std dev, min, max win totals
- Optional: visualizations of distribution (histograms)

---

## MVP Scope

- Team-level simulation only (no player-level interactions)
- Strength metric = simple derived ratio (e.g., OPS / ERA)
- Randomness modeled with `np.random.rand()` comparison

---

## Future Extensions

- Add player-level simulation and dynamic lineups
- Incorporate weather, home/away, and park factors
- Build interactive front-end for uploading data and viewing results
