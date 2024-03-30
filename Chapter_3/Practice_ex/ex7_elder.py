# COCI '18 Contest 4 #1 Elder
# https://dmoj.ca/problem/coci18c4p1

# Questions :
# 1. Which wizard did the wand obey after all  duels?
# 2. How many different wizards did the wand obey?

# Input :
# 1. The first line contains an uppercase letter of 
# the English alphabet, the label of the wizard that the 
# wand obeyed at the beginning.

# 2. The second line contains an integer number :
# N ( 1<= N <= 100), the number of duels from the text of
# the task.

# Nth. ...rows there are two different uppercase letters of the 
# English alphabet: Z1 - Z2 separated by a space, whereas the
# wizard with the label Z1 defeated the wizard with the label Z2
# in the  duel.

# Output :
# 1. Uppercase letter of English Alphabet > wizar wand obeys
# 2. Int > n of different wizards the wand obey

owner = str(input())
n_duels = int(input())
ow_count = 1
owners = []
owners.append(owner)

for n in range(0, n_duels):
    match = str(input())
    
    if match[-1] == owner:
        owner = match[0]
        if owner in owners:
            pass
        else:
            ow_count +=1
            owners.append(owner)
        
    else:
        continue

print(owner)
print(ow_count)