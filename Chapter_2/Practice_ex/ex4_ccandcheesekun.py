
# DMOPC '16 Contest 1 P0 - C.C. and Cheese-kun
# https://dmoj.ca/problem/dmopc16c1p0

# Input A : int > (1 <= W => 3) > Width of the pizza.
# Input B : int > (0 <= C => 100) > Percentage of the pizza
# covered in extra cheese.

# Output : A single line containing C.C.'s satisfaction
# with her order in the form: 
# ' C.C. is M satisfied with her pizza.'
# Here, M is a string describing her satisfaction, which 
# will be one of: absolutely, fairly or very.

width = int(input())
cheese = int(input())
m = None

if (width == 3) and (cheese >= 95):
    m = 'absolutely'
elif (width == 1) and (cheese <= 50):
    m = 'fairly'
else:
    m = 'very'

print(f'C.C. is {m} satisfied with her pizza.')