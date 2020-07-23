
# variable  integers, floating points, strings

x = 5     # integer int
y = 1.2636  # float point float
z = 'python'  # string str

print(x)    # displays the output to the terminal
print(y)
print(z)

# how do we determine the type of a variable?
print(type(x))
print(type(y))
print(type(z))

# basic mathematical operators
# + - * / () **-power %-remainder //

a = (5 * 9 / 3) + 10 ** 2 -1
print(a)

print(5 // 3)   # 1 // is the float operator

# strings data type
a = 'python'                  # single quote
b = "javascript"             # doube quotes
c = """This is docstring"""  # triple quotes, or docstring
# ways to format a string in python  #important to format to add clarity to output data
print('The language is', a)   # can use comma to format strings
print('{} and {} are programming languages'.format(a.capitalize(), b))    # can use .format operator
print('{1} and {0} are programming languages'.format(a.capitalize(), b))    # a refers to index 0, b refers to index 1
# the f-string
a, b, c = 50, 650, 400
print(f'{a} x {b} = {a * b}!')

# c-style programming
# printf() function in C-programming
print('%d * %d = %d' % (5, 5, 5 * 5))

# properties of strings
# indexing
x= 'football'
y = 'basket ball'
print(x[0])             # f
print(x[4])             # b
print(x[-1])            # l
print(x[len(x) - 1])    # l
# slice
# string[start:stop:skip]
print(x[0:4])           # foot
print(x[4:])            # ball
print(x[4:100])         # ball
print(x[::])            # football  # :: 3rd integer is skip step
print(x[:5])            # footb
print(x[::1])           # football
print(x[::2])           # fobl
print(x[::-1])          #llabtoof # reverse the string
print(x[0:-1])
print(x[4:-1])

# 4 builtin data structures in python
# data structures store and organize data

#list
# -------------
# mutable
# index list like a string
# a list can be sliced like a string
# append
# pop
# extend
# sort
# list are great when we need to rapidly
# list: has index and elements. Indexes are integers at map values. Elements are

x = []              # empty list
x.append(10)
x.append(20)
x.append(30)
x.append(40)
print(x)           # [10, 20, 30, 40]
# remove 40 from x
x.pop()     # removes 40
x.pop()     # removes 30
print(x)    # [10, 20]

x.extend([30, 40, 50, 60])
print(x)  # [10, 20, 30, 40, 50, 60]

# tuple
# --------------
# immutable data structure
# once created in memory, can't reassign
# use tuple when you want to store data
# is more memory efficient than list
# limited functionality compared to a list
# consider using tuple when there is a relationship between data

laptop = ('apple', 'dell', 'hp', 'sony', 'lenova')
# index
print(laptop[0])
print(laptop[-1])
# slice
print(laptop[2:])   # (hp, sony, lenova)

# list indexes can be reassigned
odds = [1, 3, 5]
print(odds)
odds[2] = 7      # [1, 3, 7]
print(odds)

# dictionaries
# ------------------
# key/value mappings
# dictionaries index data using keys
# use when you need to represent data in a map
# example of dict in action is JSON

military = {'a': 'army', 'c': 'chairforce', 'n': 'navy', 'm': 'marines', 'g': 'coast guard'}
print(military)

#keys
print(military.keys())
# values
print(military.values())
# get specific value
print(military['a'])
# get method
print(military.get('m'))  # marines

# reassignment , a benifit of using subscript nototation
military['n'] = 'Navy' #capitalized navy
print(military)

# set
# ----------
# containers for unique items only
# doesn't store in order

a = {1, 2, 2, 5, 10}    # {1, 2, 10, 5}
print(a)


