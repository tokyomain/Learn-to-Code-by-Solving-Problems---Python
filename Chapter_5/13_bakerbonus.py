# ECOO '17 R3 P1 - Baker Brie / Baker Bonus
# https://dmoj.ca/problem/ecoo17r3p1

# 1 : F > number of franchises
# 2 : D > days of information
# 3 : D lines > F int separated by spaces



for dataset in range(10):

    lst = input().split()
    franchisees = int(lst[0])
    days = int(lst[1])
    grid = []

    for i in range(days):
        row = input().split()
        # Transform into int:
        for j in range(franchisees):
            row[j] = int(row[j])
        grid.append(row)
    
    bonuses = 0

    for row in grid:
        total = sum(row)
        if total % 13 == 0:
            bonuses = bonuses + total // 13
        
    # Looping through indeces:
    for col_index in range(franchisees):
        total = 0
        for row_index in range(days):
            total = total + grid[row_index][col_index]
        if total % 13 == 0:
            bonuses = bonuses + total // 13
    
    print(bonuses)