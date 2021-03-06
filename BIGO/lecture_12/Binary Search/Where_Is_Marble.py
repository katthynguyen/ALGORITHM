# python 3
def inp():
    return map(int, input().split(' '))
    
def bsFirst(a, left, right, x):
    if left <= right:
        mid = (left + right) // 2
        if (mid == left or x > a[mid - 1]) and a[mid] == x:
            return mid
        elif x > a[mid]:
            return bsFirst(a, mid + 1, right, x)
        else:
            return bsFirst(a, left, mid - 1, x)
    return -1

def BS_search(a, l, r, value):
    ans = -1
    while l <= r:
        mid = int( (l + r) / 2 )
        if a[mid] == value:
            ans = mid
            r = mid - 1
        elif a[mid] > value:
            r = mid - 1
        else:
            l = mid + 1
    return ans

def solve():
    testcase = 0
    while True:
        testcase += 1
        n, q = inp()
        if n == 0 and q == 0:
            break
        a = []
        for i in range(n):
            x = int(input())
            a.append(x)
        a.sort()
        print("CASE# " + str(testcase) + ":")
        for i in range(q):
            x = int(input())
            ans = bsFirst(a, 0, n-1, x)
            if ans == -1:
                print(str(x) + " not found")
            else:
                print(str(x) + " found at " + str(ans + 1))

solve()
# C++

"""
#include <bits/stdc++.h>
#define MAX 10005
using namespace std;

int a[MAX];

int BSFirst(int a[], int left, int right, int x) {
    if (left <= right) {
        int mid = left + (right - left) / 2;

        if (a[mid] == x && (mid == left || a[mid - 1] < x)) {
            return mid;
        }
        else if (a[mid] < x) {
            return BSFirst(a, mid + 1, right, x);
        }
        return BSFirst(a, left, mid - 1, x);
    }

    return -1;
}

int main() {
    int N, Q, x, t = 1;
    
    while (cin >> N >> Q) {
		if (N == 0 && Q == 0) {
			break;
		}
		
        for (int i = 0; i < N; i++) {
            cin >> a[i];
        }

        sort(a, a + N);
        cout << "CASE# " << t++ << ":" << endl;

        for (int i = 0; i < Q; i++) {
            cin >> x;
            int index = BSFirst(a, 0, N - 1, x);
            
            if (index == -1) {
                cout << x << " not found" << endl;
            }
            else {
                cout << x << " found at " << index + 1 << endl;
            }
        }
    }
    return 0;
}
"""

# JAVA
"""
import java.io.*;
import java.util.*;

class Main {
    
    public static int bsFirst(ArrayList<Integer> a, int left, int right, int x) {
        if (left <= right) {
            int mid = left + (right - left) / 2;
            if ((mid == 0 || x > a.get(mid - 1)) && a.get(mid) == x)
                return mid;
            else if (x > a.get(mid))
                return bsFirst(a, (mid + 1), right, x);
            else
                return bsFirst(a, left, (mid - 1), x);
        }
        return -1;
    }
    
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        ArrayList<Integer> a = new ArrayList<Integer>();
        int n, q, temp;
        int count = 1;
		
        while (true) {
            n = in.nextInt();
            q = in.nextInt();
            if (n == 0 && q == 0)
                break;
            for (int i = 0; i < n; i++) {
                temp = in.nextInt();
                a.add(temp);
            }
			
            int x;
            Collections.sort(a);
            System.out.printf("CASE# %d:\n", count++);
            for (int i = 0; i < q; i++) {
                x = in.nextInt();
                int result = bsFirst(a, 0, n - 1, x);
                if (result != -1) {
                    System.out.printf("%d found at ", x);
                    System.out.printf("%d\n", result+1);
                }
                else {
                    System.out.printf("%d not found\n", x);
                }
            }
            a.clear();
        }
        return;
    }
}
"""