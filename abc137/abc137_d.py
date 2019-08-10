# -*- coding: utf-8 -*-
## 断念

from operator import itemgetter

n, m = map(int, input().split())

# A日後、報酬B
workList = []
for i in range(n):
    a, b = map(int, input().split())
    workList.append({'day':a, 'value':b, 'used':False})
# print(workList)

# 報酬順にソート
workList = sorted(workList, key=itemgetter('value'), reverse=True)
# print(workList)

# 仕事予定リスト
plan = [0] * m

for i, work in enumerate(workList):
    # 空いており、使われていなければ設定
    if (not work['used']) & plan[work['day']-1] == 0:
        plan[work['day']-1] = work['value']
        workList[i]['used'] = True


print(plan)
print(workList)
