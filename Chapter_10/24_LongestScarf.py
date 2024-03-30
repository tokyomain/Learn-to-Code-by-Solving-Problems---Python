# DMOPC '20 Contest 2 P2 - Lousy Christmas Presents
# https://dmoj.ca/problem/dmopc20c2p2


# Scarf whose length is 'n' feet and each foot has a specific color
# You also have 'm' relatives
# Each relative indicates what their desired scarflooks like by specifying 
# the color of its first foot and last foot.

# Your goal is to cut your original scarf in such a way as to produce the
# longest desired scarf for one of your relatives.

# Input: 
# 1/ A line containing the integer scarf length 'n' and integer number of
#relatives 'm', separated by a space.   1 < 'n' 'm' < 100.000

# 2/ A line containing n integers separated by spaces. Each integer specifies
#  the color of one foot of scarf in order from the first foot to the last foot.
# Each integer is between 1 and 1,000,000

# 3/ m lines, one per relative, containing two integers separated by a
# space. These numbers describe the relative’s desired scarf: the first
# integer is the desired color of the first foot, and the second integer
# is the desired color of the last foot.

# Output:
# Output the length of the longest desired scarf that can be produced by cutting
# your original scarf.


#        //////////     {  Functions  }     //////////

#       //////////     {  Main Program  }     //////////   

lst = input().split()
n = int(lst[0])
m = int(lst[1])

scarf = input().split()
for i in range(n):
    scarf[i] = int(scarf[i])

leftmost_index = {}
rightmost_index = {}

for i in range(n):
    color = scarf[i]
    if not color in leftmost_index:
        leftmost_index[color] = i
        rightmost_index[color] = i
    else:
        rightmost_index[color] = i

max_length = 0

for i in range(m):
    relative = input().split()
    first = int(relative[0])
    last = int(relative[1])
    if first in leftmost_index and last in leftmost_index:
        length = rightmost_index[last] - leftmost_index[first] + 1
        if length > max_length:
            max_length = length
        
print(max_length)
