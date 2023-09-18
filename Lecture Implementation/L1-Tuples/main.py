"""
FUNCTIONS
1) Write a program that takes two inputs from the user. If both values are positive, add and print the result.
If both values are negative, multiply the numbers and print the result.

2) Put the code in the function

3) Pass the inputs as arguments to the function.
"""


def processing(x, y):
    if x > 0 and y > 0:
        print("The summation is", x + y)
    if x < 0 and y < 0:
        print("The product is", x * y)


int1, int2 = int(input("Enter value one: ")), int(input("Enter value two: "))
processing(int1, int2)

"""
LOOPS
1) Write a program that prints your name for an inputted number of times.
2) Print the even numbers between 1 and 10.
3) While loop that takes numbers from the user and stops when the user enters a number greater than 10.
4) Write a loop that takes numbers from the user and stores them in a list.
"""

# 1
print()
name = input("What is your name? ")
repeat = int(input("Enter the number of times you want the program to repeat: "))
for a in range(repeat):
    print(name)
while repeat > 0:
    print(name)
    repeat -= 1

# 2
print()
for b in range(1, 11):
    if b % 2 == 0:
        print(b)

# 3
print()
c = 0
while c < 10:
    c = float(input("Enter a number: "))

# 4
print()
my_list = []
var = 0
while var == 0:
    text = input('Enter a number: ')
    if text == "":
        break
    my_list.append(int(text))
summation = 0
for d in range(len(my_list)):
    summation += my_list[d]
print("Your total is:", summation)
"""
We ca use the index instead of list_name.append(item) bu creating a list with a fixed length
and using a loop, updating the index position with the inputted data.
"""
