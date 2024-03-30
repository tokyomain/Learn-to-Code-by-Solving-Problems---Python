
# CCC '15 J2 - Happy or Sad > https://dmoj.ca/problem/ccc15j2

happy = ':-)'
sad = ':-('

text = str(input())


count_happy = text.count(happy)
count_sad = text.count(sad)

if (count_happy == 0) and (count_sad == 0):
    print('none')
elif count_happy > count_sad:
    print('happy')
elif count_sad > count_happy:
    print('sad')
else:
    print('unsure')
