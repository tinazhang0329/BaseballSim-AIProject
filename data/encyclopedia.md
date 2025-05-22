# 2025 Cubs & White Sox Data Tables Reference

This document describes each CSV data table available for the 2025 Chicago Cubs and Chicago White Sox, explains every variable/column, and summarizes the importance of each table for game day simulation.  
**Variables needing additional preparation or parsing are marked with ⚠️ and explained in the notes.**

---

## Table Index

- [standard_batting.csv](#standard_battingcsv)
- [value_batting.csv](#value_battingcsv)
- [standard_pitching.csv](#standard_pitchingcsv)
- [value_pitching.csv](#value_pitchingcsv)
- [standard_fielding.csv](#standard_fieldingcsv)
- [full_season_roster_appearances.csv](#full_season_roster_appearancescsv)
- [current_40_roster.csv / 40_man_roster.csv](#current_40_rostercsv--40_man_rostercsv)
- [Data Dict.txt](#data-dicttxt)

---

## standard_batting.csv

**Description:**  
Traditional batting stats for each player.

**Variables:**
- `Rk`: Row number
- `Player` ⚠️: Player name (may include `*` for left-handed, `#` for switch; needs to be parsed for handedness)
- `Age`: Player age
- `Pos` ⚠️: Primary position (may need normalization; sometimes contains multiple positions or codes)
- `WAR`: Wins Above Replacement
- `G`: Games played
- `PA`: Plate appearances
- `AB`: At bats
- `R`: Runs scored
- `H`: Hits
- `2B`: Doubles
- `3B`: Triples
- `HR`: Home runs
- `RBI`: Runs batted in
- `SB`: Stolen bases
- `CS`: Caught stealing
- `BB`: Walks
- `SO`: Strikeouts
- `BA`: Batting average
- `OBP`: On-base percentage
- `SLG`: Slugging percentage
- `OPS`: On-base plus slugging
- `OPS+`: OPS adjusted for league/park
- `rOBA`: Weighted on-base average
- `Rbat+`: Batting runs above average
- `TB`: Total bases
- `GIDP`: Grounded into double play
- `HBP`: Hit by pitch
- `SH`: Sacrifice hits
- `SF`: Sacrifice flies
- `IBB`: Intentional walks
- `Pos` (again) ⚠️: Secondary/alternate positions played (needs clarification/normalization)
- `Awards`: Awards received
- `Player-additional`: Baseball-Reference player ID
- `PrimaryPosition`: Primary position code
- `EligiblePositions`: List of eligible positions
- `PositionFlexibility`: Flexibility score based on positions played
- `Is1B`: Boolean for first base eligibility
- `Is2B`: Boolean for second base eligibility
- `Is3B`: Boolean for third base eligibility
- `IsSS`: Boolean for shortstop eligibility
- `IsLF`: Boolean for left field eligibility
- `IsCF`: Boolean for center field eligibility
- `IsRF`: Boolean for right field eligibility
- `IsC`: Boolean for catcher eligibility
- `IsP`: Boolean for pitcher eligibility

**Preparation Needed:**
- ⚠️ **Handedness**: Parse from `Player` field, create new `Handedness` column (`L`, `R`, `S`).
- ⚠️ **Player Name**: Remove handedness symbol from `Player`.
- ⚠️ **Position**: Normalize `Pos` fields to standard position codes; if multiple, select primary or create a list.
- ⚠️ **Dummy Variables**: Consider creating boolean columns for each position (e.g., `is_1B`, `is_2B`, etc.) for lineup logic.

---

## value_batting.csv

**Description:**  
Advanced value metrics for batters.

**Variables:**
- `Rk`: Row number
- `Player` ⚠️: Player name (same handedness parsing as above)
- `Age`: Player age
- `PA`: Plate appearances
- `Rbat`: Batting runs above average
- `Rbaser`: Baserunning runs above average
- `Rdp`: Double play runs above average
- `Rfield`: Fielding runs above average
- `Rpos`: Positional adjustment runs
- `RAA`: Runs above average
- `WAA`: Wins above average
- `Rrep`: Replacement runs
- `RAR`: Runs above replacement
- `WAR`: Wins above replacement
- `waaWL%`: Win-loss percentage based on WAA
- `162WL%`: Win-loss percentage over 162 games
- `oWAR`: Offensive WAR
- `dWAR`: Defensive WAR
- `oRAR`: Offensive runs above replacement
- `Pos` ⚠️: Position(s) played (may need normalization)
- `Awards`: Awards received
- `Player-additional`: Baseball-Reference player ID
- `PrimaryPosition`: Primary position code
- `EligiblePositions`: List of eligible positions
- `PositionFlexibility`: Flexibility score based on positions played
- `Is1B`: Boolean for first base eligibility
- `Is2B`: Boolean for second base eligibility
- `Is3B`: Boolean for third base eligibility
- `IsSS`: Boolean for shortstop eligibility
- `IsLF`: Boolean for left field eligibility
- `IsCF`: Boolean for center field eligibility
- `IsRF`: Boolean for right field eligibility
- `IsC`: Boolean for catcher eligibility
- `IsP`: Boolean for pitcher eligibility

**Preparation Needed:**
- ⚠️ **Handedness**: Parse from `Player`.
- ⚠️ **Position**: Normalize as above.

---

## standard_pitching.csv

**Description:**  
Traditional pitching stats for each player.

**Variables:**
- `Rk`: Row number
- `Player` ⚠️: Player name (parse for handedness)
- `Age`: Player age
- `Pos` ⚠️: Pitcher role/position (may need normalization)
- `WAR`: Wins Above Replacement
- `W`: Wins
- `L`: Losses
- `ERA`: Earned run average
- `G`: Games pitched
- `GS`: Games started
- `GF`: Games finished
- `CG`: Complete games
- `SHO`: Shutouts
- `SV`: Saves
- `IP`: Innings pitched
- `H`: Hits allowed
- `R`: Runs allowed
- `ER`: Earned runs allowed
- `HR`: Home runs allowed
- `BB`: Walks allowed
- `IBB`: Intentional walks allowed
- `SO`: Strikeouts
- `HBP`: Hit by pitch
- `BK`: Balks
- `WP`: Wild pitches
- `BF`: Batters faced
- `ERA+`: ERA adjusted for league/park
- `FIP`: Fielding Independent Pitching
- `WHIP`: Walks plus hits per inning pitched
- `Awards`: Awards received
- `Player-additional`: Baseball-Reference player ID
- `PrimaryPosition`: Primary position code
- `EligiblePositions`: List of eligible positions
- `PositionFlexibility`: Flexibility score based on positions played
- `Is1B`: Boolean for first base eligibility
- `Is2B`: Boolean for second base eligibility
- `Is3B`: Boolean for third base eligibility
- `IsSS`: Boolean for shortstop eligibility
- `IsLF`: Boolean for left field eligibility
- `IsCF`: Boolean for center field eligibility
- `IsRF`: Boolean for right field eligibility
- `IsC`: Boolean for catcher eligibility
- `IsP`: Boolean for pitcher eligibility

**Preparation Needed:**
- ⚠️ **Handedness**: Parse from `Player`.
- ⚠️ **Position**: Normalize pitcher roles (SP, RP, CL, etc.).

---

## value_pitching.csv

**Description:**  
Advanced value metrics for pitchers.

**Variables:**
- `Rk`: Row number
- `Player` ⚠️: Player name (parse for handedness)
- `Age`: Player age
- `W`: Wins
- `L`: Losses
- `ERA`: Earned run average
- `G`: Games pitched
- `GS`: Games started
- `SV`: Saves
- `IP`: Innings pitched
- `H`: Hits allowed
- `R`: Runs allowed
- `ER`: Earned runs allowed
- `HR`: Home runs allowed
- `BB`: Walks allowed
- `SO`: Strikeouts
- `WAR`: Wins Above Replacement
- `RA9`: Runs allowed per 9 innings
- `FIP`: Fielding Independent Pitching
- `ERA+`: ERA adjusted for league/park
- `Awards`: Awards received
- `Player-additional`: Baseball-Reference player ID
- `PrimaryPosition`: Primary position code
- `EligiblePositions`: List of eligible positions
- `PositionFlexibility`: Flexibility score based on positions played
- `Is1B`: Boolean for first base eligibility
- `Is2B`: Boolean for second base eligibility
- `Is3B`: Boolean for third base eligibility
- `IsSS`: Boolean for shortstop eligibility
- `IsLF`: Boolean for left field eligibility
- `IsCF`: Boolean for center field eligibility
- `IsRF`: Boolean for right field eligibility
- `IsC`: Boolean for catcher eligibility
- `IsP`: Boolean for pitcher eligibility

**Preparation Needed:**
- ⚠️ **Handedness**: Parse from `Player`.

---

## standard_fielding.csv

**Description:**  
Fielding stats for each player.

**Variables:**
- `Rk`: Row number
- `Player` ⚠️: Player name (parse for handedness)
- `Age`: Player age
- `Pos` ⚠️: Position(s) played (may need normalization)
- `G`: Games at position
- `GS`: Games started at position
- `Inn`: Innings played at position
- `PO`: Putouts
- `A`: Assists
- `E`: Errors
- `DP`: Double plays turned
- `Fld%`: Fielding percentage
- `Awards`: Awards received
- `Player-additional`: Baseball-Reference player ID
- `PrimaryPosition`: Primary position code
- `EligiblePositions`: List of eligible positions
- `PositionFlexibility`: Flexibility score based on positions played
- `Is1B`: Boolean for first base eligibility
- `Is2B`: Boolean for second base eligibility
- `Is3B`: Boolean for third base eligibility
- `IsSS`: Boolean for shortstop eligibility
- `IsLF`: Boolean for left field eligibility
- `IsCF`: Boolean for center field eligibility
- `IsRF`: Boolean for right field eligibility
- `IsC`: Boolean for catcher eligibility
- `IsP`: Boolean for pitcher eligibility

**Preparation Needed:**
- ⚠️ **Handedness**: Parse from `Player`.
- ⚠️ **Position**: Normalize as above.

---

## full_season_roster_appearances.csv

**Description:**  
Roster of all players who appeared for the team during the season, with appearance counts.

**Variables:**
- `Player` ⚠️: Player name (parse for handedness)
- `Pos` ⚠️: Position(s) played (may need normalization)
- `G`: Games played
- `GS`: Games started
- `Awards`: Awards received
- `Player-additional`: Baseball-Reference player ID
- `PrimaryPosition`: Primary position code
- `EligiblePositions`: List of eligible positions
- `PositionFlexibility`: Flexibility score based on positions played
- `Is1B`: Boolean for first base eligibility
- `Is2B`: Boolean for second base eligibility
- `Is3B`: Boolean for third base eligibility
- `IsSS`: Boolean for shortstop eligibility
- `IsLF`: Boolean for left field eligibility
- `IsCF`: Boolean for center field eligibility
- `IsRF`: Boolean for right field eligibility
- `IsC`: Boolean for catcher eligibility
- `IsP`: Boolean for pitcher eligibility

**Preparation Needed:**
- ⚠️ **Handedness**: Parse from `Player`.
- ⚠️ **Position**: Normalize as above.

---

## current_40_roster.csv / 40_man_roster.csv

**Description:**  
Current 40-man roster for the team.

**Variables:**
- `Player` ⚠️: Player name (parse for handedness)
- `Pos` ⚠️: Primary position (normalize)
- `Status`: Roster status (active, injured, etc.)
- `Awards`: Awards received
- `Player-additional`: Baseball-Reference player ID
- `PrimaryPosition`: Primary position code
- `EligiblePositions`: List of eligible positions
- `PositionFlexibility`: Flexibility score based on positions played
- `Is1B`: Boolean for first base eligibility
- `Is2B`: Boolean for second base eligibility
- `Is3B`: Boolean for third base eligibility
- `IsSS`: Boolean for shortstop eligibility
- `IsLF`: Boolean for left field eligibility
- `IsCF`: Boolean for center field eligibility
- `IsRF`: Boolean for right field eligibility
- `IsC`: Boolean for catcher eligibility
- `IsP`: Boolean for pitcher eligibility

**Preparation Needed:**
- ⚠️ **Handedness**: Parse from `Player`.
- ⚠️ **Position**: Normalize as above.

---

## Data Dict.txt

**Description:**  
A text file describing the meaning of each variable/column in the CSVs.

---

## **Variables Needing Additional Preparation**

- **Handedness**: Extract from `Player` field for all tables.
- **Player Name**: Remove handedness symbol for all tables.
- **Position**: Normalize position codes, handle multiple positions, and possibly create dummy variables for each position.
- **Pitcher Role**: Normalize for simulation logic (SP, RP, CL).
- **Awards**: May need to be split into a list if multiple awards are present.
- **Player-additional**: Use as a unique player ID for cross-referencing.

---

## **Summary for Simulation**

- **Batting, pitching, and fielding stats**: Core for play-by-play simulation.
- **Handedness and position**: Essential for realistic matchups and lineup logic.
- **Roster and appearances**: Ensure only eligible players are used.
- **Advanced value metrics**: Useful for AI, player ranking, and analytics.
- **Data prep**: Parsing and normalizing these variables is a required step before simulation.

---

## Data Preparation Requirements

- All player names must be cleaned of handedness symbols.
- Handedness must be extracted to a new column (`Handedness`: L, R, S).
- Position columns must be normalized to standard codes; if multiple, select primary or create a list.
- Player IDs (`Player-additional`) must be used for cross-table consistency.
- All numeric/stat columns must be validated as numbers.
- **Stat family/sub-header rows (e.g., `,,,Standard,Standard,...`) are dropped from all cleaned and team totals CSVs. Only the real column header and data rows are retained.**
- **All cleaned and team totals CSVs include:**
  - `Handedness` column
  - `EligiblePositions` (comma-separated)
  - `PositionFlexibility` (count)
  - Dummy variables for each position (e.g., `Is1B`, `Is2B`, ..., `IsDH`, `IsUT`)
- Output files must be one row per player per table, ready for Go struct mapping.

**Note:**  
In the raw CSVs, a stat family/sub-header row (e.g., `,,,Standard,Standard,...`) may appear above the real column header. This row is dropped in all cleaned and team totals CSVs; only the actual column names are retained as the header.

---

**Next Phase Requirement:**  
- Implement a data preparation module to parse, clean, and normalize all variables as described above before using them in the simulation engine.

---

**Author:** Andrew D'Amico
**Email:** Andrew.Damico@u.northwestern.edu

