N, C = map(int, input().split())
plans = [tuple(map(int, input().split())) for _ in range(N)]

cost = []
for a, b, c in plans:
    cost.append((a, c))
    cost.append((b+1, -c))
cost.sort()
current_cost = 0
current_day = 0
sum_cost = 0
for day, dc in cost:
    sum_cost += min(current_cost, C) * (day - current_day)
    current_day = day
    current_cost += dc
print(sum_cost)
