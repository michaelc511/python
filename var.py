
# Lesson 3 
# Declare variables for name, age, and salary.
name = "John Doe"
age = 30
salary = 50000.0

#print numbers from 1 to 100
for i in range(1, 101):
    print(i)    

# Print numbers from ten to one using a while loop.
count = 10
while count > 0:
    print(count)
    count -= 1  

# Check if a number is positive, negative, or zero. 
number = 5
if number > 0:
    print("The number is positive.")
elif number < 0:    print("The number is negative.")
else:    print("The number is zero.")         

# Create a list of even numbers from one to twenty. 
even_numbers = [i for i in range(1, 21) if i % 2 == 0]
print(even_numbers) 

# Create a dictionary of student grades. 
student_grades = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}
print(student_grades) 

# Define a tuple of three programming languages. 
programming_languages = ("Python", "Java", "C++")
print(programming_languages)  

# 2.1 Function to check if a number is prime 
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def reverse_string(s):
    """This function takes a string as input and returns the reversed version of the string."""
    return s[::-1]

# 3.1 
def is_prime3(n):
    """ this function checks whetaer a number is prime
    it returns true if the number is prime, otherwise false
        """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 4.1 
# Function to check prime numbers
# The function should handle edge cases like 0,1 and negative numbers
def is_prime4(n):
    """ this function checks whetaer a number is prime
    it returns true if the number is prime, otherwise false
        """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 5.1
def is_prime5(n):
    for i in range(2, n):
        if n % i == 0:
            return False

# Lesson 4

# Function to count the number of vowels in each string
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

print(count_vowels("Hello World"))  # Output: 3
print(count_vowels("Python Programming"))  # Output: 4
print(count_vowels("Data Science"))  # Output: 5
print

# Lesson 5

 
# fix syntax error and handle negative inputs
def factorial(n):
    """This function calculates the factorial of a number n using recursion."""
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(5))  # Output: 120
print(factorial(0))  # Output: 1
print(factorial(-3)) # Output: Factorial is not defined for negative numbers.