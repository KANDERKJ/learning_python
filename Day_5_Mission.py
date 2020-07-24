# Day 5 Mission

# 1) integers and float points (int and float)

# 2) integer

# 3)
pi = 3.14
r =  2
print(type(pi))
print(type(r))
print(pi * r ** 2)

# 4)
name = 'Kyle'
surname = 'Kander'
print(type(name))
 # i) string
 # ii)
print('Kyle ' + 'Kander')
# iii)
print([name.lower() ] + [surname.upper()])


# 5)
question = input('Is Marine Corps bootcamp extremely difficult? ')
if question == 'Yes':
    print('Yes, hard as tits!')
else:
    print('Silence, I kill you!')

# 6)

budget =int(input('What is your budget? '))
if budget <= 0:
    print('error')
elif budget > 1000:
    print('error')
elif budget > 550:
    print('You will eat well this month!')
elif budget == 550:
    print('This is the average American food budget.')
else:
    print('This is less than the average American food budget.')

# 7)
i = 1
while i <= 100:
    if i % 2 == 0:
        print(i, end=' ')
    i = i + 1
print()
# i)
i = range(1, 100)
for i in range(2, 101, 2):
    print(i, end=' ')
    i = i +2
print()
# 8)
import random
nums = random
for nums in range(100):
    print(random.randint(1, 100), end=' ')

print()

nums = []
for x in range(100):
    y = random.randint(1, 100)
    nums.append(y)
print(nums)
