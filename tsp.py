import math

def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def tsp(points):
    n = len(points)
    dp = [[float('inf')]*n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 0
    for k in range(1, n):
        for i in range(n):
            for j in range(n):
                if i != j and i != j-k and j != i-k:
                    dp[i][j] = min(dp[i][j], dp[i][j-k] + distance(points[i], points[j-k]) + distance(points[j-k], points[j]))
    return min(dp[i][j] for i in range(n) for j in range(n))

def main():
    points = [[0, 0], [10, 0], [5, 3], [0, 5], [3, 4], [4, 3], [3, 0]]
    print(tsp(points))

if __name__ == '__main__':
    main()