# COCI '13 Contest 3 #1 Riječi
# https://dmoj.ca/problem/coci13c3p1

# After "K" times of pressing the button, how much letters A 
# and how much letters B will be displayed on the screen?

# Input : K ( 1 <= K <= 45)

# Output : he first and only line of output must contain two 
# space-separated integers, the number of letters A and the 
# number of letters B.

# Conditions > B > BA
#            > A > B

# Pattern: 
# 1 : A  > B  >........................0 1
# 2 : B  > BA >........................1 1
# 3 : BA > BAB >.......................1 2
# 4 : BAB > BABBA >....................2 3
# 5 : BABBA > BABBABAB >...............3 5
# 6 : BABBABAB > BABBABABBABBA >.......5 8

input = int(input())
n1, n2 = 0, 1
sum = n1 + n2

for n in range(0, input-1):
    n1 = n2
    n2 = sum
    sum = n1 + n2
    
print(n1, n2)
    

