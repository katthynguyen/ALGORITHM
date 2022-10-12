# given two array A,B consisting of integer
# 3   3
# 2   1
# 1   2   3
# 3   4   5

na, nb = map(int,input().split())
k, m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

print("YES") if a[k-1] < b[nb-m] else print("NO")