# CCC '11 S1 - English or French?
# https://dmoj.ca/problem/ccc11s1

# t T > s S : English
# s S > t T : French
# s S = t T : French

# Input : 
# 1 > int > N
# N lines

# Output : English / French

english = ''
french = ''

n_lines = int(input())

for n in range(n_lines):
    line = input()
    for l in line:
        if l in 'tT':
            english += l
        elif l in 'sS':
            french += l
        else:
            pass


if len(english) > len(french):
    print('English')
elif len(french) > len(english):
    print('French')
else:
    print('French')