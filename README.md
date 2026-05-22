# Formula 1 Race Analytics - Work In Progress

Active analytics project exploring Formula 1 race results, driver performance, constructor standings, qualifying outcomes, pit stops, sprint results, and generated latest-race updates.

## Why I Built This

I built this project to turn a personal interest in Formula 1 into a practical analytics workflow using Python, FastF1, CSV data modelling, and Power BI. It is intentionally marked as work in progress because I am still improving the dashboard story, adding analysis pages, and expanding the project outputs.

## Analytics Questions

- What does the latest generated race output show for driver position and points?
- Which historical Formula 1 tables are useful for dashboard modelling?
- How can race results, qualifying, pit stops, driver standings, and constructor standings be connected for analysis?
- What early summaries can support a Power BI dashboard?
- How can a live sports interest be converted into a repeatable analytics workflow?

## Tools Used

Python, FastF1, Pandas, Power BI, CSV data modelling, and sports analytics.

## What I Implemented

The project includes a FastF1 refresh script for generated latest-race output, Formula 1 data inventory notes, latest race result outputs, early pit-stop and race-status summaries, dashboard planning notes, and aggregate visuals. The local project also includes a Power BI dashboard file that can be uploaded later after checking embedded data and file size.

## Repository Guide

| Path | Purpose |
|---|---|
| `src/` | FastF1 refresh script for latest generated race output. |
| `data/` | Formula 1 data notes and modelling context. |
| `outputs/` | Dataset inventory, latest race results, race-count summaries, result statuses, and pit-stop output. |
| `dashboards/` | Power BI dashboard direction and sharing notes. |
| `reports/` | Current WIP project status and next improvements. |
| `assets/` | Public-facing visuals for quick project review. |
| `requirements.txt` | Python libraries required for the refresh workflow. |

## Current Public Evidence

- FastF1 refresh script.
- Latest generated race results CSV.
- Compact latest-race points output.
- Dataset inventory across core Formula 1 tables.
- Recent season race-count summary.
- Top result-status summary.
- Early pit-stop analysis output.
- Dashboard evidence guide.
- Project status notes.
- Visual summaries for race points and dataset inventory.

## Outputs And Results

The current output demonstrates that the project is more than an idea: it has a working data refresh direction, committed CSV outputs, summary tables, and dashboard planning. The latest generated output in the repository is for the Japanese Grand Prix at Suzuka, with points and race-position data prepared for analysis.

## Project Walkthrough

A good way to explore this project is to start with `outputs/race_analytics_output_summary.md`, then review `src/update_latest_race_results.py`, `outputs/dataset_inventory.csv`, and `reports/project_status.md`. The project is designed to show self-directed learning, data refresh scripting, and dashboard development around a live sports analytics topic.

## Next Improvements

Planned improvements include dashboard screenshots, driver and constructor trend pages, race-by-race comparisons, a notebook version for easier review, and clearer Power BI data model notes.

## Project Notes

This project shows curiosity, self-directed learning, and the ability to build analytics around a live subject area. It is not presented as a finished production dashboard yet; it is a visible active project with current outputs and a clear improvement path.
