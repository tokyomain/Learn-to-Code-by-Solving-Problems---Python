# --------------------------------

# The Challenge
# In basketball, three plays score points: a three-point shot,
#  a two-point shot, and a one-point free throw.
# You just watched a basketball game between the Apples and
#  Bananas and recorded the number of successful three-point,
#  two-point, and onepoint plays for each team. Indicate whether 
# the game was won by the Apples, the game was won by the Bananas,
#  or the game was a tie.

# ---------------------------------

# Input A: Apples Succesfull 3-point shots
# Input B: Apples Succesfull 2-point shots
# Input C: Apples Succesfull 1-point shots

# Input D: Bananas Succesfull 3-point shots
# Input E: Bananas Succesfull 2-point shots
# Input F: Bananas Succesfull 1-point shots

# Each input >  ( 0 < int > 100 )

# Output : Single character > A : Apples Win
# Output : Single character > B : Bananas Win
# Output : Single character > T : Tie

apple_three = int(input())
apple_two = int(input())
apple_one = int(input())

banana_three = int(input())
banana_two = int(input())
banana_one = int(input())

apple_total = apple_three *3  + apple_two * 2 + apple_one
banana_total = banana_three *3  + banana_two * 2 + banana_one

if apple_total > banana_total:
    print('A')
elif banana_total > apple_total:
    print('B')
else:
    print('T')

    