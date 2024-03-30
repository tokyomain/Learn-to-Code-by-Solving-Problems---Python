# CCC '18 J2 - Occupy parking
# https://dmoj.ca/problem/ccc18j2

# Input Specification :

# Input 1 : The first line contains integer n, the number of 
# parking spaces. n is between 1 and 100.

# Input 2 : The second line contains a string of n characters for 
# yesterday’s information, one character for each parking space. 
# A 'C' indicates an occupied parking space (C for car), and
#  a '.' indicates an empty parking space.

# Input 3 : The third line contains a string of n characters for 
# today’s information, in the same format as the second line.

# Output : Output the number of parking spaces that were occupied 
# on both days.

n = int(input())
yesterday = input()
today = input()

occupied = 0

for i in range(len(yesterday)):
    if yesterday[i] == ('C' or 'c') and today[i] == ('C' or 'c'):
        occupied = occupied + 1
    
print(occupied)