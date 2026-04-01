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

# Function to check if a number is prime 
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

