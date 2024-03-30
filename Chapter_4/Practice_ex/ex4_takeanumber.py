# ECOO '13 R1 P1 - Take a Number
# https://dmoj.ca/problem/ecoo13r1p1

# Opens 8hs - 15hs

# Input 1 : int > N ( 0 < N < 1000 ) > next number in the machine.
# 2 : n lines > activity at the attendance desk.
# TAKE > student has arrived and taken the next number N.
# SERVE > attendance secretary has served the next student in line.
# CLOSE > desk has closed, remaining students still served
# Last line will contains the string EOF. 
# never will there be more than 999 students waiting.

# Your job is to keep track of the line.
# Each time you encounter the word CLOSE, you must print 3 integers 
# on a single line, each separated by a single space. 
# 1st : number of students who were late that day.
# 2nd : number of students who remained in line after desk closed.
# 3rd : next number in the machine for the next day. 

condition = True
dormilones = 0
esperando = 0

machine = int(input())

while condition == True:
    word = input()
    if word == 'TAKE':
        if esperando >= 999:
            break
        dormilones += 1
        machine += 1
        esperando += 1
        if machine >= 999:
            machine = 1
        else:
            continue
    elif word == 'SERVE':
        if esperando >= 999:
            break
        esperando -= 1
        if machine >= 999:
            machine = 1
        else:
            continue
    elif word == 'CLOSE':
        if esperando >= 999:
            break
        print(f"{dormilones} {esperando} {machine}")
        esperando = 0
        dormilones = 0
        if machine >= 999:
            machine = 1
        else:
            continue
    else:
        condition = False
        
    