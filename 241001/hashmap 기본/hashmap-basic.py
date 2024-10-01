from sys import stdin

n = int(stdin.readline())
d = dict()
for i in range(n):
    coms = list(stdin.readline().split())
    if coms[0] == 'add':
        d[coms[1]] = coms[2]
    elif coms[0] == 'find':
        if coms[1] in d:
            print(d[coms[1]])
        else:
            print('None')
    elif coms[0] == 'remove':
        d.pop(coms[1])