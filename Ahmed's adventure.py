import time
import random
# I used the time and random modules to make game good
hearts = 3
score = 0
def start_game():
    global hearts, score
    hearts = 3  # number of hearts at the beginning
    score = 0  #  score at the beginning
    #this function starts the game and introduces the player to the adventure
    print("Welcome to your adventure!")
    time.sleep(2)
    print("You wake up in a garden and don't remember how you got here.")
    print("You have to choose one of two choices:")
    print("1 - shows a house which is very old and has a person lives in it")
    print("2 - shows you a dark cave which has mysterious things ")
    Answer = input("What is your choice? (1 = house / 2 = cave): ")
    #these are the choices the player can make
    if Answer == "1":
        enter_house()
    elif Answer == "2":
        enter_cave()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        return
def enter_house():
    global hearts,score
    print("You entered the house and found a person holding a knife.")
    print("You have two choices:")
    print("3 - Attack him")
    print("4 - Defend yourself")
    #this function is for the player to enter the house and face a person with a knife.you can either attack him or defend yourself
    attack_counter = 0
    while True:
        choice = input("Your choice (3 = attack / 4 = defend): ")
        if choice == "3":
            # Simulate attack
            def attack():
                nonlocal_attack_counter = attack_counter + 20
                print(f"You attacked! Total attacks: {nonlocal_attack_counter}")
                return nonlocal_attack_counter
            attack_counter = attack()
            score = attack_counter
            if score >= 15:
                print("You attacked the person and he died. You won!")  
                print("Hearts left: 3 hearts")
                score = attack_counter = 20
                print(f"Total score: {score}")
                break
        elif score < 15: 
            print("you attacked the person, but he was stronger and you lost")
            hearts -= 1
            print(f"Hearts left: {hearts} hearts")
            if hearts <= 0:
                print("You lost all your hearts. Game Over!")
            elif hearts > 0:
                print("You're still alive!")
            
            
            while True:
                choice = input("Would you like to play again? (Yes/No): ")
                if choice == "Yes":
                    start_game()
                    break
                elif choice == "No":
                    print("Thank you for playing!")
                    exit()
                else:
                    print("Invalid choice. Please enter Yes or No.")
                    return
        elif choice == "4":
         print("You defended yourself and escaped to another place.")
        print("You reached an island with a treasure guarded by guardians.")
        print("5 - Join the guardians")
        print("6 - Attack the guardians")
        #simulate defending yourself and escaping to an island with a treasure guarded by guardians and you can either join them or attack them
        attack_state = {'counter': 0}
        while True:
            choice = input("Your choice (5 = join / 6 = attack): ")
            if choice == "5":
                print("You joined them and stole the treasure. You won!")
                score = attack_state['counter'] = 20
                print(f"Total score: {score}")
                break
            elif choice == "6":
                attack_state['counter'] += 20
                score = attack_state['counter']
                if score >= 15:
                    print("You attacked the guardians and they were defeated. You won!")
                    score = attack_state['counter'] = 20
                    print(f"Total score: {score}")
                    break
                elif score < 15: 
                    print("You attacked the guardians, but they were too strong and you lost.")
                    hearts -= 1
                    print(f"Hearts left: {hearts} hearts")
            if hearts <= 0:
                print("You lost all your hearts. Game Over!")
            else:
                print("You're still alive!")
        
            return      
            # Simulate attack with its results and escape with scores and lives and loop for choices


def enter_cave():
    global hearts, score
    print("You found your friend Amoro who came by time machine.")
    print("He says you must find the time machine to go back.")
    print("You face a monster in the cave.")
    monster = random.choice(["dragon", "mummy", "zombie", "vampire"])
    print("7 - Fight the monster")
    print("8 - Run away")
    #this function is for the player to enter the cave and face a monster.you can either fight it or run away
    while True:
        choice = input("Your choice (7 = fight / 8 = run): ")
        if choice == "7":
            attack_counter = 0
            def attack():
                local_attack_counter = attack_counter + 20
                print(f"You attacked! Total attacks: {local_attack_counter}")
                return local_attack_counter
            attack_counter = attack()
            score = attack_counter
            if score >= 15:
                print("You fought the monster and won. You escaped! You won!")
                hearts = 3  # Reset hearts after winning
                score = attack_counter = 20
                print(f"Total score: {score}")
                break
            if score < 15:
                print("You fought the monster, but it was too strong and you lost.")
                hearts -= 1
                print(f"Hearts left: {hearts} hearts")
            if hearts <= 0:
                print("You lost all your hearts. Game Over!")
            else:
                print("You're still alive!")
                return
            #simulate fighting the monster with a function and shows the score
        elif choice == "8":
            hearts -= 1
            print("You ran but the monster caught you. You lost.")
            print(f"Hearts left: {hearts} hearts")
            if hearts <= 0:
                print("You lost all your hearts. Game Over!")
            elif hearts > 0:
                print("You're still alive!")
            return
        #it shows that monster caught you and you lost one life and returns .if your lives are 0, the game ends
        else:
            print("Invalid choice. Try again.")
            return
        while True:
            print("would you like to try again?")
            choice = input("your choice (Yes/No):")
            if choice == "Yes":
                start_game()
            elif choice == "No":
                print("thank you for playing")
                exit()
            else:
                print("Invalid choice. Please enter Yes or No.")
                return
# This loop will keep asking the player for a valid choice.if the player chooses to try again, the game restarts with random monsters else you recieve thank you for playing.
if __name__ == "__main__":
    start_game()
