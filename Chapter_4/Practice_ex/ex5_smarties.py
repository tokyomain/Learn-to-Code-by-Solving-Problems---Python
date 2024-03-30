#  ECOO '15 R1 P1 - When You Eat Your Smarties
# https://dmoj.ca/problem/ecoo15r1p1
#  orange blue green, yellow, pink, violet, brown  red.


colors = 'orangebluegreenyellowpinkvioletbrown'
all = 0
reds = 0
timer = 0

for test in range(1):
    while True:
        smartie = str(input())
        if smartie == 'red':
            reds += 1
        elif smartie in colors:
            all += 1
        else:
            time_all = ((all // 7)*13)
            sobra = all%7
            if sobra != 0:
                time_all += 13
            else: 
                continue
            time_reds = reds * 16
            timer = time_all + time_reds
            print(timer, all, reds)
            all = 0
            reds = 0
            timer = 0
            break
