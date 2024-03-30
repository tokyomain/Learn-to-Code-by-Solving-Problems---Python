# CCC '00 S1 - Slot Machines
# https://dmoj.ca/problem/ccc00s1


# Martha's money left:
quarters = int(input())

# Number of plays since the last payment for each machine:
first = int(input())
second = int(input())
third = int(input())

# N of Martha's plays: 
plays = 0

# Slot machine Martha's will play next
machine = 0

# Solution :

while quarters >= 1:

    quarters -= 1

    if machine == 0:
        first += 1
        if first == 35:
            first = 0
            quarters += 30
    elif machine == 1:
        second += 1
        if second == 100:
            second = 0
            quarters += 60
    elif machine == 2:
        third += 1
        if third == 10:
            third = 0
            quarters += 9
        
    plays += 1

    # Move to the next machine:
    machine += 1

    # We want to start over at machine 0, we add a check: 
    if machine == 3:
        machine = 0

print("Martha plays", plays, "times before going broke.")

