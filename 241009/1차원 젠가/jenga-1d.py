n = int(input())
jenga = [int(input()) for _ in range(n)]
s1, e1 = map(lambda x: int(x) - 1, input().split())
s2, e2 = map(lambda x: int(x) - 1, input().split())

first_step_jenga = [0]*n
end_idx_first_step = 0

for i in range(n):
    if not (s1 <= i <= e1):
        first_step_jenga[end_idx_first_step] = jenga[i]
        end_idx_first_step += 1

second_step_jenga = [0] * end_idx_first_step
end_idx_second_step = 0
for i in range(end_idx_first_step):
    if not (s2 <= i <= e2):
        second_step_jenga[end_idx_second_step] = first_step_jenga[i]
        end_idx_second_step += 1

print(end_idx_second_step)
for i in range(end_idx_second_step):
    print(second_step_jenga[i])