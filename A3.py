
import random
random.seed(30)

def main():
    display_banner()
    play_game()

def play_game():
    player_num = 1
    game_finished = False
    coins_list = create_coins_list()
    while game_finished == False:
        display_coins_list(coins_list)
        print("PLAYER NUMBER: " + str(player_num))
        position_num = get_position_number_from_user()
        if validate_index(coins_list, position_num):
            move_num = get_number_places_to_move()
            if validate_move(coins_list, position_num, move_num):
                move_dollar_to_the_left(coins_list, position_num, move_num)
                game_finished = check_game_finished(coins_list)
                if game_finished:
                     congratulate_player(player_num)
            else:
                print("ERROR: Invalid move!")
        else:
            print("ERROR: Invalid position number!")
        player_num = get_next_player_num(player_num)
    
def display_banner():
    #complete this
    print("*"*15)
    print("COIN STRIP GAME")
    print("*"*15)
def get_position_number_from_user():
    #complete this
    position_number=input("Enter position number of coin: ")
    return int(position_number)
def get_number_places_to_move():
    #complete this
    move_num=input("Enter number of places to move coin: ")
    return int(move_num)
def get_next_player_num(player_number):
    #complete this
    if player_number==1:
        return 2
    else:
        return 1
def congratulate_player(player_number):
    #complete this
    print("=============================")
    print("** Y O U   H A V E   W O N **")
    print("       PLAYER NUMBER:",player_number)
    print("=============================")   
def display_coins_list(coins_list):
    #complete this
    print("123456789")
    print("-"*9)
    third_line=""
    for item in coins_list:
        third_line+=item
    print(third_line)
def check_game_finished(coins_list):
    #complete this
    check=[]
    for i in range(0,4):
        check.append(coins_list[i])
    if check==['$','$','$','$']:
        return True
    else:
        return False
def move_random_character_to_end(coins_list):
    #complete this
    random_position=random.randrange(0,len(coins_list))
    random_char=coins_list[random_position]
    coins_list.pop(random_position)
    coins_list.append(random_char)
    return coins_list
def create_coins_list():
    #complete this
    coins_list=['-', '$', '-', '$', '-', '$', '-', '$', '-']
    coins_list=move_random_character_to_end(coins_list)
    coins_list=move_random_character_to_end(coins_list)
    coins_list=move_random_character_to_end(coins_list)
    coins_list=move_random_character_to_end(coins_list)
    return coins_list
def validate_move(coins_list, position_number, to_move):
    #complete this
    new_position=position_number-1-to_move
    if new_position<0:
        return False
    if coins_list[new_position]!="$":
        for index in range(new_position,position_number-1):
            if coins_list[index]=="$":
                return False
        return True
    else:
        return False

def validate_index(coins_list, position_number):
    #complete this
    if position_number>=1 and position_number<=9:
        index=position_number-1
        if coins_list[index]=="$":
            return True
        else:
            return False
    else:
        return False
def move_dollar_to_the_left(coins_list, position_number, to_move):
    #complete this 
    new_position=position_number-1-to_move
    coins_list[position_number-1]="-"
    coins_list[new_position]="$"
    return coins_list
    
main()
