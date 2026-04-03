# TROUBLESHOOT: Common Issues

## "NameError: name 'current_location' is not defined"
You're using `current_location` inside a function without `global current_location`. Add that line at the top of the function.

## "KeyError" when moving
The choice the player typed doesn't exist in `choices`. Check spelling. Use `.strip().lower()` on input so "North" and "north" both work.

## Game doesn't end when you reach treasure
Make sure the location has `"win": True` and that `show_location()` returns True when it sees that. The main loop checks `won` and breaks.

## Can enter treasure room without key
In `process_choice`, check if the next place has `needs_item` and if the player has those items in `inventory` before moving.

## Items don't get picked up
When moving to a new location, check if that location has an "items" list. Loop through it and append each to inventory if not already there.
