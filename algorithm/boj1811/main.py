

n, m, b = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

max_n = -10**10
min_n = 10**10

best_time = 10**30
best_h = -1

for i in range(n):
    for j in range(m):
        max_n = max(board[i][j], max_n)
        min_n = min(board[i][j], min_n)


for h in range(min_n, max_n+1):
    remove = 0
    add = 0

    for i in range(n):
        for j in range(m):
            mine = board[i][j]

            if mine > h:
                remove += (mine - h)    
            elif mine < h:
                add += (h - mine)

    if b + remove < add:
        continue

    time = 2 * remove + add


    if time < best_time or (time == best_time and h > best_h):
        best_time = time
        best_h = h

print (best_time, best_h)