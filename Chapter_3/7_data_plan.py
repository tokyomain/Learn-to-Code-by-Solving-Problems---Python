# COCI '16 Contest 1 #1 Tarifa
# https://dmoj.ca/problem/coci16c1p1

# x = megabytes of data per month.
# Any data unused in a given month carries over to the next.
# We are given the number of megabytes of data that Pero uses in 
# each of the first 'n' months.

# Input : 
# 1 > int 'x' > the number of megabytes given to Pero per month
# 1 < x > 100

# 2 > int 'n' > the number of months that Pero has had the data
# plan.
# 1 < n > 100

# 3 > 'n' lines > one for each month, giving the integer number
# of megabytes that Pero uses in that month.

# Output : The number of megabytes available for the next month.


monthly_mb = int(input())
n = int(input())

excess = 0


for i in range(n):
    used = int(input())
    excess = excess + monthly_mb - used

print( excess + monthly_mb)


# One alternative > 

'''
base = 0
used = 0

for i in range(n):
    used += int(input())
    base += monthly_mb

total = base - used + 10
print(total)'''