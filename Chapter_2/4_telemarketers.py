
# The Challenge

# In this problem, we’ll assume that phone numbers are four
#  digits. A phone number belongs to a telemarketer if its
#  four digits satisfy all three of the following properties:
# The first digit is 8 or 9.
# The fourth digit is 8 or 9.
# The second and third digits are the same.

# Determine whether a phone number belongs to a telemarketer,
# and indicate whether we should answer the phone or ignore it.

# Input : There are four lines of input. These lines give the
#  first, second, third, and fourth digits of the phone 
# number, respectively. Each digit is an integer between 0 
# and 9.

# Output : If the phone number belongs to a telemarketer,
# output ignore; otherwise, output answer.


first = int(input())
second = int(input())
third = int(input())
fourth = int(input())

if ((first == 8 or first == 9) and 
    (fourth == 8 or fourth == 9) and
    (second == third)):
    print('ignore')
else:
    print('answer')
