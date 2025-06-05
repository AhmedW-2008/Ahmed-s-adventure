import time
def start_game():
    print("Welcome to your adventure!")
    time.sleep(2)
    print("You wake up in a garden and don't remember how you got here.")
    print("You have to choose one of two choices:")
    print("1 - shows a house which is very old and has a person lives in it")
    print("2 - shows you a dark cave which has mysterious things ")
    Answer= input("What is your choice? (1 = house / 2 = cave): ")
    if Answer == "1":
       enter_house()
    elif Answer=="2":
        enter_cave()
    else:
        print("Invalid choice. try again.")

def enter_house():
    print("You entered the house and found a person holding a knife.")
    print("You have two choices:")
    print("3 - Attack him")
    print("4 - Defend yourself")
    attack_state = {'counter': 0}
    while True:
        choice = input("Your choice (3 = attack / 4 = defend): ")
        if choice == "3":
            def attack():
                print(f"You attacked! Total attacks: {attack_state['counter']}")
                attack_state['counter'] += 10
                print("you attacked the person, but he was stronger and you lost")
                print("game over")
            # Simulate attack
            attack()
            break
        elif choice == "4":
            print("You defended yourself and escaped to another place.")
            print("You reached an island with a treasure guarded by guardians.")
            print("5 - Join the guardians")
            print("6 - Attack the guardians")
            
            while True:
                choice = input("Your choice (5 = join / 6 = attack): ")
                if choice == "5":
                    print("You joined them and stole the treasure. You won!")
                    break
                elif choice == "6":
                    attack_state['counter'] += 10
                    print(f"You attacked! Total attacks: {attack_state['counter']}")
                    print("You killed most of them, but one survived and killed you.")
                    print("Game over.")
                else:
                    print("Invalid choice. Try again.")
            break

def enter_cave():
    print("You found your friend Amoro who came by time machine.")
    print("He says you must find the time machine to go back.")
    print("You face a monster in the cave.")
    print("7 - Fight the monster")
    print("8 - Run away")
    
    attack_counter = 0

    while True:
        choice = input("Your choice (7 = fight / 8 = run): ")
        if choice == "7":
            def attack():
                nonlocal attack_counter
                attack_counter += 10
                print(f"You attacked! Total attacks: {attack_counter}")
            
            attack()
            print("You fought the monster and won. You escaped! You won!")
            break
        elif choice == "8":
            print("You ran but the monster caught you. You lost.")
            print("Game over.")
        print("would you like to try again?")
        choice = input("your choice (Yes/No):")
        if choice == "yes":
            start_game()
            import random
            random_monsters = ["dragon","mummy","zombie","vampire"]
            random_monster = random.choice(random_monsters)
        elif choice == "no":
           print("thank you for playing")
        else:
            print("end of the game")
            exit ()

if __name__ == "__main__":
    start_game()
