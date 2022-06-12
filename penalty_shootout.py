import csv


def check_target_area(this_is_list):
# we will go through the list  of  data and  find out the  area in the football gate the  player  got  the  most  shots

    list_of_most_shots = []

    for player_shots in this_is_list:
        the_most_shots = max(player_shots[1:7])
        area_with_most_shots = player_shots.index(the_most_shots)
        list_of_most_shots.append(area_with_most_shots)

   # print(list_of_most_shots)
    return list_of_most_shots

############################################# 
def translate_our_codes(bunch_of_codes):
    list_of_translations = []
    for code in bunch_of_codes:
        if(code == 1):
            list_of_translations.append("Top right corner")
        elif (code == 2):
            list_of_translations.append("Middle right ")
        elif (code == 3):
            list_of_translations.append("Bottom right corner")
        elif(code == 4):
            list_of_translations.append("Top center")
        elif (code == 5):
            list_of_translations.append("Middle center ")
        elif (code == 6):
            list_of_translations.append("Bottom center")
        elif (code == 7):
            list_of_translations.append("Top left corner")
        elif (code == 8):
            list_of_translations.append("Middle left")
        elif(code == 9):
            list_of_translations.append("Bottom left corner")
        else:
            list_of_translations.append("Not Applicable")

    return list_of_translations



def this_is_my_main_program():
# openning file and  reading this  file. Then adding goalkeepers and  their  names to the  lists. 
# Translating number data from code  to text. and  printing  of goalkeepers and the  gate  areas of  kicks .

    penalty_takers_document = open("penalty_kick_data.csv")
    player_stats = csv.reader(penalty_takers_document)

    list_of_penalty_kick_takers = []

    for line in player_stats:
        list_of_penalty_kick_takers.append(line)
        
   # check_target_area(list_of_penalty_kick_takers) # we check the  gate area with maximum kicks
   # print(list_of_penalty_kick_takers)

    names_of_penalty_kick_takers =[]
    for item in list_of_penalty_kick_takers:
        names_of_penalty_kick_takers.append(item[0])
   # print(names_of_penalty_kick_takers)


    area_of_kicks =  translate_our_codes(check_target_area(list_of_penalty_kick_takers))

# printing names  of goalkeepers and  areas where footballers kick
    for x in range(0, len(names_of_penalty_kick_takers)):
        print("{} - {}".format(names_of_penalty_kick_takers[x], area_of_kicks[x]))



   # print(list_of_penalty_kick_takers)
   # check_target_area(list_of_penalty_kick_takers)


this_is_my_main_program()

