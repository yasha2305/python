matrix = []

for i in range(2):
    matrix.append(list(map(int, input().split())))

print("Transpose:")
for i in range(2):
    for j in range(2):
        print(matrix[j][i], end=" ")
    print()