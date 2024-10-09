n, t = map(int, input().split())

top_line = list(map(int, input().split()))
bot_line = list(map(int, input().split()))

for _ in range(t):
    top_temp = top_line[n-1]
    for i in range(n-1, 0, -1):
        top_line[i] = top_line[i-1]
    
    bot_temp = bot_line[n-1]
    top_line[0] = bot_temp

    for i in range(n-1, 0, -1):
        bot_line[i] = bot_line[i-1]
    
    bot_line[0] = top_temp


print(*top_line)
print(*bot_line)