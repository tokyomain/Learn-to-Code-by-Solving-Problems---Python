# USACO 2018 January Contest, Bronze / Problem 2. Lifeguards
# http://usaco.org/index.php?page=viewproblem2&cpid=784

#        //////////     {  Functions  }     //////////

def num_covered(intervals, fired):
    """
    intervals is a list of lifeguard intervals;
    each interval is a [start, end] list.
    fired is the index of the lifeguard to fire.

    Return the number of time units covered by all lifeguards
    except the one fired.
    """
    covered = set()                                       #1
    for i in range(len(intervals)):
        if i != fired:
            interval = intervals[i]
            for j in range(interval[0], interval[1]):     #2
                covered.add(j)                            #3
    return len(covered)



#       //////////     {  Main Program  }     //////////   

input_file = open('lifeguards.in', 'r')
output_file = open('lifeguards.out', 'w')

# Reading the number of lifeguards 
n = int(input_file.readline())

intervals = []

# Read each lifeguard’s time interval
for i in range(n):
    interval = input_file.readline().split()
    # Convert each of its components to an integer
    interval[0] = int(interval[0])
    interval[1] = int(interval[1])
    # Append it as a two-value list to our list of intervals
    intervals.append(interval)

# Track the maximum number of time units that can be covered
max_covered = 0

# Separately fire each lifeguard using a range for loop
for fired in range(n):
    result = num_covered(intervals, fired)
    if result > max_covered:
        max_covered = result

output_file.write(str(max_covered) + '\n' )

input_file.close()
output_file.close()