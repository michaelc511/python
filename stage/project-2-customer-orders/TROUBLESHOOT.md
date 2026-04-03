# TROUBLESHOOT: Common Issues

## KeyError when accessing dictionary
Use `.get(key, default)` instead of `dict[key]` when the key might not exist. Example: `product_counts.get(product, 0)`.

## Wrong totals
Check that you're adding to the right customer. Make sure `customer_id` is the first item in each order tuple.

## Categories missing
Initialize the dictionary with all categories first: `{cat: 0 for cat in categories}` so every category appears even if it has no orders.

## Sort order wrong
`sorted(..., reverse=True)` for highest first. `key=lambda x: x[1]` sorts by the second element (count or revenue).

## Duplicate products in category list
Use `if product not in by_category[category]:` before appending to avoid listing the same product twice.
