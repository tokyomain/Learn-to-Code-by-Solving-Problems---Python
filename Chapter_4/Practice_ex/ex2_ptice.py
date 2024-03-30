# COCI '08 Contest 1 #2 Ptice
# https://dmoj.ca/problem/coci08c1p2

# Write a program that, given the correct answers to the exam, 
# determines who of the three was right – whose sequence contains 
# the most correct answers.

# Input:
# 1 : int > N( 1<= N >= 100) > Number of questions > ie  5
# 2 : str > of N letters A, B, C > correct answers > BACBB 

# Output :
# 1 : M > largest number of correct answers.
# 2 : Names of the boys in alphabetical order si acertaron al menos una

names = ['Adrian', 'Bruno', 'Goran']
boys = [0, 1, 2]
sequence_list = ['ABCABCABCABC', 'BABCBABCBABC', 'CCAABBCCAABB']
points_list = [0, 0, 0]

quest = int(input())
correct = str(input())

sequence = ''
boys_names = 0

for boy in boys:
    sequence = sequence_list[boy]
    index = 0
    for ch in correct:
        if ch == sequence[index%(len(sequence))]:
            points_list[boy] += 1
            index+= 1
        else:
            index+= 1
            continue

maximum = max(points_list)           
print(maximum)
#print(points_list)

for points in points_list:
    if points == maximum:
        print(names[boys_names])
        boys_names += 1
    else:
        boys_names += 1