# CCC '18 J3 - Are we there yet?
# https://dmoj.ca/problem/ccc18j3

# Input : (4 + ints) < 1000 :: representing distance between pair 
#  of cities
# Output : 5 lines containing the distance from city 'i' to each
#  city in order, separated by one space.

# 1 leer input > 
# distances = [3, 10, 12, 5]

def distance(actual):
    for city in range(len(cities)):
        
        if city > actual:
            slicing = distances[actual:city]
            cities[city] = sum(slicing)
            slicing = []
        elif city == actual:
            cities[city] = 0
        else:
            slicing = distances[city:actual]
            cities[city] = sum(slicing)
            slicing = []
        city = 0
    return cities    
    

    

cities = [0, 0, 0, 0, 0]
distances = []
input_dis = input().split()

for d in input_dis:
    distances.append(int(d))


for actual in range(0,5):
    distance(actual)
    print(*cities)