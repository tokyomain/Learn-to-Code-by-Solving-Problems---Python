# CCC '18 S1 - Voronoi Villages
# https://dmoj.ca/problem/ccc18s1


list_villages = []
size_list = []
numberOfVillages = int(input())

for i in range(numberOfVillages):
    list_villages.append(int(input()))

list_villages.sort()

for v in list_villages:
    if v == list_villages[0]: 
        continue
    elif v == list_villages[-1]:
        continue
    else:
        v_index = list_villages.index(v)
        l_index = v_index - 1
        r_index = v_index + 1
        size = (list_villages[v_index] - list_villages[l_index]) / 2 + (list_villages[r_index] - list_villages[v_index]) / 2
        size_list.append(size)

size_list.sort()

print(size_list[0])