# EXPLAIN: How the Customer Orders Analysis Works

## What This Program Does

It takes a list of customer orders (who bought what, from which category, for how much) and answers:
- How much did each customer spend?
- Are they high, medium, or low value?
- Which products sold the most?
- Which category made the most money?

---

## Step-by-Step Walkthrough

### 1. The Data

```python
orders = [(101, "Laptop", "Electronics", 899), ...]
```

Each order is a tuple: (customer_id, product_name, category, price). A tuple is like a list but you can't change it. We use it for data that stays fixed.

### 2. get_customer_totals()

Loops through all orders. For each one, it adds the price to that customer's total. Uses a dictionary: `customer_totals[customer_id] += price`.

### 3. classify_customers()

Takes the totals and puts each customer in a bucket:
- High Value: $500 or more
- Medium Value: $200 to $499
- Low Value: Under $200

### 4. get_products_by_category()

Groups products by category. Uses a dictionary where each category is a key and the value is a list of products in that category.

### 5. get_most_purchased_products()

Counts how many times each product was bought. Uses `product_counts.get(product, 0) + 1` to add 1 each time we see that product. Then sorts by count, highest first.

### 6. get_category_revenue()

Adds up all the money per category. Same idea as customer totals, but grouped by category instead of customer.

---

## Data Structures Used

| Structure | Where | Why |
|----------|-------|-----|
| List | orders | Ordered list of all orders |
| Tuple | each order | Fixed data (customer, product, category, price) |
| Dictionary | customer_totals, by_category | Look up by key (customer_id or category) |
| Set | categories | Unique list of categories (no duplicates) |
