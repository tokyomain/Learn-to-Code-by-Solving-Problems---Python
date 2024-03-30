# COCI '18 Contest 3 #1 Magnus
# https://dmoj.ca/problem/coci18c3p1

# HONI-block
# Input : The first line contains a word of length:
# (1 <= N >= 100.000), consisting of uppercase letters of the
#  English alphabet.

# Output : num > In the first and only line, print out the 
# required number of HONI-blocks.


# palabra = 'EEHUFONDIHDFODADNNNHINODIHSODNDEUI'
word = str(input())
honi = 'HONI'
index = 0
honies = ''

for ch in word:
    if index == 4:
        index = 0
    else:
        pass
    if ch == honi[index]:
        honies += ch
        index += 1
    else:
        pass

print(honies.count(honi))