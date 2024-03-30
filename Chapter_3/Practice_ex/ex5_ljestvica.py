# COCI '12 Contest 5 #1 Ljestvica
# https://dmoj.ca/problem/coci12c5p1

# A-minor > A D E > 3rd tone interval > 3ST
# C-major > C F G > 3rd tone interval > 4ST

a_main = "ADE"
c_main = "CFG"
separator = "|"

count_a = 0
count_c = 0

#input = "CD|EC|CD|EC|EF|G|EF|B|GAGA"
#input = "BC|BC|BC|BA"


input = str(input())
flag = True

for i in input:

    if i == separator:
        flag = True
        continue
    else:
        pass

    if flag == True:
        if i in a_main:
            count_a += 1
            flag = False
        elif i in c_main:
            count_c += 1
            flag = False
        else:
            flag = False
    else:
        continue

if count_a > count_c:
    #print("Count A", count_a , "Count C", count_c )
    print("A-mol")
elif count_c > count_a:
    #print("Count C", count_c, "Count A", count_a)
    print("C-dur")
else:
    if input[-1] == "A":
        print("A-mol")
    else:
        print("C-dur")