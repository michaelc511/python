"""
Building a Python Adventure Game with GitHub Copilot
A text-based adventure where users explore locations, make choices, and complete a quest.
"""

# Game state - where the player is and what they have
current_location = "start"
inventory = []
game_over = False

# Game map - each location has a description and choices
locations = {
    "start": {
        "description": "You wake up in a dark forest. A path leads north to a castle, east to a village.",
        "choices": {"north": "castle", "east": "village"},
    },
    "castle": {
        "description": "A towering castle. The gate is open. You see a key on the ground.",
        "choices": {"enter": "castle_hall", "back": "start"},
        "items": ["key"],
    },
    "castle_hall": {
        "description": "Inside the castle hall. A locked door is to the west. A chest sits in the corner.",
        "choices": {"west": "treasure_room", "back": "castle"},
        "needs_item": ["key"],
        "blocked_message": "The door is locked. You need a key.",
    },
    "treasure_room": {
        "description": "You found the treasure! The quest is complete. You win!",
        "choices": {},
        "win": True,
    },
    "village": {
        "description": "A quiet village. A shopkeeper waves you over. 'Need supplies?'",
        "choices": {"north": "castle", "talk": "village"},
    },
}


def show_location():
    """Display the current location and what the player can do."""
    loc = locations.get(current_location, {})
    print("\n" + "=" * 40)
    print(loc.get("description", "Unknown place."))
    print("=" * 40)
    
    if loc.get("win"):
        return True
    
    choices = loc.get("choices", {})
    if choices:
        print("\nWhat do you do?")
        for action, destination in choices.items():
            print(f"  - {action}")
    return False


def get_player_choice():
    """Ask the player what they want to do."""
    choice = input("\nYour choice: ").strip().lower()
    return choice


def process_choice(choice):
    """Handle the player's choice and move them or give items."""
    global current_location, inventory
    
    loc = locations.get(current_location, {})
    choices = loc.get("choices", {})
    
    if choice in choices:
        next_place = choices[choice]
        
        if next_place == current_location and choice == "talk":
            print("The shopkeeper says: 'Good luck on your quest!'")
            return
        
        if loc.get("needs_item") and next_place == "treasure_room":
            for item in loc["needs_item"]:
                if item not in inventory:
                    print(loc.get("blocked_message", "You can't go there yet."))
                    return
        
        if next_place in locations and "items" in locations.get(next_place, {}):
            for item in locations[next_place]["items"]:
                if item not in inventory:
                    inventory.append(item)
                    print(f"\nYou picked up: {item}")
        
        current_location = next_place
    else:
        print("That's not a valid choice. Try again.")


def main():
    """Run the game loop."""
    global game_over
    
    print("\n*** PYTHON ADVENTURE GAME ***")
    print("Explore, make choices, and find the treasure!")
    
    while not game_over:
        won = show_location()
        if won:
            print("\nCongratulations! You completed the quest!")
            break
        
        choice = get_player_choice()
        if choice == "quit":
            print("Thanks for playing!")
            break
        
        process_choice(choice)


if __name__ == "__main__":
    main()
