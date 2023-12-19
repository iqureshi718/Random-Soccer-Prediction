import random

# Define some constants for home advantage and injury impact
HOME_ADVANTAGE = 0.2
INJURY_IMPACT = 0.1

def get_team_info(team_num):
    # Prompt the user for information about a team
    print(f"Please enter information for team {team_num}:")
    team_name = input("Team name: ")
    team_form = float(input("Team form (0-1): "))
    team_injuries = float(input("Team injuries (0-1): "))
    team_home = input("Is the team playing at home (y/n)? ").lower() == "y"
    return {"name": team_name, "form": team_form, "injuries": team_injuries, "home": team_home}

def simulate_match(team1, team2):
    # Simulate a single match between team1 and team2
    # Factors such as team form, player injuries, and home advantage are taken into account
    team1_form = team1["form"]
    team2_form = team2["form"]
    team1_injuries = team1["injuries"]
    team2_injuries = team2["injuries"]
    team1_home = team1["home"]
    team2_home = team2["home"]
    
    # Calculate the impact of team form and player injuries
    team1_strength = (1 - INJURY_IMPACT * team1_injuries) * team1_form
    team2_strength = (1 - INJURY_IMPACT * team2_injuries) * team2_form
    
    # Apply home advantage if applicable
    if team1_home:
        team1_strength += HOME_ADVANTAGE
    elif team2_home:
        team2_strength += HOME_ADVANTAGE
        
    # Simulate the match based on team strengths
    match_result = random.random() * (team1_strength + team2_strength)
    if match_result < team1_strength:
        return team1
    elif match_result > team2_strength:
        return team2
    else:
        return "draw"

def simulate_matches(team1, team2, num_matches):
    # Simulate num_matches matches between team1 and team2
    team1_wins = 0
    team2_wins = 0
    draws = 0
    for i in range(num_matches):
        winner = simulate_match(team1, team2)
        if winner == team1:
            team1_wins += 1
        elif winner == team2:
            team2_wins += 1
        else:
            draws += 1
    return team1_wins, team2_wins, draws

# Prompt the user for information about each team
team1 = get_team_info(1)
team2 = get_team_info(2)

# Simulate 10,000 matches between the two teams
num_matches = 10000
team1_wins, team2_wins, draws = simulate_matches(team1, team2, num_matches)

# Print the results
print(f"{team1['name']} wins:", team1_wins)
print(f"{team2['name']} wins:", team2_wins)
print("Draws:", draws)
print("Odds of", f"{team1['name']}", "wins:",(team1_wins/num_matches)*100),"%"
print("Odds of", f"{team2['name']}", "wins:",(team2_wins/num_matches)*100),"%"
print("Odds of draw:",(draws/num_matches)*100),"%"

# Calculate the odds of winning for each team
total_wins = team1_wins + team2_wins
team1_odds = team1_wins / total_wins
team2_odds = team2_wins / total_wins

# Print the odds of winning
print
