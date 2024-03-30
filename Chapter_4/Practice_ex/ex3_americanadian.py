# CCC '02 J2 - AmeriCanadian
# https://dmoj.ca/problem/ccc02j2

# Write a program to help Americans translate to Canadian.

# Input : string < 64 chars
# Output : word traduce to Canadian if is american, if not return 
# word as given. 

# Conditions for detecting American spelling :
# if word > 4 chars AND suffix consisting of a consonant followed 
# by 'or'

vowels = 'aeiouy'
box = ''

while True:
    word = str(input())
    if word == 'quit!':
        break
    else:
        if len(word)> 4 and word[-2:]== 'or' and word[-3] not in vowels:
            box = word[:-1] + 'u' + word[-1]
            print(box)
        else:
            print(word)



