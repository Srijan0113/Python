from requests import get #Used to make HTTP GET requests to APIs (like fetching cricket match data).
from pprint import PrettyPrinter #PrettyPrinter: A utility to pretty-print Python objects (dictionaries, lists) in a readable way.
import time 

BASE_URL = "https://api.cricapi.com/v1"
API_KEY = "badbe253-d1d6-4c3e-943c-8cf1a80bd441"
UPCOMING_URL = f"{BASE_URL}/currentMatches?apikey={API_KEY}"
PAST_URL = f"{BASE_URL}/matches?apikey={API_KEY}&status=completed"

#An API is a set of rules that allows one software/application to talk to another.Think of it as a messenger between two programs.


printer = PrettyPrinter()

def get_all_matches(url):
    try:
        response = get(url)
        response.raise_for_status()
        data = response.json() #JSON is a lightweight format to store and exchange data. It’s easy for humans to read and write, and easy for machines to parse and generate.
        # Structure:
        # JSON represents data as key-value pairs.

        return data.get("data", [])
    except Exception as e:
        print("Error fetching data:", e)
        return []

    #The try-except ensures the program is robust and can handle network/API issues gracefully.Without it, a single failed request could stop the entire cricket tracker.
    
def get_country_list(matches):
    """Return a sorted list of unique country/team names from matches."""
    countries = set()
    for match in matches:
        team_info = match.get("teamInfo", [])
        for team in team_info:
            name = team.get("name", "")
            if name:
                countries.add(name)
    return sorted(countries)

def get_required_matches(matches,country,completed_only=False):
    required_matches = []

#     match = {
#     "teamInfo": [
#         {"name": "India"},
#         {"name": "Australia"}
#     ]
# }

    # team1 = match.get("teamInfo", [{}])[0].get("name", "")  # "India"
    # team2 = match.get("teamInfo", [{}])[1].get("name", "")  # "Australia"


    for match in matches:
        team1 = match.get("teamInfo", [{}])[0].get("name", "")
        team2 = match.get("teamInfo", [{}])[1].get("name", "")
        status = match.get("status", "").lower()
        if country.lower() in team1.lower() or country.lower() in team2.lower():
            if completed_only:
                if "not started" in status or "upcoming" in status:
                    continue  # Skip matches that haven’t started
            required_matches.append(match)

    return required_matches

def show_match_details(matches,title):
    print(f"\n=== {title} ===")
    if not matches:
        print(f"No matches found right now.")
        return

    for m in matches:
        print(m.get("name", "Unknown Match"))
        print("Date:", m.get("date", "N/A"))
        print("Venue:", m.get("venue", "N/A"))
        print("Teams:", ", ".join([t.get("name", "") for t in m.get("teamInfo", [])]))
        print("Status:", m.get("status", "N/A"))
        print("-" * 60)


def fetch_scorecard(match_id):
    """Fetch the scorecard of a specific match by match ID."""
    url = f"{BASE_URL}/scorecard?apikey={API_KEY}&id={match_id}"
    try:
        response = get(url)
        response.raise_for_status()
        data = response.json()
        return data.get("data", {})  # Returns the detailed score info
    except Exception as e:
        print("Error fetching scorecard:", e)
        return {}
    
def display_scorecard(scorecard):
    """Display basic scoreboard information."""
    if not scorecard:
        print("No scorecard available.")
        return

    # Team names
    teams = [t.get("name","") for t in scorecard.get("teamInfo",[])]
    print("Teams:", " vs ".join(teams))

    # Current score(s)
    for inning in scorecard.get("innings", []):
        print(f"\n{inning.get('battingTeam','')} Innings")
        print("Score:", inning.get("runs","N/A"), "/", inning.get("wickets","N/A"))
        print("Overs:", inning.get("overs","N/A"))
        
        # Top batsmen
        print("Batsmen:")
        for batsman in inning.get("batsmen", []):
            print(f"  {batsman.get('name','')} - {batsman.get('runs','')} ({batsman.get('balls','')} balls)")

        # Top bowlers
        print("Bowlers:")
        for bowler in inning.get("bowlers", []):
            print(f"  {bowler.get('name','')} - {bowler.get('overs','')} overs, {bowler.get('runs','')} runs, {bowler.get('wickets','')} wickets")



def main():
    print("Welcome to the Cricket Match Tracker!")
    
    
    # Fetch upcoming matches
    upcoming_matches = get_all_matches(UPCOMING_URL)
    countries = get_country_list(upcoming_matches)

    print("\nAvailable countries or teams in upcoming matches:")
    for idx, country in enumerate(countries, 1):
        print(f"{idx}. {country}")
    country = input("Enter country name or team name : ").strip()
    upcoming_filtered = get_required_matches(upcoming_matches, country,completed_only=False)
    show_match_details(upcoming_filtered, f"Upcoming Matches for {country}")
    time.sleep(10)

    # Fetch recently played matches
    past_matches = get_all_matches(PAST_URL)
    countries = get_country_list(past_matches)

    print("\nCountries/Teams with recent matches:")
    for idx, country in enumerate(countries, 1):
        print(f"{idx}. {country}")
    country = input("Enter country name or team name : ").strip()
    past_filtered = get_required_matches(past_matches, country,completed_only=True)
    show_match_details(past_filtered, f"Recently Played Matches for {country}")

    for match in past_filtered:  # or past_filtered
      match_id = match.get("id")
      if match_id:
        # Fetch and show scoreboard
        scorecard = fetch_scorecard(match_id)
        display_scorecard(scorecard)
        print("-"*60)


   
   

if __name__ == "__main__":
    main()



