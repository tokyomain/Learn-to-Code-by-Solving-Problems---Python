# USACO 2013 December Contest, Bronze / Problem 2. Cow Baseball
# http://usaco.org/index.php?page=viewproblem2&cpid=359

from bisect import bisect_left, bisect_right

#        //////////     {  Functions  }     //////////


#       //////////     {  Main Program  }     //////////   

input_file = open('baseball.in', 'r')
output_file = open('baseball.out', 'w')

n = int(input_file.readline())

positions = []

for i in range(n):
    positions.append(int(input_file.readline()))    

positions.sort()                                     #1

total = 0

for i in range(n):                                    #2
    for j in range(i + 1, n):                         #3
        first_two_diff = positions[j] - positions[i]
        low = positions[j] + first_two_diff
        high = positions[j] + first_two_diff * 2
        left = bisect_left(positions, low)
        right = bisect_right(positions, high)
        total = total + right - left

output_file.write(str(total) + '\n')

input_file.close()
output_file.close()