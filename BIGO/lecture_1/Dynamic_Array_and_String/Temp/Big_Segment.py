n = int(input())
L ,R = [],[]

for _ in range(n):
    a,b = map(int,input().split())
    L.append(a)
    R.append(b)

left ,right = min(L),max(R)
for i in range(n):
    if left == L[i] and right == R[i]:
        print(i + 1)
        exit()
        
print(-1)