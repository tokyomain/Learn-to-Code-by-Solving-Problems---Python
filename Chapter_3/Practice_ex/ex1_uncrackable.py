# WC '17 Contest 3 J3 - Uncrackable
# https://dmoj.ca/problem/wc17c3j3


# The password must be a string between 8 and 12 characters 
# long (inclusive). Such that every character is either:
# - uppercase letter >= 2
# - lowercase letter >= 3
# - digit >= 1

# Input : The first and only line of input consists of a single 
# string, the password. 
# Output : Output a single string, either 'Valid' if the password
# is valid, or 'Invalid' otherwise.

password = input()
upper_ch = 0
lower_ch = 0
digit = 0

if len(password) >= 8 and len(password) <= 12:
    for c in password:
        if c.isupper():
            upper_ch += 1
        elif c.islower():
            lower_ch += 1
        elif c.isdigit():
            digit += 1
else:
    pass


if (upper_ch >= 2) and (lower_ch >= 3) and (digit >= 1):
    print('Valid')
else:
    print('Invalid')

'''print('Upper Characters(2): ', upper_ch)
print('Lower Characters(3): ', lower_ch)
print('Digit characters(1): ', digit)'''