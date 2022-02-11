"""
Consum:
    T : total free time
    N : total books
    Ai : minutes to read the i-th book
    i(1->th)
    => MAX(N(i-th))
--------------------------------
Input: 
    1 : N, T : the number of books, the number of free minutes he got's
    2: A(0,i) the number of minutes need to read i-th books
Output:
    The maximum number of the books valery can read
"""

# N: The number of books, the number of free minutes valery got's
N,T = list(map(int,input().split()))

# minutes to read the i-th books
A = list(map(int,input().split()))

max = A[0]
def max_Read_Book(N,T,A):
    for i in A:
        
max_Read_Book(N,T,A)
