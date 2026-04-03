# Adventure Game - A text-based quest to find treasure in an ancient land
# Using GitHub Copilot to assist in writing and optimizing code

print("Adventure Game Setup Complete!")

# function start_game() to display game intro and ask player for their name and store it in a variable.
"""
 Now provide the player w initial choice (explore a forest or enter a cave)
"""
def start_game():
    while True:
        print("Welcome to the Adventure Game!")
        player_name = input("Please enter your name: ")
        print(f"Hello, {player_name}! Your adventure begins now.")
        
        print("You find yourself at a crossroads. Do you want to explore the forest or enter the cave?")
        choice = input("Type 'forest' to explore the forest or 'cave' to enter the cave: ").lower()
        
        if choice == 'forest':
            forest_path()
        elif choice == 'cave':
            cave_path()
        else:
            print("Invalid choice. Please choose 'forest' or 'cave'.")
        
        restart = input("\nWould you like to play again? (yes/no): ").lower()
        if restart != 'yes':
            print("Thanks for playing! Goodbye!")
            break    

def forest_path():
  """
    describes the forset scenario. provide the player with choices to follow a river or climb a tree) Use if-else to hande the choices
  """
  print("You are in the forest. You see a river and a tall tree.")
  choice = input("Do you want to follow the river or climb the tree? Type 'river' or 'tree': ").lower()       
  if choice == 'river':
    print("You follow the river and find a hidden waterfall with a secret cave behind it!")
  elif choice == 'tree':
    print("You climb the tree and find a nest with a golden egg inside!")
  else:
    print("Invalid choice. Please choose 'river' or 'tree'.")     

def cave_path():
   """ describes the cave scenario. provide the player with choices  (light a torche or proceed in the dark) use conditions to determin the outcome   
   """
   print("You are in the cave. You see a dark tunnel and a small alcove.")    
   choice = input("Do you want to explore deeper into the cave or take a rest? Type 'explore' or 'rest': ").lower()       
   if choice == 'explore':
     print("You explore deeper into the cave and find an ancient artifact that grants you magical powers!")
   elif choice == 'rest':
     print("You take a rest in the alcove and find a hidden stash of supplies that will help you on your adventure!")
   else:
     print("Invalid choice. Please choose 'explore' or 'rest'.")

start_game() 