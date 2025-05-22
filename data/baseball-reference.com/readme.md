# Baseball-Reference Raw Data

This folder contains raw CSV exports from [Baseball-Reference.com](https://www.baseball-reference.com/) for the 2025 Chicago Cubs and Chicago White Sox.

## Structure

- Each team has its own subfolder (e.g., `2025 Chicago Cubs/`, `2025 Chicago WhiteSox/`).
- Each subfolder contains tables such as batting, pitching, fielding, roster, and schedule data.
- Files are named to match the table type (e.g., `standard_batting.csv`, `full_season_roster.csv`).

## Data Source

All data in this directory was sourced from [Baseball-Reference.com](https://www.baseball-reference.com/).

## Usage

These files are used as input for the data cleaning and normalization pipeline (`data_prepper` module).  
Do not edit these files directly; always re-export from Baseball-Reference if updates are needed.

---

**Author:** Andrew D'Amico
**Email:** Andrew.Damico@u.northwestern.edu

