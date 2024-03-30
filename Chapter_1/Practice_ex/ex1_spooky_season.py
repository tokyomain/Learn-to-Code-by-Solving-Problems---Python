
# S(2<=S<=20) > int
# input > int S
# output > string > spooky word corresponding to the given
# value of S

# ex > S = 5 > Spoooooky

spookiness = int(input())
start = 'sp'
end = 'ky'
middle = 'o'

solution = start + (middle*spookiness) + end
print(solution)