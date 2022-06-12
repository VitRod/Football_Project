import random

# if  random generates  0 then no  goal,   if  it  generates 1  then there is  a  goal
def  did_they_score():
    shot = random.randint(0, 1)
    if(shot == 0):
        return 0
    elif(shot == 1):
        return  1


def check_for_a_winner(team_one_shots_list, team_two_shots_list):
# we check whether there is  a  winner after  each  kick

# function  sum  calculates  the  total of items  in the  list . It sums  up all the  goals of  players .
    team_one_score = sum(team_one_shots_list)
    team_two_score = sum(team_two_shots_list)

    if(len(team_two_shots_list) < 5) and ((max(team_one_score, team_two_score)) -
                                          min(team_one_score, team_two_score) > (5 - len(team_two_shots_list))):
        if (team_one_score > team_two_score):
            print("Team one  wins {} - {}".format(team_one_score, team_two_score))
            return False
        elif (team_two_score > team_one_score):
            print("Team two  wins {} - {}".format(team_two_score, team_one_score))
            return False
    elif(len(team_one_shots_list) > 5) and ((len(team_two_shots_list) > 5) and ((max(team_one_score, team_two_score)) - min(team_one_score,team_two_score) > 0)):
        if (team_one_score > team_two_score):
            print("Team one  wins {} - {}".format(team_one_score, team_two_score))
            return False
        elif (team_two_score > team_one_score):
            print("Team two  wins {} - {}".format(team_two_score, team_one_score))
            return False

    else:
        # if we  do not  have  winner  in shots penalty
        return True



def simulate_penalty_shootout():
# footballers will kick penalties and  we  will find  out  the  winners  from two teams

    team_1_scores = []
    team_2_scores = []
    game_on = True

# if  random generates  0 then no  goal,   if  it  generates 1  then there is  a  goal
    while(game_on == True):
       # shot = random.randint(0, 1)
       if (check_for_a_winner(team_1_scores, team_2_scores)):
            shot_team_one = did_they_score()
            team_1_scores.append(shot_team_one)
       else:
           break

       if (check_for_a_winner(team_1_scores, team_2_scores)):
            shot_team_two = did_they_score()
            team_2_scores.append(shot_team_two)
       else:
           break

        # game_on = False

    print(team_1_scores)
    print(team_2_scores)

simulate_penalty_shootout()