# Customer Orders Analysis
# Analyzing customer orders using Python data structures

# =====================================================
# TASK 1: STORE CUSTOMER ORDERS
# =====================================================
# Requirements:
# 1. Create a list of customer names
# 2. Store each customer's order details (customer name, product, price, category) as tuples inside a list
# 3. Use a dictionary where keys are customer names and values are lists of ordered products

# Step 1.1: Create a list of customer names
customer_names = ["Alice Johnson", "Bob Smith", "Carol Williams", "David Brown", "Eve Davis"]

# Step 1.2: Store each customer's order details as tuples in a list
# Format: (customer_name, product, price, category)
orders = [
    ("Alice Johnson", "Laptop", 1200, "Electronics"),
    ("Alice Johnson", "Mouse", 25, "Electronics"),
    ("Bob Smith", "T-Shirt", 30, "Clothing"),
    ("Bob Smith", "Jeans", 60, "Clothing"),
    ("Bob Smith", "Shoes", 85, "Clothing"),
    ("Carol Williams", "Bed Frame", 350, "Home Essentials"),
    ("Carol Williams", "Pillow", 45, "Home Essentials"),
    ("David Brown", "Monitor", 400, "Electronics"),
    ("David Brown", "Keyboard", 120, "Electronics"),
    ("David Brown", "Chair", 250, "Home Essentials"),
    ("Eve Davis", "Sweater", 50, "Clothing"),
    ("Eve Davis", "Hat", 20, "Clothing"),
]

# Step 1.3: Use a dictionary where keys are customer names and values are lists of ordered products
"""
we are storing customer name as the key and it's value is lists of ordered products 
customer_order = { 
  cust_name: [
     {prod:..., price:...., category,...},
    ...
  ]
customer_orders = {
    "Alice Johnson": [
        {"product": "Laptop", "price": 1200, "category": "Electronics"},
        {"product": "Mouse", "price": 25, "category": "Electronics"},
    ],
    "Bob Smith": [
        {"product": "T-Shirt", "price": 30, "category": "Clothing"},
        {"product": "Jeans", "price": 60, "category": "Clothing"},
        {"product": "Shoes", "price": 85, "category": "Clothing"},
    ],
    "Carol Williams": [
        {"product": "Bed Frame", "price": 350, "category": "Home Essentials"},
        {"product": "Pillow", "price": 45, "category": "Home Essentials"},
    ],
    "David Brown": [
        {"product": "Monitor", "price": 400, "category": "Electronics"},
        {"product": "Keyboard", "price": 120, "category": "Electronics"},
        {"product": "Chair", "price": 250, "category": "Home Essentials"},
    ],
    "Eve Davis": [
        {"product": "Sweater", "price": 50, "category": "Clothing"},
        {"product": "Hat", "price": 20, "category": "Clothing"},
    ],
}
"""
customer_orders = {}
for customer_name, product, price, category in orders:
    if customer_name not in customer_orders:
        customer_orders[customer_name] = []
    customer_orders[customer_name].append({"product": product, "price": price, "category": category})

print("=" * 60)
print("ORDER DATA (SOURCE)")
print("=" * 60)
print(f"Total customers: {len(customer_names)}")
print(f"Total orders: {len(orders)}")
print()

# =====================================================
# TASK 2: CLASSIFY PRODUCTS BY CATEGORY
# =====================================================
# Requirements:
# 1. Use a dictionary to map each product to its respective category
# 2. Create a set of unique product categories
# 3. Display all available product categories

# Step 2.1: Use a dictionary to map each product to its category
# product_category = { prod_name: category, ... }
product_category = {}
for customer_name, product, price, category in orders:
    if product not in product_category:
        product_category[product] = category

# Step 2.2: Create a set of unique product categories
# Set ignores duplicates: same category may appear on many order rows, but we keep each category name only once.
unique_categories = set()
for customer_name, product, price, category in orders:
    unique_categories.add(category)

print("=" * 60)
print("PRODUCT CATEGORY ANALYSIS")
print("=" * 60)
# Step 2.3: Display all available product categories
print(f"Available categories: {sorted(unique_categories)}")
print(f"Total unique categories: {len(unique_categories)}")
print()

print("Products by category:")
for product, category in sorted(product_category.items()):
    print(f"  {product}: {category}")
print()

# =====================================================
# TASK 3: ANALYZE CUSTOMER ORDERS
# =====================================================
# Requirements:
# 1. Use a loop to calculate the total amount each customer spends
# 2. Classify customers based on total purchase value:
#    - Above $100: High-value buyer
#    - Between $50 and $100: Moderate buyer
#    - Below $50: Low-value buyer

# Step 3.1 & 3.2: Use a loop to calculate total spending and classify customers
# customer_spending dict is built in Task 4.4 (with top-3 sorting).
# customer_classification: maps each customer name -> label (High / Moderate / Low buyer).
"""
customer_spending (name → total $ spent)

{
    "Alice Johnson": 1225.0,      # 1200 + 25
    "Bob Smith": 175.0,           # 30 + 60 + 85
    "Carol Williams": 395.0,      # 350 + 45
    "David Brown": 770.0,         # 400 + 120 + 250
    "Eve Davis": 70.0,            # 50 + 20
}
customer_classification (name → label)


{
    "Alice Johnson": "High-value buyer",    # 1225 > 100
    "Bob Smith": "High-value buyer",        # 175 > 100
    "Carol Williams": "High-value buyer",   # 395 > 100
    "David Brown": "High-value buyer",      # 770 > 100
    "Eve Davis": "Moderate buyer",          # 50 ≤ 70 ≤ 100
}

""" 
customer_classification = {}

