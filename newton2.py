from collections import Counter
n=int(input())
l=[input().split() for i in range(n-1)]
li=[j for i in l for j in i]
co=dict(Counter(li))
ans="No"
for i in co.items():
    if i[1]==n-1:
        ans="Yes"
print(ans)
