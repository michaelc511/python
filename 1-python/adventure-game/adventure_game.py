# Adventure Game - A text-based quest to find treasure in an ancient land
# Using GitHub Copilot to assist in writing and optimizing code

print("Adventure Game Setup Complete!")

# main game loop

def start_game():
    while True:
        print("\nWelcome to the Adventure Game!")
        player_name = input("Please enter your name: ")
        print(f"Hello, {player_name}! Your quest is to find the legendary treasure.")
        print("Think critically, make wise decisions, and trust your instincts.")

        print("\nYou find yourself at a crossroads. Do you want to explore the forest or enter the cave?")
        choice = input("Type 'forest' to explore the forest or 'cave' to enter the cave: ").lower()

        if choice == 'forest':
            outcome = forest_path()
        elif choice == 'cave':
            outcome = cave_path()
        else:
            print("Invalid choice. Please choose 'forest' or 'cave'.")
            outcome = 'continue'

        if outcome == 'win':
            print("\nCongratulations! You found the treasure and won the game!")
        elif outcome == 'lose':
            print("\nOh no! Your decision led to the end of your adventure.")

        restart = input("\nWould you like to play again? (yes/no): ").lower()
        if restart != 'yes':
            print("Thanks for playing! Goodbye!")
            break


def forest_path():
    print("\nYou are in the forest. You see a river and a tall tree.")
    choice = input("Do you want to follow the river or climb the tree? Type 'river' or 'tree': ").lower()

    if choice == 'river':
        print("You follow the river and find a hidden waterfall with a secret cave behind it.")
        second_choice = input("Do you enter the secret cave? (yes/no): ").lower()
        if second_choice == 'yes':
            print("Inside the cave, you discover the ancient treasure chest.")
            return 'win'
        else:
            print("You walk away and miss the treasure.")
            return 'lose'

    elif choice == 'tree':
        print("You climb the tree and a branch breaks, dropping you into thorny bushes.")
        print("You manage to get up but you are injured and must end your adventure.")
        return 'lose'

    else:
        print("Invalid choice. Please choose 'river' or 'tree'.")
        return 'continue'


def cave_path():
    print("\nYou are in the cave. You see a dark tunnel and a small alcove.")
    choice = input("Do you want to explore deeper into the cave or take a rest? Type 'explore' or 'rest': ").lower()

    if choice == 'explore':
        print("You explore deeper into the cave and encounter a sleeping dragon.")
        second_choice = input("Do you sneak past the dragon or retreat? (sneak/retreat): ").lower()
        if second_choice == 'sneak':
            print("You sneak past the dragon and find a chest full of treasure.")
            return 'win'
        else:
            print("You retreat safely but leave the treasure behind.")
            return 'lose'

    elif choice == 'rest':
        print("While resting in the alcove, bandits find you and chase you out.")
        return 'lose'

    else:
        print("Invalid choice. Please choose 'explore' or 'rest'.")
        return 'continue'


start_game() 