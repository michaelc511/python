# CONCEPTS: What You Need to Know

## List
Ordered collection. `orders = [...]`. You can add, remove, loop through. Mutable (changeable).

## Tuple
Like a list but immutable (can't change). `(101, "Laptop", 899)`. Good for fixed records.

## Dictionary
Key-value pairs. `{"customer_101": 500}`. Look up by key. Great for grouping and summing.

## Set
Collection of unique items. No duplicates. `{"Electronics", "Clothing"}`. Used when you need "all possible categories."

## Lambda
Short way to write a one-line function. `key=lambda x: x[1]` means "sort by the second item."

## .get()
`scores.get("Alice", 0)` returns the value for "Alice", or 0 if not found. Avoids KeyError.
