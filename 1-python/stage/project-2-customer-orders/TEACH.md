# TEACH: Script for Teaching This Project

## Opening (1 min)

"We're playing data analyst. We have a list of orders—who bought what and for how much. Our job: find patterns. Who are our best customers? What sells most? Where does our money come from?"

## Key Points to Cover

### 1. Tuples for Fixed Data (2 min)

"Each order is a tuple: (customer_id, product, category, price). Tuples are like lists but you don't change them. Good for data that shouldn't be edited."

### 2. Dictionaries for Grouping (2 min)

"When we want to add up spending per customer, we use a dictionary. Key = customer_id, value = total. Every time we see an order, we add its price to that customer's total."

### 3. Loops and Conditionals (2 min)

"We loop through every order. We use if/else to classify: if total >= 500, high value; elif >= 200, medium; else low."

### 4. Sets for Unique Values (1 min)

"Categories is a set—it only holds unique values. No duplicate 'Electronics' or 'Clothing'. We use it to make sure we have all categories when we build our results."

### 5. Run and Interpret (3 min)

Run the program. Point out: "See how Electronics has the most revenue? That's a business insight. We'd tell the manager: focus on Electronics."

## Closing

"Same pattern for any data analysis: load data, loop through it, group with dictionaries, then summarize. The structures—lists, tuples, dicts, sets—are the tools."
