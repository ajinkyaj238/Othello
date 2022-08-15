game_hashmap = {0: [1,2,3,4,10], 1: [2,3,4,5,123]}
matrix = [row for row in game_hashmap.values()]
print(matrix)
for i in range(len(matrix)):
    for j in matrix[i]:
        print(j)