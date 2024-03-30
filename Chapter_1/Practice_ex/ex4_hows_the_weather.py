# Write a program to conveniently convert temperatures 
# measured in degrees Celsius to Fahrenheit instead.

# Celsius > Fahrenheit

# F > is a temperature in Fahrenheit
# C > is the same temperature in Celsius > -40 <= int => 40

# Formula > C = 5/9 * (F-32)
# Input > int > C
# Output > int > F > Equivalent to C

# 20 = 5/9 * (F-32)
# F = (20 / (5/9)) + 32

c = int(input())
f = (c / (5/9)) + 32
print(f)
