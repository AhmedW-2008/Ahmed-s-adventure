import time

# Ahmed's adventure game
def start_game():
    
    print("welcome to your adventure")
    if __name__ == "__ahmed,s adventure__":
    start_game(ahmed,s adventure) 

    time.sleep(2)
    print("wake up in a garden and you don't remember how you got here")
    print("you have to choose one of two choices")
    print("first choice shows a house which is very old and has a person lives in it")
    print("the second choice shows you a dark cave which has mysterious things ")
    print("you have to choose one of them")
    time.sleep(2)
    choice = input("your choice (1 = house / 2 = cave): ")

    if choice == "1":
        enter_house()
    elif choice == "2":
        enter_cave()
    else:
        print("Invalid choice. Game over.")

def enter_house():
    print("when you entered the house you found a person with a knife")
    print("you have two choices attack him or defend yourself")
    choice = input("your choice 3= attack /4 = defend:")
    if choice == "3":
        attack_counter = 0
        def attack():
        
            print(f"You attacked! Total attacks: {attack_counter}")
            attack_counter += 10
            print("you attacked the person, but he was stronger and you lost")
            print("game over")
        attack()
    elif choice == "4":
        print("you defended yourself and escaped to another place")
        print("you found yourself in an island and you found a treasure but there are guardians ")
        time.sleep(2)
        print("you have to choose one of two choices")
        choice = input("your choice (5= join /6= attack):")
        if choice == "5":
            print("you are now a guardian ")
            print("you stole the treasure and you won")
        elif choice == "6":
            print("you killed them but one of them still alive and he killed you")
            attack_counter = 0  
            def attack():
                
                attack_counter += 10
                print(f"You attacked! Total attacks: {attack_counter}")
            attack()
            print("game over")
        else:
            print("Invalid choice. Game over.")
    else:
        print("Invalid choice. Game over.")

def enter_cave():
    print("when you entered the cave you found his friend amoro")
    print("amoro how did you come here?")
    print("he said I came here by time machine")
    time.sleep(2)
    print("do you know the way to go back?")
    print("yes we should go into the cave and find the time machine")
    print("during the way, they found a monster")
    time.sleep(2)
    print("you have to choose one of two choices")
    choice = input("your choice (7=fight/8 = run away):")
    if choice == "7":
        print("they fought the monster and won")
        print("you won")
    elif choice == "8":
        print("they ran away and found the cave closed, the monster killed them")
        print("game over")
        print("would you like to Try again?")
        choice = input("your choice (yes/no):")
        if choice == "yes":
            def play_again():
    while True
            print("Restarting the game")
            time.sleep(1)
            start_game()
            import random
            random_monsters = ["dragon","mummy","zombie","vampire"]
            random_monster = random.choice(random_monsters)
        elif choice == "no":
            print("thank you for playing")
            exit()
        else:
            print("Invalid choice. Game over.")

print ("end of the game")
