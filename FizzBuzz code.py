#Final Game
p = 0
lives = 3
p1_lives = 3
p2_lives = 3
h_counter = 0
h_counter2p = 0
high_count = 0
high_count2p = 0
import time

#Define section
def game_2p():
    global p
    global p1_lives
    global p2_lives
    global h_counter2p
    game_done = False
    n = 0
    while game_done is False:
        game_done = True
        high_score()
        if p == 0:
            input_number = input("Player_1 please Input a number: ")
            p = p + 1
            n = n + 1
            if input_number.isnumeric():
                input_number = int(input_number)
            else:
                input_number = input_number.capitalize()
            #Check
            divisible_3 = False
            if n % 3 == 0:
                divisible_3 = True

            divisible_5 = False
            if n % 5 == 0:
                divisible_5 = True

            if divisible_3 and divisible_5 is True:
                if input_number == "Fizzbuzz":
                    game_done = False
                else:
                    if p1_lives > 1:
                        time.sleep(1)
                        h_counter2p = n - 1
                        high_score2p()
                        print("Incorrect")
                        p1_lives = p1_lives - 1
                        time.sleep(1)
                        print(f"Player_1 has {p1_lives} lives left")
                        n = 0
                        game_done = False
                    else:
                        game_over()

            elif divisible_3 is True:
                if input_number == "Fizz":
                    game_done = False
                else:
                    if p1_lives > 1:
                        time.sleep(1)
                        h_counter2p = n - 1
                        high_score2p()
                        print("Incorrect")
                        p1_lives = p1_lives - 1
                        time.sleep(1)
                        print(f"Player_1 has {p1_lives} lives left")
                        n = 0
                        game_done = False
                    else:
                        game_over()
            elif divisible_5 is True:
                if input_number == "Buzz":
                    game_done = False
                else:
                    if p1_lives > 1:
                        time.sleep(1)
                        h_counter2p = n - 1
                        high_score2p()
                        print("Incorrect")
                        p1_lives = p1_lives - 1
                        time.sleep(1)
                        print(f"Player_1 has {p1_lives} lives left")
                        n = 0
                        game_done = False
                    else:
                        game_over()
            else:
                if n == input_number:
                    game_done = False
                else:
                    if p1_lives > 1:
                        time.sleep(1)
                        h_counter2p = n - 1
                        high_score2p()
                        print("Incorrect")
                        p1_lives = p1_lives - 1
                        time.sleep(1)
                        print(f"Player_1 has {p1_lives} lives left")
                        n = 0
                        game_done = False
                    else:
                        game_over()
        elif p == 1:
            input_number = input("Player_2 please Input a number: ")
            p = p - 1
            n = n + 1
            if input_number.isnumeric():
                input_number = int(input_number)
            else:
                input_number = input_number.capitalize()
            # Check
            divisible_3 = False
            if n % 3 == 0:
                divisible_3 = True

            divisible_5 = False
            if n % 5 == 0:
                divisible_5 = True

            if divisible_3 and divisible_5 is True:
                if input_number == "Fizzbuzz":
                    game_done = False
                else:
                    if p2_lives > 1:
                        time.sleep(1)
                        h_counter2p = n - 1
                        high_score2p()
                        print("Incorrect")
                        p2_lives = p2_lives - 1
                        time.sleep(1)
                        print(f"Player_2 has {p2_lives} lives left")
                        game_done = False
                        n = 0
                    else:
                        game_over()

            elif divisible_3 is True:
                if input_number == "Fizz":
                    game_done = False
                else:
                    if p2_lives > 1:
                        time.sleep(1)
                        h_counter2p = n - 1
                        high_score2p()
                        print("Incorrect")
                        p2_lives = p2_lives - 1
                        time.sleep(1)
                        print(f"Player_2 has {p2_lives} lives left")
                        game_done = False
                        n = 0
                    else:
                        game_over()
            elif divisible_5 is True:
                if input_number == "Buzz":
                    game_done = False
                else:
                    if p2_lives > 1:
                        time.sleep(1)
                        h_counter2p = n - 1
                        high_score2p()
                        print("Incorrect")
                        p2_lives = p2_lives - 1
                        time.sleep(1)
                        print(f"Player_2 has {p2_lives} lives left")
                        game_done = False
                        n = 0
                    else:
                        game_over()
            else:
                if n == input_number:
                    game_done = False
                else:
                    if p2_lives > 1:
                        time.sleep(1)
                        h_counter2p = n - 1
                        high_score2p()
                        print("Incorrect")
                        p2_lives = p2_lives - 1
                        time.sleep(1)
                        print(f"Player_2 has {p2_lives} lives left")
                        game_done = False
                        n = 0
                    else:
                        game_over()

