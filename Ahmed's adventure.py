import time
# I used the time module to add delays to make game good
def start_game():
    #this function starts the game and introduces the player to the adventure
    print("Welcome to your adventure!")
    time.sleep(2)
    print("You wake up in a garden and don't remember how you got here.")
    print("You have to choose one of two choices:")
    print("1 - shows a house which is very old and has a person lives in it")
    print("2 - shows you a dark cave which has mysterious things ")
    print("you have 3 lives in your game")
    #number of lives
    lives = 3
    print(f"You have {lives} lives.")
    Answer = input("What is your choice? (1 = house / 2 = cave): ")
    #these are the choices the player can make
    while Answer not in ["1", "2"]:
        print("Invalid choice. Try again.")
        #this loop will keep asking the player for a valid choice
    if Answer == "1":
        enter_house()
        Answer = {'counter':5}
    elif Answer == "2":
        enter_cave()
    Answer = {'counter':5}
    #these are conditions for player if he chooses1,he will enter the house and if he chooses 2, he will enter the cave
def enter_house():
    print("You entered the house and found a person holding a knife.")
    print("You have two choices:")
    print("3 - Attack him")
    print("4 - Defend yourself")
    #this function is for the player to enter the house and face a person with a knife.you can either attack him or defend yourself
    attack_state = {'counter':0 }
    while True:
        choice = input("Your choice (3 = attack / 4 = defend): ")
        while choice not in ["3", "4"]:
            print("Invalid choice. Try again.")
        if choice == "3":
            def attack():
                print(f"You attacked! Total attacks: {attack_state['counter']}")
                attack_state['counter1'] += 20
                attack_state['counter2'] += 5
                score = attack_state['counter']
                if score >= 15:
                    print("You attacked the person and he died. You won!")  
                    lives = 3
                    score = attack_state['counter'] = 20
                    print(f"Total score: {score}")
                if score < 15: 
                    lives = 2
                    print("you attacked the person, but he was stronger and you lost")
                    print("game over")
                    return
            # Simulate attack with a function and shows the score and lives
            attack()
            break
        elif choice == "4":
            choice = {'counter':5}
            print("You defended yourself and escaped to another place.")
            print("You reached an island with a treasure guarded by guardians.")
            print("5 - Join the guardians")
            print("6 - Attack the guardians")
            #simulate defending yourself and escaping to an island with a treasure guarded by guardians and you can either join them or attack them
            while True:
                choice = input("Your choice (5 = join / 6 = attack): ")
                while choice not in ["5", "6"]:
                    print("Invalid choice. Try again.")
                if choice == "5":
                    choice = {'counter':5}
                    print("You joined them and stole the treasure. You won!")
                    lives = 3
                    score = attack_state['counter'] = 20
                    print(f"Total score: {score}")
                    break
                elif choice == "6":
                    attack_state['counter':5]
                    score = attack_state['counter']
                    if score >= 15:
                        print("You attacked the guardians and they were defeated. You won!")
                        lives = 3
                        score = attack_state['counter'] = 20
                        print(f"Total score: {score}")
                        break
                    if score < 15: 
                        print("You attacked the guardians, but they were too strong and you lost.")
                        lives = 2
                        print("Game over.") 
                        return      
                    # Simulate attack with its reults and escape with scores and lives and loop for choices
                    print(f"You attacked! Total attacks: {attack_state['counter']}")
                else:
                    print("Invalid choice. Try again.")
            break

def enter_cave():
    print("You found your friend Amoro who came by time machine.")
    print("He says you must find the time machine to go back.")
    print("You face a monster in the cave.")
    print("7 - Fight the monster")
    print("8 - Run away")
    #this function is for the player to enter the cave and face a monster.you can either fight it or run away
    while True:
        choice = input("Your choice (7 = fight / 8 = run): ")
        while choice not in ["7", "8"]:
            print("Invalid choice. Try again.")
        if choice == "7":
            choice = {'counter':5}
            def attack():
                nonlocal attack_counter
                attack_counter += 20
                print(f"You attacked! Total attacks: {attack_counter}")
            attack()
            score = attack_counter
            if score >= 15:
                print("You fought the monster and won. You escaped! You won!")
                lives = 3
                score = attack_counter=20
                print(f"Total score: {score}")
                break
            if score < 15:
                print("You fought the monster, but it was too strong and you lost.")
                lives = 2
                print("Game over.")
                return
            #simulate fighting the monster with a function and shows the score
        elif choice == "8":
            choice = {'counter':5}
            lives = 2
            print("You ran but the monster caught you. You lost.")
            print("Game over.")
            return
        #it shows that monster caught you and you lost one life and returns .if your lives are 0, the game ends
        while True:
            print("would you like to try again?")
            choice = input("your choice (Yes/No):")
            if choice == "Yes":
                start_game()
                import random
                random_monsters = ["dragon", "mummy", "zombie", "vampire"]
                random_monster = random.choice(random_monsters)
                return
            #i used random module to choose a random monster if the player chooses to try again
            elif choice == "No":
                print("thank you for playing")
                exit()
            else:
                print("Invalid choice. Please enter Yes or No.")
# This loop will keep asking the player for a valid choice.if the player chooses to try again, the game restarts with random monsters else you recieve thank you for playing.
if __name__ == "__main__":
    start_game()
