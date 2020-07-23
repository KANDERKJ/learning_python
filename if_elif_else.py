

# Demo of if/elif statement from Doug

print('How many years have you been an employee: ')
emyears = int(input())  # raw_inout() is used in python2.x
if emyears >= 30:
    vacadays = int(emyears * 3)
elif emyears >= 20:
    vacadays = int(emyears *2)
elif emyears >= 10:
    vacadays = int(emyears * 1.5)
else:
    vacadays = int(emyears * 1)
print('You have ' + str(vacadays) + ' vacation days.')



emyears = int(input('How many years you have been an employee? '))
if emyears >= 30:
    vacadays = float(emyears * 3)
elif emyears >= 20:
    vacadays = float(emyears * 2)
elif emyears >= 10:
    vacadays = float(emyears * 1.5)
else:
    vacadays = emyears * 1
print('You have ' + str(vacadays) + ' vacation days.')