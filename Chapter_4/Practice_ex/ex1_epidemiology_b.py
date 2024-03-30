p = int(input())
n = int(input())
r = int(input())

previous_day = n
day = 0

while n <= p:
    n += previous_day * r
    previous_day *= r

    day += 1

print(day)