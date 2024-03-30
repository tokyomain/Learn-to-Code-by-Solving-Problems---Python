# USACO 2014 January Contest, Bronze / Problem 1. Ski Course Design
#http://usaco.org/index.php?page=viewproblem2&cpid=376


# 'n' hills with height 0 < 'h' > 100
# A farm can be registered as a ski training camp only if the difference in
# height between the highest and lowest hills is 17 or less.
# The cost of changing a hill’s height by x units is x*2.

# Determine the minimum amount that Farmer John will need to pay to change 
# the heights of hills so that he can register his farm as a ski training
# camp


#        //////////     {  Functions  }     //////////

MAX_DIFFERENCE = 17
MAX_HEIGHT = 100

def cost_for_range(heights, low, high):
    """
    heights is a list of hill heights.
    low is an integer giving the low end of the range.
    high is an integer giving the gigh end of a range.

    Return the cost of changing all heights of hills to be 
    between low and high.
    """
    cost = 0
    for height in heights:
        if height < low:
            cost = cost + (low - height) ** 2
        elif height > high:
            cost = cost + (height - high) ** 2
    return cost


#       //////////     {  Main Program  }     //////////   

input_file = open('skidesign.in', 'r')
output_file = open('skidesign.out', 'w')

n = int(input_file.readline())

heights = []

for i in range(n):
    heights.append(int(input_file.readline()))

min_cost = cost_for_range(heights, 0, MAX_DIFFERENCE)

for low in range(1, MAX_HEIGHT + 1):
    result = cost_for_range(heights, low, low + MAX_DIFFERENCE)
    if result < min_cost:
        min_cost = result

output_file.write(str(min_cost) + '\n' )

input_file.close()
output_file.close()
