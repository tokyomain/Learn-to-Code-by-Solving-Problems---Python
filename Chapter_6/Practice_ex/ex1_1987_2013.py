# CCC '13 S1 - From 1987 to 2013
# https://dmoj.ca/problem/ccc13s1

# Given a year, what is the next year with distinct digits?

# Input: int: Y (0 <= Y <= 10.000) representing the starting year.
# Ouput: int: D representing the next year after Y with distinct digits.

# A partir del num Y sumarle 1
# chequear si se repite digito.
#    Si repite, next
#    Si no, return year > end.

def have_doubles(year):
    year = str(year)
    lst = []
    for ch in year:
        if ch not in lst:
            lst.append(ch)
        else:
            doubles = 'yes'
            return doubles
    doubles = 'no'
    return doubles
    

input_num = int(input())
year = input_num
doubles = 'yes'

while True:
    year = year + 1
    doubles = have_doubles(year)
    if doubles == 'no':
        print(year)
        break
    else:
        continue
    


