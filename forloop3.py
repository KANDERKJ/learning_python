
# keep count of the vowels

vowel = 0 # the counter
basket = input('Enter in some text')    # reads input from user
for item in basket:
    if item == 'a' or item == 'e' or item == 'i' \
    or item == 'o' or item == 'u':
        vowel += 1

print('In the string: \n + basket')  # print('In the string: \n {}'.format(basket))
print('The vowel count is {}'.format(vowel)) # print('The vowel count is: ' + str(vowel))

# need descriptive variable names not vague or open to misinterpretation
# \n means new line