for customer_name in customer_names:
    total_spent = 0
    # Sum this customer's order line prices from customer_orders (if they have any orders).
    if customer_name in customer_orders:
        for order in customer_orders[customer_name]:
            total_spent += order["price"]

    # customer_spending[customer_name] = total_spent

    # Classify by assignment rules: >$100 high, $50–$100 moderate, <$50 low.
    if total_spent > 100:
        customer_classification[customer_name] = "High-value buyer"
    elif 50 <= total_spent <= 100:
        customer_classification[customer_name] = "Moderate buyer"
    else:
        customer_classification[customer_name] = "Low-value buyer"

print("=" * 60)
print("CUSTOMER CLASSIFICATION")
print("=" * 60)
for customer_name in sorted(customer_names):
    print(f"  {customer_name}: {customer_classification[customer_name]}")
print()

# =====================================================
# TASK 4: GENERATE BUSINESS INSIGHTS
# =====================================================
# Requirements:
# 1. Calculate the total revenue per product category and store in a dictionary
# 2. Extract unique products from all orders using a set
# 3. Use a list comprehension to find all customers who purchased electronics
# 4. Build customer_spending, then identify the top three highest-spending customers using sorting

# Step 4.1: Calculate the total revenue per product category and store it in a dictionary
revenue_per_category = {}
for category in unique_categories:
    revenue_per_category[category] = 0

for customer_name, product, price, category in orders:
    revenue_per_category[category] += price

# Step 4.2: Extract unique products from all orders using a set
unique_products = set()
for customer_name, product, price, category in orders:
    unique_products.add(product)

# Step 4.3: Unique customers who purchased Electronics — build a set first, then convert to a list
electronics_customers_set = {
    customer_name
    for customer_name, product, price, category in orders
    if category == "Electronics"
}
electronics_customers = list(electronics_customers_set)

# Step 4.4: Top spenders — build customer_spending (name → total $), then sort and take top 3
customer_spending = {}
for customer_name in customer_names:
    total_spent = 0
    if customer_name in customer_orders:
        for order in customer_orders[customer_name]:
            total_spent += order["price"]
    customer_spending[customer_name] = total_spent

top_three_customers = sorted(customer_spending.items(), key=lambda x: x[1], reverse=True)[:3]

print("=" * 60)
print("KEY BUSINESS INSIGHTS")
print("=" * 60)

print("Revenue by product category:")
for category in sorted(revenue_per_category.keys()):
    revenue = revenue_per_category[category]
    print(f"  {category:20}: ${revenue:8.2f}")
print()

print(f"Total Revenue: ${sum(revenue_per_category.values()):.2f}")
print()

print(f"Unique Products Count: {len(unique_products)}")
print(f"Unique Products: {sorted(unique_products)}")
print()

print(f"Customers who purchased Electronics ({len(electronics_customers)}):")
for customer in sorted(electronics_customers):
    print(f"  - {customer}")
print()

print("Top 3 Highest-Spending Customers:")
for i, (customer_name, spending) in enumerate(top_three_customers, 1):
    print(f"  {i}. {customer_name}: ${spending:.2f}")
print()

# =====================================================
# TASK 5: ORGANIZE AND DISPLAY DATA
# =====================================================
# Requirements:
# 1. Print a summary of each customer's total spending and their classification
# 2. Use set operations to find customers who purchased from multiple categories
# 3. Identify common customers who bought both electronics and clothing

# Step 5.1: Build customer-categories mapping for set operations
customer_categories = {}
for customer_name, product, price, category in orders:
    if customer_name not in customer_categories:
        customer_categories[customer_name] = set()
    customer_categories[customer_name].add(category)

# Step 5.2: Use set operations to find customers who purchased from multiple categories
multi_category_customers = [
    customer_name for customer_name, categories in customer_categories.items()
    if len(categories) > 1
]

# Step 5.3: Identify common customers who bought both electronics and clothing
# Using set intersection to find customers in both categories
electronics_buyers = set([
    customer_name for customer_name, product, price, category in orders
    if category == "Electronics"
])

clothing_buyers = set([
    customer_name for customer_name, product, price, category in orders
    if category == "Clothing"
])

common_buyers = electronics_buyers.intersection(clothing_buyers)

print("=" * 60)
print("CROSS-CATEGORY PURCHASE INSIGHTS")
print("=" * 60)
print()
# Step 5.1 continued: Print summary of each customer's total spending and classification

print(f"Customers who purchased from multiple categories ({len(multi_category_customers)}):")
for customer in sorted(multi_category_customers):
    categories = sorted(customer_categories[customer])
    print(f"  - {customer}: {', '.join(categories)}")
print()

print(f"Customers who bought BOTH Electronics AND Clothing ({len(common_buyers)}):")
for customer in sorted(common_buyers):
    print(f"  - {customer}")
print()

# =====================================================
# FINAL SUMMARY REPORT
# =====================================================

print("=" * 60)
print("COMPREHENSIVE REPORT SUMMARY")
print("=" * 60)
print(f"Total Customers: {len(customer_names)}")
print(f"Total Orders: {len(orders)}")
print(f"Total Products: {len(unique_products)}")
print(f"Total Categories: {len(unique_categories)}")
print(f"Total Revenue: ${sum(revenue_per_category.values()):.2f}")
print()

# Customer classification summary
high_value = sum(1 for classification in customer_classification.values() if "High-value" in classification)
moderate_value = sum(1 for classification in customer_classification.values() if "Moderate" in classification)
low_value = sum(1 for classification in customer_classification.values() if "Low-value" in classification)

print("Customer classification (counts):")
print(f"  High-value buyers: {high_value}")
print(f"  Moderate buyers: {moderate_value}")
print(f"  Low-value buyers: {low_value}")
print()

print("=" * 60)