def game_1p():
    global p
    global lives
    global h_counter
    game_done = False
    n = 0
    while game_done is False:
        game_done = True
        p = p + 2
        input_number = input("Please Input a number: ")
        n = n + 1
        if input_number.isnumeric():
            input_number = int(input_number)
        else:
            input_number = input_number.capitalize()
            #Check
        divisible_3 = False
        if n % 3 == 0:
            divisible_3 = True

        divisible_5 = False
        if n % 5 == 0:
            divisible_5 = True

        if divisible_3 and divisible_5 is True:
            if input_number == "Fizzbuzz":
                game_done = False
            else:
                if lives > 1:
                    time.sleep(1)
                    h_counter = n - 1
                    high_score()
                    print("Incorrect")
                    lives = lives - 1
                    time.sleep(1)
                    print(f"You have {lives} lives left")
                    game_1p()
                else:
                    game_over()

        elif divisible_3 is True:
            if input_number == "Fizz":
                game_done = False
            else:
                if lives > 1:
                    time.sleep(1)
                    h_counter = n - 1
                    high_score()
                    print("Incorrect")
                    lives = lives - 1
                    time.sleep(1)
                    print(f"You have {lives} lives left")
                    game_1p()
                else:
                    game_over()
        elif divisible_5 is True:
            if input_number == "Buzz":
                game_done = False
            else:
                if lives > 1:
                    time.sleep(1)
                    h_counter = n - 1
                    high_score()
                    print("Incorrect")
                    lives = lives - 1
                    time.sleep(1)
                    print(f"You have {lives} lives left")
                    game_1p()
                else:
                    game_over()
        else:
            if n == input_number:
                game_done = False
            else:
                if lives > 1:
                    time.sleep(1)
                    h_counter = n - 1
                    high_score()
                    print("Incorrect")
                    lives = lives - 1
                    time.sleep(1)
                    print(f"You have {lives} lives left")
                    game_1p()
                else:
                    game_over()


def game_over():
    global p
    time.sleep(1)
    print("Game OVER")
    time.sleep(1)
    if p == 0:
        print("Player_1 has won the game")
        p = 0
        time.sleep(1)
        menu()

    elif p == 1:
        print("Player_2 has won the game")
        p = 0
        time.sleep(1)
        menu()

    elif p == 2:
        print("You have lost the game")
        p = 0
        time.sleep(1)
        menu()

    else:
        print("You have lost the game")
        p = 0
        time.sleep(1)
        menu()

def high_score():
    global high_count
    global high_count2p
    if high_count < h_counter:
        high_count = h_counter
    elif high_count >= h_counter:
        high_count = high_count
    else:
        print("ERROR")

def high_score2p():
    global high_count2p
    if high_count2p < h_counter2p:
        high_count2p = h_counter2p
    elif high_count2p >= h_counter2p:
        high_count2p = high_count2p
    else:
        print("ERROR")


def game_1p_one():
    global p
    global lives
    global h_counter
    game_done = False
    n = 0
    while game_done is False:
        game_done = True
        p = p + 2
        input_number = input("Please Input a number: ")
        n = n + 1
        if input_number.isnumeric():
            input_number = int(input_number)
        else:
            input_number = input_number.capitalize()
            # Check
        divisible_3 = False
        if n % 3 == 0:
            divisible_3 = True

        divisible_5 = False
        if n % 5 == 0:
            divisible_5 = True

        if divisible_3 and divisible_5 is True:
            if input_number == "Fizzbuzz":
                game_done = False
            else:
                game_over()

        elif divisible_3 is True:
            if input_number == "Fizz":
                game_done = False
            else:
                game_over()

        elif divisible_5 is True:
            if input_number == "Buzz":
                game_done = False
            else:
                game_over()
        else:
            if n == input_number:
                game_done = False
            else:
                game_over()

def game_2p_one():
    global p
    global p1_lives
    global p2_lives
    global h_counter
    game_done = False
    n = 0
    while game_done is False:
        game_done = True
        high_score()
        if p == 0:
            input_number = input("Player_1 please Input a number: ")
            p = p + 1
            n = n + 1
            if input_number.isnumeric():
                input_number = int(input_number)
            else:
                input_number = input_number.capitalize()
            # Check
            divisible_3 = False
            if n % 3 == 0:
                divisible_3 = True

            divisible_5 = False
            if n % 5 == 0:
                divisible_5 = True

            if divisible_3 and divisible_5 is True:
                if input_number == "Fizzbuzz":
                    game_done = False
                else:
                    game_over()

            elif divisible_3 is True:
                if input_number == "Fizz":
                    game_done = False
                else:
                    game_over()
            elif divisible_5 is True:
                if input_number == "Buzz":
                    game_done = False
                else:
                    game_over()
            else:
                if n == input_number:
                    game_done = False
                else:
                    game_over()

        elif p == 1:
            input_number = input("Player_2 please Input a number: ")
            p = p - 1
            n = n + 1
            if input_number.isnumeric():
                input_number = int(input_number)
            else:
                input_number = input_number.capitalize()
            # Check
            divisible_3 = False
            if n % 3 == 0:
                divisible_3 = True

            divisible_5 = False
            if n % 5 == 0:
                divisible_5 = True

            if divisible_3 and divisible_5 is True:
                if input_number == "Fizzbuzz":
                    game_done = False
                else:
                    game_over()

            elif divisible_3 is True:
                if input_number == "Fizz":
                    game_done = False
                else:
                    game_over()
            elif divisible_5 is True:
                if input_number == "Buzz":
                    game_done = False
                else:
                    game_over()
            else:
                if n == input_number:
                    game_done = False
                else:
                    game_over()
                    
