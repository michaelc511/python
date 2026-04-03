"""
Analyzing Customer Orders Using Python
Classify products, identify purchasing patterns, and generate business insights.
"""

# Sample customer order data: (customer_id, product_name, category, price)
orders = [
    (101, "Laptop", "Electronics", 899),
    (101, "Mouse", "Electronics", 29),
    (102, "T-Shirt", "Clothing", 25),
    (102, "Jeans", "Clothing", 55),
    (103, "Coffee Maker", "Home Essentials", 79),
    (103, "Laptop", "Electronics", 899),
    (104, "Headphones", "Electronics", 149),
    (104, "Pillows", "Home Essentials", 35),
    (105, "Sweater", "Clothing", 45),
    (105, "Laptop", "Electronics", 899),
    (101, "Keyboard", "Electronics", 59),
    (102, "Shoes", "Clothing", 80),
]

# Product categories
categories = {"Electronics", "Clothing", "Home Essentials"}


def get_customer_totals(orders):
    """Add up total spending per customer. Returns a dictionary."""
    customer_totals = {}
    for customer_id, product, category, price in orders:
        if customer_id not in customer_totals:
            customer_totals[customer_id] = 0
        customer_totals[customer_id] += price
    return customer_totals


def classify_customers(customer_totals):
    """Classify customers by spending: high, medium, or low value."""
    high_value = 500
    medium_value = 200
    
    classification = {}
    for customer_id, total in customer_totals.items():
        if total >= high_value:
            classification[customer_id] = "High Value"
        elif total >= medium_value:
            classification[customer_id] = "Medium Value"
        else:
            classification[customer_id] = "Low Value"
    return classification


def get_products_by_category(orders):
    """Group products by category. Returns a dictionary of category -> list of products."""
    by_category = {cat: [] for cat in categories}
    for customer_id, product, category, price in orders:
        if product not in by_category[category]:
            by_category[category].append(product)
    return by_category


def get_most_purchased_products(orders):
    """Find which products were bought most often. Returns a list of (product, count)."""
    product_counts = {}
    for customer_id, product, category, price in orders:
        product_counts[product] = product_counts.get(product, 0) + 1
    
    sorted_products = sorted(product_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_products


def get_category_revenue(orders):
    """Calculate total revenue per category."""
    category_revenue = {cat: 0 for cat in categories}
    for customer_id, product, category, price in orders:
        category_revenue[category] += price
    return category_revenue


def main():
    """Run the analysis and print results."""
    print("=" * 50)
    print("CUSTOMER ORDER ANALYSIS REPORT")
    print("=" * 50)
    
    customer_totals = get_customer_totals(orders)
    print("\n1. CUSTOMER TOTAL SPENDING:")
    for cust_id, total in sorted(customer_totals.items()):
        print(f"   Customer {cust_id}: ${total}")
    
    classification = classify_customers(customer_totals)
    print("\n2. CUSTOMER CLASSIFICATION:")
    for cust_id, level in sorted(classification.items()):
        print(f"   Customer {cust_id}: {level}")
    
    by_category = get_products_by_category(orders)
    print("\n3. PRODUCTS BY CATEGORY:")
    for cat, products in by_category.items():
        print(f"   {cat}: {products}")
    
    most_purchased = get_most_purchased_products(orders)
    print("\n4. MOST PURCHASED PRODUCTS:")
    for product, count in most_purchased[:5]:
        print(f"   {product}: {count} orders")
    
    revenue = get_category_revenue(orders)
    print("\n5. REVENUE BY CATEGORY:")
    for cat, amount in sorted(revenue.items(), key=lambda x: x[1], reverse=True):
        print(f"   {cat}: ${amount}")
    
    print("\n" + "=" * 50)
    print("BUSINESS INSIGHTS:")
    print("- High-value customers (>$500) are key for revenue.")
    print("- Electronics drives the most revenue.")
    print("- Focus marketing on Laptop and Electronics category.")
    print("=" * 50)


if __name__ == "__main__":
    main()
