# 3
# 7   20  88

n = int(input())
v= list(map(int,input().split()))

t = 0
for i in range(n):
    if t + 15 < v[i]:
        print(t + 15)
        exit()
    else:
        t = v[i]
print(min(90,t+15))