# PROBLEM 1
# declare a variable x and assign 7 to it
x = 7

# find out if x is less than 10
if x < 10:
    print("Less than 10")

# change x to equal 15
x = 15



# PROBLEM 2
# declare a variable x and assign 7 to it
x = 7

# created if-else statement to check the value of x
if x < 10:
    print("Less than 10")
else:
    print("Greater than 10")

# make x to equal 15
x = 15

# check the value of x again
if x < 10:
    print("Less than 10")
else:
    print("Greater than 10")



# PROBLEM 3
# declare a variable x and assign 15 to it
x = 15

# create if-elif-else statement to check the value of x
if x < 10:
    print("Less than 10")
elif 10 < x < 20:
    print("Between 10 and 20")
else:
    print("Greater than or equal to 20")

# make x to equal 50
x = 50

# check the value of x again
if x < 10:
    print("Less than 10")
elif 10 < x < 20:
    print("Between 10 and 20")
else:
    print("Greater than or equal to 20")



# PROBLEM 4 
# declare a variable x and assign 15 to it
x = 15

# make if-else statement to check the value of x
if x < 10 or x > 20:
    print("Out of range")
else:
    print("In range")

# change x to equal 5
x = 5

# check the value of x again
if x < 10 or x > 20:
    print("Out of range")
else:
    print("In range")



# PROBLEM 5
# get the score input from the user
score = float(input("Enter the score (0-100): "))

# find out the letter grade
if score < 0 or score > 100:
    print("Score out of range")
elif score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")



# PROBLEM 6
# define tax brackets and rates 
tax_brackets = {
    "Single": [
        (8350, 0.10),
        (33950, 0.15),
        (82250, 0.25),
        (171550, 0.28),
        (372950, 0.33),
        (float('inf'), 0.35)
    ],
    "Married Filing Jointly": [
        (16700, 0.10),
        (67900, 0.15),
        (137050, 0.25),
        (208850, 0.28),
        (372950, 0.33),
        (float('inf'), 0.35)
    ],
    "Married Filing Separately": [
        (8350, 0.10),
        (33950, 0.15),
        (68525, 0.25),
        (104425, 0.28),
        (186475, 0.33),
        (float('inf'), 0.35)
    ],
    "Head of Household": [
        (11950, 0.10),
        (45500, 0.15),
        (117450, 0.25),
        (190200, 0.28),
        (372950, 0.33),
        (float('inf'), 0.35)
    ]