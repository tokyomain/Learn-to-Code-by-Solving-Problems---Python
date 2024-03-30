
# input A > int 'r' > radius of the cone
# input B > int 'h' > height of the cone
# formula to calculate volume > (pi.r**2.h) / 3

# import math

radius = int(input('Enter the radius of the cone:'))
height = int(input('Enter the height of the cone:'))
# PI = math.pi
PI = 3.141592653589793

volume = (PI*radius**2*height)/3

print('Volume of the cone: ', volume)