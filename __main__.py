INF = float("inf")
V = 4 #вершины

def floyd(G):
    (f, s) = (lambda p: list(map(lambda q: q, p)), G)
    dist = list(map(f, s))

    for r in range(V):
        for p in range(V):
            for q in range(V):
                dist[p][q] = min(dist[p][q], dist[p][r] + dist[r][q])
    s_print(dist)

# Printing the output
def s_print(dist):
    for p in range(V):
        for q in range(V):
            if(dist[p][q] == INF):
                print("inf", end=" ")
            else:
                print(dist[p][q], end=" ")
        print(" ")

G = [[0, 6, INF, INF],
         [3, 0, 8, 5],
         [9, INF, 0, 6],
         [7, INF, 5, 0]]

floyd(G)
input()