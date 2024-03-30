# Write a program that will compute the total Calories of a 
# meal.

# Input : The program should input a number for each type of
#  item then calculate and display the Calorie total.

# Input A : Choice of burger
# Input B : Choice of side
# Input C : Choice of drink
# Input D : Choice of dessert

# Output : The program prints out the total Calories of the 
# selected meal, and stops executing after this output.

burger = int(input())
side = int(input())
drink = int(input())
dessert = int(input())

total_calorie = 0

if burger == 1:
    total_calorie += 461
elif burger == 2:
    total_calorie += 431
elif burger == 3:
    total_calorie += 420
else:
    total_calorie += 0

if side == 1:
    total_calorie += 100
elif side == 2:
    total_calorie += 57
elif side == 3:
    total_calorie += 70
else:
    total_calorie += 0

if drink == 1:
    total_calorie += 130
elif drink == 2:
    total_calorie += 160
elif drink == 3:
    total_calorie += 118
else:
    total_calorie += 0

if dessert == 1:
    total_calorie += 167
elif dessert == 2:
    total_calorie += 266
elif dessert == 3:
    total_calorie += 75
else:
    total_calorie += 0

total_calorie = str(total_calorie)
print('Your total Calorie count is '+total_calorie+'.')


