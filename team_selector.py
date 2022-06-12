import  random


# 12 names of  players
our_players = ["Andy", "Becks", "Chris", "Dave", "Eggy", "Fudge", "Goosey", "Harry", "Izzie", "Johnno", "Kev", "Mo"]


def pick_the_teams(list_of_players):
# creating two teams  by  choosing  players  from the  list .

    team_blue_shirts = []
    team_red_shirts = []
# round of random choosing  of 6 players  from the  list  to a  team
    for team_choice_round in range(1, 7):
        # captain of  first  team takes  a  choice  of  player from the  list
        first_choice = random.choice(list_of_players)
        # to avoid  repetitions  of  players  we use  function  remove()
        list_of_players.remove(first_choice)
        # captain of  second  team takes  a  choice  of  player from the  list
        second_choice = random.choice(list_of_players)
        list_of_players.remove(second_choice)
        
        # adding players to team lists
        team_blue_shirts.append(first_choice)
        team_red_shirts.append(second_choice)

    return team_blue_shirts, team_red_shirts




def  this_is_my_main_program():



    team_blue_shirts, team_red_shirts = pick_the_teams(our_players)

# 1st  variant
    # sentences = ["Matchday Team Sheet\n",
    #              "Date\n\n",
    #              "Team in Blue Shirts\n",
    #              "{}\n\n".format(team_blue_shirts),
    #              "Team in Red Shirts\n"
    #              "{}".format(team_red_shirts),
    #              ]

    # my_document = open("team_list.txt", "w")
    # my_document.writelines(sentences)
    # my_document.close()

#2nd  variant
    # file  openning
    my_document = open("team_list.txt", "w")
    # writing the string  to the the  file
    my_document.write("Matchday Team Sheet\n")
    my_document.write("Date\n\n")
    my_document.write("Team in Blue Shirts\n")
    # writing players  from the  list to the  team
    for player in team_blue_shirts:
        my_document.write(player + "\n")

    my_document.write("\nTeam in Red Shirts\n")
    for player in team_red_shirts:
        my_document.write(player + "\n")

    my_document.close()

    print(team_blue_shirts)
    print(team_red_shirts)

this_is_my_main_program()






