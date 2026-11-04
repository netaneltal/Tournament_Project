def menu():
    print(f"========== TOURNAMENT MANAGER ==========")
    print("1. Add team")
    print("2. Show all teams")
    print("3. Add match result")
    print("4. Show standings")
    print("5. Show leading team")
    print("6. Show best attacking team")
    print("7. Show team success rate")
    print("8. Show teams without wins")
    print("9. Show tournament summary")
    print("10. Check championship potential")
    print("0. Exit") 

teams = [{
            "id": 11,"name": "b", "played": 0,
            "wins": 0, "draws": 0, "losses": 0,
            "goals_for": 7, "goals_against": 0, "points": 10
            },{
            "id": 22,"name": "a", "played": 0,
            "wins": 0, "draws": 0, "losses": 0,
            "goals_for": 10, "goals_against": 0, "points": 10
            }]
matches = [{"home_team_id": 1,"away_team_id": 2,
            "home_goals": 3,"away_goals": 1}]

def add_team(id,name):
    team = {
            "id": 0,"name": "0", "played": 0,
            "wins": 0, "draws": 0, "losses": 0,
            "goals_for": 0, "goals_against": 0, "points": 0
            }
    team["id"]= id
    team["name"]= name
    teams.append(team)

def add_matche(home_team_id,home_goals,away_team_id,away_goals):
   matche = {"home_team_id": 0,"away_team_id": 0,
            "home_goals": 0,"away_goals": 0}   
   matche["home_team_id"] = home_team_id
   matche["home_goals"] = home_goals
   matche["away_team_id"] = away_team_id
   matche["away_goals"] = away_goals
   matches.append(matche)

def show_teams():
   if teams == []:
      print("No teams to display")
   else:   
    print(teams) 

def match_update(home_team_id,home_goals,away_team_id,away_goals):
    goals_home = home_goals 
    goals_away = away_goals    
    for team in teams:
      if team["id"] == home_team_id:
         team["goals_for"] += home_goals
         team["played"] += 1
         team["goals_against"] += away_goals
         if goals_home > goals_away:
            team["wins"] += 1
            team["points"] += 3
         elif goals_home == goals_away: 
            team["draws"] += 1
            team["points"] += 1
         else:
            team["losses"] += 1
      elif team["id"] == away_team_id:
         team["goals_for"] += away_goals 
         team["played"] += 1
         team["goals_against"] += home_goals
         if goals_home < goals_away:
            team["wins"] += 1
            team["points"] += 3
         elif goals_home == goals_away: 
            team["draws"] += 1
            team["points"] += 1
         else:
            team["losses"] += 1

def success_rate():
   for team in teams:
      if team["played"] == 0:
         print(f"{team["name"]}:No teams to display") 
      else:
        success = (100 * team["points"]) // (3 * team["played"])
        print(f"name:{team["name"]} success rate{success}%")           
   
def without_wins():
   for team in teams:
      if team["played"] > 0 and team["wins"] == 0:
         print(f"name:{team["name"]} Number of games:{team["played"]} number of points:{team["points"]}")

            
def ranking_Table():
   points = sorted(teams,key=lambda p:(p["points"],p["goals_for"]-p["goals_against"],p["goals_for"]),reverse=True)
   for team in points:
      print(team)


def leading_team():
    if matches == False:
       print("There is no leading group yet.")
    else:   
     points = sorted(teams,key=lambda p:(p["points"],p["goals_for"]-p["goals_against"],p["goals_for"]),reverse=True)
     print(points[0])


def best_attacking():
   goals = sorted(teams,key=lambda p:(p["goals_for"]),reverse=True)
   must_goals = goals[0] 
   best_attacking_team = []
   for team in teams:
      if team["goals_for"] == must_goals["goals_for"]:
         best_attacking_team.append(team)
   print(best_attacking_team)
def total_goals():
   total = 0
   for goal in teams:
      total += goal["goals_for"]
   return total 

def average_goals(goal):
   mat = 0
   avg = goal
   for m in matches:
      mat += 1 
   return avg / mat

def total_draw():
   total = 0
   for d in teams:
      total += d["draws"]
   return total // 2   
                

def tournament_summary():
   print(f"Number of teams: {len(teams)}")
   print(f"Number of games: {len(matches)}")
   print(f"Total number of goals: {total_goals()}")
   print(f"Average goals per game: {average_goals(total_goals())}")
   print(f"Number of games that ended in a draw: {total_draw()}")
   leading_team()


def choice():
    while True:
     menu()      
     menu_choice = input("Choose an option: ")
     if menu_choice == "1":
        id = int(input("enter id:"))
        name = input("enter a name:")
        add_team(id,name)
        print(teams)
     elif menu_choice == "2": 
        show_teams()  
     elif menu_choice == "3":
        print(matches)
        home_team_id = int(input("home_team_id"))
        home_goals = int(input("home_goals"))
        away_team_id = int(input("away_team_id"))
        away_goals = int(input("away_goals"))
        add_matche(home_team_id,home_goals,away_team_id,away_goals)
        match_update(home_team_id,home_goals,away_team_id,away_goals)
        print(matches)
     elif menu_choice == "4":
        ranking_Table()   
     elif menu_choice == "5":
        leading_team()
     elif menu_choice == "6":
        best_attacking()
     elif menu_choice == "7": 
        success_rate() 
     elif menu_choice == "8":
        without_wins()  
     elif menu_choice == "9":
        tournament_summary()
     elif menu_choice == "0":  
        exit()   
     else:
        print("Please enter a number between 1 and 10; press 0 to exit.")   

choice()
        

