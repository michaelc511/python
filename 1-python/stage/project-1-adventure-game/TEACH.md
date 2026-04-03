# TEACH: Script for Teaching This Project

## Opening (1 min)

"Today we're building a text-based adventure game. No graphics—just text. You type 'north' or 'east' and the game tells you what happens. The goal: find the treasure in the castle."

## Key Points to Cover

### 1. The Dictionary is the Map (2 min)

"All the places in the game live in one big dictionary called `locations`. Each place has a description—what you see—and choices—what you can type. When you type 'north', the game looks up where that takes you and moves you there."

### 2. Variables Track State (1 min)

"`current_location` remembers where you are. `inventory` is a list of stuff you picked up. The game changes these as you play."

### 3. The Loop (2 min)

"The game runs in a loop: show the place, ask for input, process the choice, repeat. It keeps going until you win or quit."

### 4. Functions Break It Up (1 min)

"We split the work into functions: one shows the location, one gets your input, one processes it. Easier to read and fix."

### 5. Live Demo (3 min)

Run the game. Move to the castle, pick up the key, enter the treasure room. Narrate what the code is doing as you go.

## Closing

"That's the core: a dictionary for the map, variables for state, a loop, and functions. You can add more locations or items the same way."
