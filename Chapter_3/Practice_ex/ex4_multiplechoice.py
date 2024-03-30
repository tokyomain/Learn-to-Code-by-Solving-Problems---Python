# CCC '11 S2 - Multiple Choice
# https://dmoj.ca/problem/ccc11s2

# Write a program that your teacher can use to grade one multiple
# choice test.

n_questions = int(input())

answer = ''
points = 0

for n in range(n_questions*2):
    answer += input()


for ans in range(n_questions):
    if answer[ans] == answer[ans + n_questions]:
        points += 1
    else:
        continue

print(points)