import random

Names = ["Alex", "Edward", "Warren", "Broderick", "Jerrold", "Claudio", "Carlton", "Hyman", "Brendon", "Isaac", "Prince", "Shelton", "Willian", "Dirk", "Leandro", "Vito", "Deandre", "Columbus", "Barton", "Mary", "Chance", "Clinton", "Rhett", "Justin", "Alec", "Morton", "Abel", "Robin", "Dewitt", "Emory", "Son", "Wilber", "Winston", "Max", "Weston", "Mitchell", "Deshawn", "Vincent", "Lino", "Orval", "Stanley", "Patricia", "Theron", "Chadwick", "German", "Eduardo", "Ramon", "Freeman", "Rex", "Ken"]


def generate_players_for_teams(list_of_players):
# choosing players from the  list  to the  teams
    team = []
    for x in range(0, 11):
        team.append(random.choice(list_of_players))
    #print(team)
    return team

#generate_players_for_teams(Names)


class Team:
    league = "English Premier League"
    tv_money = 10000   # money teams  receive  for  one  game
    number_of_teams = 0

    def __init__(self, team_name, stadium, manager_name, finances, players):
        self.team_name = team_name
        self.stadium = stadium
        self.manager_name = manager_name
        self.finances = finances
        self.players = players

        Team.number_of_teams += 1

    def stadium_display(self):
        return ("{} - {}".format(self.team_name, self.stadium))

    def apply_tv_money(self):
        self.finances =  self.finances + self.tv_money


# class Women_Team(Team):
#     tv_money = 20000
#
#     def __init__(self, team_name, stadium, manager_name, finances, assistant_manager):
#         super().__init__(team_name, stadium, manager_name, finances)
#         self.assistant_manager = assistant_manager


#creating instances of  classes
ManCity = Team("Manchester City", "Etihad", "Pep Guardiolo", 999999999, generate_players_for_teams(Names))
Liverpool = Team("Liverpool", "Anfield", "Jurgen Klopp", 500000000, generate_players_for_teams(Names))

# print(ManCity.finances)
# print(Liverpool.manager_name)
#
# print(ManCity.stadium_display())
# print(Liverpool.stadium_display())

# Liverpool.tv_money = Liverpool.tv_money * 1.10  # Liverpool receives 10% more after each  game from tv providers
# print(Liverpool.finances)
# Liverpool.apply_tv_money()
# print(Liverpool.finances)

# if  we will make  more  instances  of  teams there  will be not 2  but more  teams
#print(Team.number_of_teams)

# ManCity_Women = Women_Team("Manchester City Women", "Etihad", "Jane Doe", 10000, "Lucy Lake")

# print(ManCity_Women.finances)
# ManCity_Women.apply_tv_money()
# print(ManCity_Women.finances)

# print(ManCity_Women.assistant_manager)

print(ManCity.players)
print(Liverpool.players)










