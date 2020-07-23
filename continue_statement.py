

i = 0
while i < 10:
    i += 1
    if i == 5:  #skips due to continue statement when i = 5
        continue  # continue means: when writing a loop may be a time where you want to skip and then resume the script after
    print(i)     # [1, 2, 3, 4, 6, 7, 8, 9, 10]
    print(i ** i) # exponential power like 1^1 2^2 3^3 4^4 skip 5 resume 6^6
