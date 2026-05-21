import os
import fastf1
import pandas as pd


def update_latest_race_results(season=2026):
      """Fetch the latest completed Formula 1 race and save a clean CSV output."""
      script_dir = os.path.dirname(os.path.abspath(__file__))
      cache_dir = os.path.join(script_dir, "cache")
      os.makedirs(cache_dir, exist_ok=True)
      fastf1.Cache.enable_cache(cache_dir)

    schedule = fastf1.get_event_schedule(season)
    completed = schedule[schedule["EventDate"] < pd.Timestamp.today()]

    if completed.empty:
              raise ValueError("No completed races found for the selected season.")

    latest_event = completed.iloc[-1]
    year = latest_event["EventDate"].year
    round_number = latest_event["RoundNumber"]

    session = fastf1.get_session(year, round_number, "R")
    session.load()

    results = session.results[["DriverNumber", "Abbreviation", "Position", "Points"]].copy()
    results["RaceName"] = latest_event["EventName"]
    results["RaceDate"] = latest_event["EventDate"]
    results["Circuit"] = latest_event["Location"]

    output_path = os.path.join(script_dir, "latest_race_results.csv")
    results.to_csv(output_path, index=False)
    print(f"Latest race data saved to {output_path}")


if __name__ == "__main__":
      update_latest_race_results()
  
