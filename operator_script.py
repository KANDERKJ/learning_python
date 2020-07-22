# We're going to read in a number from the user input
# we want to see if the number is greater than 50
# we want display the output

# STARTER CODE
read_num = int(input('Enter in a number'))
print(' The number is {}'.format(read_num))

# write the comparison operator to check if read_num is greater than 50
# WRITE CODE HERE

print(read_num > 50)   # enter 45 the statement is false enter 65 the statment is true

# if operator
# ----------
# if expr:    expression reduces down to a single value immediatley follows 'if' sing bool True/False
        #statements are code to be executed inside 'if'

x = 5
if x == 5:
    print(x)

print('How many years have you been an employee')
empyears = int(input())     # empyears is integer input, input form user
if empyears >= 5:           # if user input was >= to 5
    vacadays = int(empyears * 2)
if empyears < 5:            # if empyears was < than 5
    vacadays = int(empyears * 1)
print('You have'+ str(vacadays) + 'vacation days.') # enter 5 years as employee will equal 10 days vacay (5 * 2)

num = int(input('Type in an integer'))
# type in an integer of 100
if num == 100:
    x = num * 2
num = 100
print(x)

num = int(input('Type in an integer'))
if num == 100:
    x = num * 2
if num < 100:
    x = num / 2
if num > 100:
    x = num
print(x)

