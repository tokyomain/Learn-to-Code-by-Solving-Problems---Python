# CCC '07 J3 - Deal or No Deal Calculator
# https://dmoj.ca/problem/ccc07j3


# calculating the average of the remaining amounts 
# comparing that value to the "Banker's" offer
#  If the offer is higher than the average, then the player 
# should "deal". Otherwise, the player should say "no deal"

# input 1: n (1 <= n < 10) > opened cases
# input 2: list of int > x(1<= x <= 10)

listing = [100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 
           500000, 1000000]
out = []
opened = []
opened_num = int(input())

for case in range(opened_num):
    case_num = int(input())
    opened.append(case_num)

offer = int(input())

for index in opened:
    out.append(listing[index-1])

for n in out:
    listing.remove(n)    

average = sum(listing)/len(listing)   
if offer > average:
    print('deal')
else:
    print('no deal')
