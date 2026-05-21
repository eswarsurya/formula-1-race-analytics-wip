import os
import fastf1
import pandas as pd

# Fetch the latest completed Formula 1 race and save a clean CSV output.
SEASON = 2026
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CACHE_DIR = os.path.join(SCRIPT_DIR, "cache")
os.makedirs(CACHE_DIR, exist_ok=True)
fastf1.Cache.enable_cache(CACHE_DIR)

schedule = fastf1.get_event_schedule(SEASON)
completed = schedule[schedule["EventDate"] < pd.Timestamp.today()]
latest_event = completed.iloc[-1]

year = latest_event["EventDate"].year
round_number = latest_event["RoundNumber"]

session = fastf1.get_session(year, round_number, "R")
session.load()

results = session.results[["DriverNumber", "Abbreviation", "Position", "Points"]].copy()
results["RaceName"] = latest_event["EventName"]
results["RaceDate"] = latest_event["EventDate"]
results["Circuit"] = latest_event["Location"]

output_path = os.path.join(SCRIPT_DIR, "latest_race_results.csv")
results.to_csv(output_path, index=False)
print(f"Latest race data saved to {output_path}")
