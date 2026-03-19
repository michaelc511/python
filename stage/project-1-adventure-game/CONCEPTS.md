# CONCEPTS: What You Need to Know

## Variables
A name that holds a value. `current_location = "start"` means "current_location" holds the text "start".

## Lists
Ordered collection. `inventory = []` is an empty list. `inventory.append("key")` adds "key" to it.

## Dictionaries
Key-value pairs. `{"north": "castle"}` means the key "north" leads to the value "castle". Used for the game map.

## Loops
`while not game_over:` keeps running until game_over becomes True. The game loop runs forever until you win or quit.

## Conditionals
`if choice in choices:` checks if what the player typed is valid. `if item not in inventory:` checks if they have the item.

## Functions
Reusable blocks of code. `def show_location():` defines a function. You call it with `show_location()`.

## Global
`global current_location` lets a function change a variable that lives outside the function. Used when the player moves to a new place.
