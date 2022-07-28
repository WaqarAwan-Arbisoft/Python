def searchSortedMatrix(matrix, key):
    for row in matrix:
        for col in range(len(row)-1, -1, -1):
            if row[col] < key:
                break
            if(row[col] == key):
                return True

    return False


matrix = [[3, 4, 4, 6],
          [6, 8, 12, 12],
          [6, 8, 12, 15],
          [9, 12, 12, 17]]
print(searchSortedMatrix(matrix=matrix, key=11))
