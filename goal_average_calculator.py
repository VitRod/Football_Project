

# This is  a  dictionary  of dictionaries
database_of_players = {
"Salah": {"name": "Mo Salah", "games_2018": 38, "goals_2018": 22},
"Kane": {"name": "Harry Kane", "games_2018": 28, "goals_2018": 17},
"Aguero": {"name": "Sergio Aguero", "games_2018": 33, "goals_2018": 21},
"Lukaku": {"name": "Romelu Lukaku", "games_2018": 32, "goals_2018": 12},
"Aubameyang": {"name": "Pierre-Emerick Aubameyang", "games_2018": 26, "goals_2018": 17},
"Mane": {"name": "Sadio Mané", "games_2018": 36, "goals_2018": 22},
"Vardy": {"name": "Jamie Vardy", "games_2018": 34, "goals_2018": 18},
"Sterling": {"name": "Raheem Sterling", "games_2018": 34, "goals_2018": 17},
"Hazard": {"name": "Eden Hazard", "games_2018": 37, "goals_2018": 16}
}


def calculate_goal_average(games, goals):
# calculating average  value  concerning  goals per game of  players

    players_goal_average = round(goals/games, 2)  # we  round  number  to 2  numbers  after  comma
    return (players_goal_average)

# Printing names of players from database
for player in database_of_players.keys():
    print(player)

# Names  of  players  from the  list
player_one_name = input("Select player one from the list \n")
player_two_name = input("Select player one from the list \n")

# average  value  concerning  goals of  players
player_one_goal_average = calculate_goal_average(database_of_players[player_one_name]["games_2018"],
                                                 database_of_players[player_one_name]["goals_2018"])
player_two_goal_average = calculate_goal_average(database_of_players[player_two_name]["games_2018"],
                                                 database_of_players[player_two_name]["goals_2018"])

print("Welcome to my my  goal  comparison  tool:\n")

# printing  player's goal average value per  game
print('{} has a goal average of {} goals per game'.format(player_one_name, player_one_goal_average))
print('{} has a goal average of {} goals per game'.format(player_two_name, player_two_goal_average))

# finding out what  player  is more prolific goal scorer
if (player_one_goal_average > player_two_goal_average):
    print('{} ({}) is a  more prolific goal scorer than {} ({})'.format(player_one_name, player_one_goal_average,
                                                                        player_two_name, player_two_goal_average))
elif (player_two_goal_average > player_one_goal_average):
    print('{} ({}) is a  more prolific goal scorer than {} ({})'.format(player_two_name,
                                                                        player_two_goal_average,
                                                                        player_one_name,
                                                                        player_one_goal_average))
else:
    print("{} ({}) is  equally good as {} ({})".format(player_one_name,
                                                       player_one_goal_average,
                                                       player_two_name,
                                                       player_two_goal_average))



















