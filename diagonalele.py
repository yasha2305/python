matrix = []

for i in range(3):
    matrix.append(list(map(int, input().split())))

print("Diagonal Elements:")
for i in range(3):
    print(matrix[i][i])