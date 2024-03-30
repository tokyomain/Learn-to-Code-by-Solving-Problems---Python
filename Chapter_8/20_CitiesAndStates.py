# USACO 2016 December Silver Contest problem Cities and States
# http://usaco.org/index.php?page=viewproblem2&cpid=667

#  SCRANTON PA    ///    PARKER SC
# This pair of cities is special because the first two characters 
# of each city give the abbreviation for the other city’s state. 


# keys : state
# values : cities

# INPUT /////

# n = number of cities 1< n > 200.000
# n lines, one per city
# each line gives the name of a city in uppercase,
# a space, and its state's abbreviation in uppercase.

# the name of each city is between 2 and 10 characters.
# the abb is exactly 2 char.
# the same name can exist in mutiple states but not appear more than
# once in the same state.

# OUTPUT /////

# Write output to the file named citystate.out
# Output the NUMBER of SPECIAL pairs of cities
# time limit for each test case: 4 sec

#        //////////     {  Functions  }     //////////

#       //////////     {  Main Program  }     //////////   


input_file = open('citystate.in', 'r')
output_file = open('citystate.out', 'w')

n = int(input_file.readline())

combo_to_num = {}

for i in range(n):
    lst = input_file.readline().split()
    city = lst[0][:2]
    state = lst[1]

    #    Building dictionary
    if city != state:
        combo = city + state
        if not combo in combo_to_num:
            combo_to_num[combo] = 1
        else:
            combo_to_num[combo] = combo_to_num[combo] + 1


total = 0

#    Loop through dict Keys
for combo in combo_to_num:
    #    We construct the other combo that we need to look up to find special pairs
    other_combo = combo[2:] + combo[:2]
    if other_combo in combo_to_num:
        total = total + combo_to_num[combo] * combo_to_num[other_combo]

output_file.write(str(total // 2) + '\n')

input_file.close()
output_file.close()