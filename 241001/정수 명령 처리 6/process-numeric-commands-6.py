from sys import stdin
import heapq

n = int(stdin.readline())
pq = []
for i in range(n):
    coms = list(stdin.readline().split())
    if coms[0] == "push":
        heapq.heappush(pq, -int(coms[1]))
    elif coms[0] == 'size':
        print(len(pq))
    elif coms[0] == 'empty':
        if pq:
            print(0)
        else:
            print(1)
    elif coms[0] == 'pop':
        if pq:
            print(-heapq.heappop(pq))
    elif coms[0] == 'top':
        if pq:
            print(-pq[0])