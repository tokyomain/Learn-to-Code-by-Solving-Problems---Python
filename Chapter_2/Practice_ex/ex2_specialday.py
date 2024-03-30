# Write a program that asks the user for a numerical month
# and numerical day of the month and then determines whether 
# that date occurs before, after, or on February 18.

# Input : The input consists of two integers each on a 
# separate line. These integers represent a date.

# Output : Exactly one of Before, After, or Special will be
# printed on one line.

month = int(input())
day = int(input())

if month < 2 or (month == 2 and day < 18):
    print('Before')
elif month > 2 or (month == 2 and day > 18):
    print('After')
elif month == 2 and day == 18:
    print('Special')