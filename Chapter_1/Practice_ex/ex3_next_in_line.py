
# Their ages form an arithmetic sequence: the difference in
#  ages between the middle child and youngest child is the
#  same as the difference in ages between the oldest child 
# and the middle child.

# Input A > Y > int > age of the Youngest child
# Inpyt B > M > int > age of the Middle child
# Output > O > int > age of the Oldest child

# Given the ages of the youngest and middle children, 
# what is the age of the oldest child?

youngest = int(input())
middle = int(input())

difference = middle - youngest
oldest = middle + difference
print(oldest)