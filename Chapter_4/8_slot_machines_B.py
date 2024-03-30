# CCC '00 S1 - Slot Machines
# https://dmoj.ca/problem/ccc00s1


quarters = int(input())

first = int(input())
second = int(input())
third = int(input())

plays = 0

# Solution :

while quarters >= 1:
    machine = plays % 3               # new
    quarters -= 1

    if machine == 0:
        first += 1
        if first % 35 == 0:           # new
            quarters += 30
    elif machine == 1:
        second += 1
        if second % 100 == 0:         # new
            quarters += 60
    elif machine == 2:
        third += 1
        if third % 10 == 0:           # new
            quarters += 9
        
    plays += 1

#print("Martha plays", plays, "times before going broke.")
print(f'Martha plays {plays} times before going broke.')    # new