# ECOO '17 R1 P1 - Munch 'n' Brunch / School Trip
# https://dmoj.ca/problem/ecoo17r1p1

# 1 cost of the school trip
# 2 proportion of students each year
# 3 total number of students.


YEAR_COSTS = [12, 10, 7, 5]

for dataset in range(10):
    trip_cost = int(input())
    proportions = input().split()
    num_students = int(input())

    for i in range(len(proportions)):
        proportions[i] = float(proportions[i])

    students_per_year = []

    for proportion in proportions:
        students = int(num_students*proportion)
        students_per_year.append(students)

    counted = sum(students_per_year)
    uncounted = num_students - counted
    most = max(students_per_year)
    where = students_per_year.index(most)
    students_per_year[where] = students_per_year[where] + uncounted

    total_raised = 0

    for i in range(len(students_per_year)):
        total_raised = total_raised + students_per_year[i] * YEAR_COSTS[i]
    
    if total_raised / 2 < trip_cost:
        print('YES')
    else:
        print('NO')