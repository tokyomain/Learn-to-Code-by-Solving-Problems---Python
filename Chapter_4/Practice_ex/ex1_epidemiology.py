# CCC '20 J2 - Epidemiology
# https://dmoj.ca/problem/ccc20j2

# Input :
# 1 : (int >= 0) > P > 
# 2 : (int >= 0) > N > Number of people that has the disease on day 0.
# 3 : (int >= 0) > R > Number of infected people per person with 
# disease, on next day.

# We want to determine when a total of more than P people have had
# the disease.

# Output : Output the number of the first day on which the total
# number of people who have had the disease is greater than P.

p = int(input())
n = int(input())
r = int(input())

day = 0
new_infected = n
total = n

while total <= p:
    new_infected = (new_infected * r) 
    total += new_infected 
    
    if total <= p:
        day +=1
    else:
        day +=1
        break
    
print(day)