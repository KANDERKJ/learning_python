

extension_list = {'Albert': 'ext21', 'Beth': 'ext42', 'Charles': 'ext07'}       # create a dictionary
print(extension_list)

# how to index a dictionary
print(extension_list['Albert'])     # 'ext21'
print(extension_list['Beth'])       # 'ext42'
print(extension_list['Charles'])    # 'ext07'

# get the keys of a dictionary

print(extension_list.keys())

# get the values of a dictionary

print(extension_list.values())

x = [2, 4, 6] # [2, 4, 6]
x.append(8)     # [2, 4, 6, 8]

extension_list.update({'James': 'ext14'})     # update adds dict like append adds list
print(extension_list)

extension_list.update({'Albert': 'ext100'})     # update also changes keys value pair
print(extension_list)

print(extension_list.get('Albert'))     # gives value, = extension_list['Albert']
extension_list['Beth']  = 'ext55'       # using square brackets allows us to reassign dict value
print(extension_list)

y = [1, 3, 5, 9]
y.pop() # [1, 3, 5] removes last value of 9
print(y)

extension_list.popitem()  # removes 'James': 'ext14' removes last dict
print(extension_list)
extension_list.pop('Beth')      # removes the specific dict you choose
print(extension_list)

# dictionary example    #keys have to be immutable , values can be anything-dictionary,tuple, list etc.

phone_book = { 'pizza': ['253-374-2832', '253-374-8372', '253-374-2834'], 'auto': ['253-474-9723', '253-474-2732', '253-632-8621'],
               'restaurant': ['253-3623-8376', '253-253-2532', '253-734-2834'] }
print(phone_book['pizza'])  # ['253-374-2832', '253-374-8372', '253-374-2834']
print(phone_book['pizza'][1])  # prints '253-374-2832'
