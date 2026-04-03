# EXPLAIN: How the Adventure Game Works

## What This Game Does

You wake up in a forest. You type commands (like "north" or "east") to move. Your goal is to find the treasure in the castle. You need to pick up a key first to open the door.

---

## Step-by-Step Walkthrough

### 1. Variables at the Top

```python
current_location = "start"
inventory = []
```

- `current_location` = where you are right now (starts at "start")
- `inventory` = list of items you've picked up (empty at first)

### 2. The `locations` Dictionary

This is a big dictionary. Each key is a place name. Each value tells the game:
- **description**: What you see
- **choices**: What you can type and where it takes you
- **items**: Things you can pick up there (optional)
- **needs_item**: What you must have to enter (optional)

### 3. The Main Loop

```
Show where you are → Ask for your choice → Do what you chose → Repeat
```

### 4. Key Functions

- **show_location()**: Prints the description and your options
- **get_player_choice()**: Asks you to type something
- **process_choice()**: Checks your input and moves you or picks up items

### 5. The Win Condition

When you reach "treasure_room", the game sees `"win": True` and ends with "You win!"

---

## Concepts Used

| Concept | Where It's Used |
|--------|------------------|
| Variables | current_location, inventory |
| Lists | inventory, items in locations |
| Dictionaries | locations (nested) |
| Loops | while not game_over |
| Conditionals | if choice in choices, if item not in inventory |
| Functions | show_location, get_player_choice, process_choice |
