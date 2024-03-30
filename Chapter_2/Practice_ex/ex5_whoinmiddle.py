# CCC '07 J1 - Who is in the Middle?
# https://dmoj.ca/problem/ccc07j1


one = int(input())
two = int(input())
three = int(input())

if ((one > two) and (one < three)) or ((one > three) and (one < two)) :
    print(one)
elif ((two > one) and (two < three)) or ((two > three) and(two < one)):
    print(two)
else:
    print(three)