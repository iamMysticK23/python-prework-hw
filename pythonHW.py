# Question 1:
# Write a function to print 'hello_USERNAME!"
# USERNAME  is the input of the function.


def hello_name(user_name):
    """Return as 'hello_USERNAME, where USERNAME is input:"""
    print("Hello" + "_" + user_name.upper() + "!")

hello_name('kenai')


# Question 2:
# Write a python function, first_odds 
# that prints the odd numbers from 1-100
# and returns nothing

def first_odds():
    """Returns odd values from 1-100"""
    odds = []
    for value in range (1,101):
        if value % 2 == 1:
            odds.append(value)
    print(odds)

# Call function
first_odds()


# Question 3:
# Please write a python function, max_num_in_list 
# to return the max number of a given list.


def max_num_in_list(a_list):
    """Returns max number in a list"""
    # Define a list to store the numbers to compare
    max_number = a_list[0]

    # loop though numbers to compare which one is bigger
    # biggest number at the time gets stored until it fails the loop
    for num in a_list:
        if num > max_number:
            max_number = num
    return max_number

# Define the testing lisst
a_list = [9, 204.8, 99.3, 34.8, 6]

#Call function
print("The biggest number in the list is : ", max_num_in_list(a_list))


# Question 4:
# Write a function to return if
# the given year is a leap year,
# A leap year is divisible by 4, but not divisible by 100
# unless it is also divisible by 400. The return should
# be boolean type (true/false).

def is_leap_year(a_year):
    """Run an if/else statement to see if input meets leap year criteria"""
    if (a_year % 400 == 0) or (a_year % 100 != 0) and (a_year % 4 ==0):
        return bool(a_year)
    
    else:
        return False
      
# Get input from user
a_year = int(input("Enter a year to see if it is a leap year. "))

# Call function
print("The year you typed in is a leap year:", is_leap_year(a_year))


# Question 5:
# Write a function to check to see
# if all numbers in list are consectutive numbers.
# For example, [2,3,4,5,6,7] are consectutive numbers
# but [1,2,4,5] are not consecutive numbers.
# The return should be boolean type.

# Note: I wanted the list to take input from a user instead of putting in a default list.

def is_consecutive(a_list):
    """Sort the list of numbers from the min range given to the max range given"""
    for numbers in range (0, input_numbers):
        user_input = int(input())
        numbers_list.append(user_input)
    return sorted(a_list)  == list(range(min(a_list), max(a_list) + 1))

# Empty list to store numbers
numbers_list = []

# Input numbers
input_numbers = int(input("How many numbers do you want to check to see if they are consecutive? "))


# Call function
print("Please input " + str(input_numbers) + " numbers.\nPress 'Enter' after each number entry." )
print("Is this list consecutive?" , is_consecutive(numbers_list))