def menu():
    time.sleep(1)
    print("======MENU======")
    print("1. Play Game")
    print("2. Rules and Example")
    print("3. Highscores")
    print("4. Exit")
    print("=================")
    time.sleep(1)
    option = int(input("Please input an option: "))
    if option == 1:
        time.sleep(1)
        print("Beginning Game")
        time.sleep(1)
        chosen = False
        while chosen is False:
            chosen = True
            print("======PLAYER======")
            print("1. One Player")
            print("2. Two Players")
            print("3. Back To Menu")
            print("==================")
            time.sleep(1)
            select = int(input("Please Select an option: "))
            if select == 1:
                time.sleep(1)
                print("======GAMEMODE======")
                print("1. Classic")
                print("2. One Life")
                print("====================")
                time.sleep(1)
                pick = int(input("Please Select an option: "))
                if pick == 1:
                    time.sleep(1)
                    game_1p()
                elif pick == 2:
                    time.sleep(1)
                    game_1p_one()
                else:
                    chosen = False
            elif select == 2:
                time.sleep(1)
                print("======GAMEMODE======")
                print("1. Classic")
                print("2. One Life")
                print("====================")
                time.sleep(1)
                pick = int(input("Please Select an option: "))
                if pick == 1:
                    time.sleep(1)
                    game_2p()
                elif pick == 2:
                    time.sleep(1)
                    game_2p_one()
                else:
                    chosen = False
            elif select == 3:
                menu()
            else:
                chosen = False
    elif option == 2:
        time.sleep(1)
        print("======RULES======")
        time.sleep(1)
        print("1. The game is about players taking turns counting up from 1")
        time.sleep(2)
        print("2. The game is recommended to play with two players")
        time.sleep(2)
        print("3. If a number is divisible by 3, the current player should input 'fizz' instead of the number")
        time.sleep(2)
        print("4. If a number is divisible by 5, the current player should input 'buzz' instead of the number")
        time.sleep(2)
        print("5. If a number is divisible by both 3 and 5, the current player should input 'fizz buzz' instead of the number")
        time.sleep(2)
        print("6. If none of the above rules apply, the current player should input the number itself")
        time.sleep(2)
        print("7. When either players incorrectly types a number / word as an input, they lose a life and the game resets back to 0")
        time.sleep(2)
        print("8. Each Player will start with three Lives")
        time.sleep(2)
        print("9. In One Life Mode, Players would only have one life and messing up will regard in an instant game over")
        time.sleep(2)
        print("======EXAMPLE======")
        time.sleep(1)
        print("Player_1 please Input a number: 1")
        time.sleep(1)
        print("Player_2 please Input a number: 2")
        time.sleep(1)
        print("Player_1 please Input a number: fizz (3) so rule is applied therefore 'fizz' is inputted")
        time.sleep(1)
        print("Player_2 please Input a number: buzz (4) the player has inputted a wrong number / word")
        time.sleep(1)
        print("Incorrect")
        time.sleep(1)
        print("Player_2 has 2 lives left (A life is deducted from player two)")
        time.sleep(1)
        print("Player_1 please Input a number: 1 (The game has reset back to zero as player two has made a mistake)")
        print("======END======")
        time.sleep(1)
        menu()
    elif option == 3:
        time.sleep(1)
        print("======HIGHSCORES======")
        print("1. One Player")
        print("2. Two Players")
        print("3. Back To Menu")
        print("======================")
        time.sleep(1)
        choice = int(input("Please enter an option: "))
        if choice == 1:
            time.sleep(1)
            print(f"Highest number reached is {high_count}")
            menu()
        elif choice == 2:
            time.sleep(1)
            print(f"Highest number reached is {high_count2p}")
            menu()
        elif choice == 3:
            menu()
        else:
            print("ERROR")
            menu()
    elif option == 4:
        time.sleep(1)
        print("Exiting Game")
        time.sleep(1)

#CALLED
menu()