# EX_1
"""
                    Fashion in Bertland
According to rules of the Berland fashion, 
a jacket should be fastened by all the buttons except only one, 
but not necessarily it should be the last one. 
Also if the jacket has only one button, it should be fastened, 
so the jacket will not swinging open.
You are given a jacket with N buttons. Determine if it is fastened in a right way.
"""

def checkJacket(v, n):
    if n == 1:
        if v[0] == 1:
            return True
        else:
            return False
    count = 0
    for i in range(n):
        if v[i] == 0:
            count += 1
    if count == 1:
        return True
    else:
        return False
 
 
n = int(input())
v = list(map(int, input().split()))
 
if checkJacket(v, n):
    print("YES")
else:
    print("NO")
