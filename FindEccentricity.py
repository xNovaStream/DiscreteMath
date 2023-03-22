with open("AdjacencyMatrix.txt") as file:
    adjacencyMatrix = [list(map(int, i.split(', '))) for i in file.read().split('\n')]

with open("Names.txt") as file:
    names = file.read().split('\n')

INF = 10**10
n = len(adjacencyMatrix)
distanceMatrix = [[INF] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            distanceMatrix[i][j] = 0
        elif adjacencyMatrix[i][j] == 1:
            distanceMatrix[i][j] = 1

for r in range(n):
    for p in range(n):
        for q in range(n):
            distanceMatrix[p][q] = min(distanceMatrix[p][q], distanceMatrix[p][r] + distanceMatrix[r][q])

eccentricities = [max(a) for a in distanceMatrix]

for i in range(n):
    print(names[i], eccentricities[i], sep=": ")
