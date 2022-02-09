# python 3
n, k = map(int, input().split())
a = list(map(int, input().split()))

sum_energy = sum(a)

left = 0
right = 1000
while right - left > 1e-7:
    mid = (left + right) / 2
    sum_transfer = 0
    for x in a:
        if x > mid:
            sum_transfer += x - mid
    if mid * n < sum_energy - sum_transfer * k / 100:
        left = mid
    else:
        right = mid

print('%.9f' % left)
# C++

"""
#include <iostream>
#include <cstdio>
using namespace std;
#define MAX 10000
#define MAX_A 1000
int n, k, A[MAX];
double sumEnergy, sumTransfer, _left, _right, mid;

int main() {
    scanf("%d %d", &n, &k);
    sumEnergy = 0;
    for (int i = 0; i < n; i++) {
        scanf("%d", &A[i]);
        sumEnergy += A[i];
    }
    
    _left = 0;
    _right = MAX_A;
    while (_right - _left > 1e-7) {
        mid =(_left + _right) / 2;
        sumTransfer = 0;
        for (int i = 0; i < n; i++) {
            if (A[i] > mid)
                sumTransfer += A[i] - mid;
        }
        if (mid * n < sumEnergy - sumTransfer*k/100) {
        	_left = mid;
        }
        else {
        	_right = mid;
        }
    }
    printf("%.9f", _left);
    return 0;
}
"""


# JAVA
"""
import java.util.*;
import java.io.*;


public class Main
{ 
    static PrintWriter out = new PrintWriter(new BufferedOutputStream(System.out), true);
    static MyScanner in = new MyScanner();
    static final int MAX = 10000;
    static final int MAX_A = 1000;
    static int n, k;
    static int A[] = new int[MAX];
    static double sumEnergy, sumTransfer, _left, _right, mid;
    

    public static void main(String[] args) {
        n = in.nextInt();
        k = in.nextInt();
        sumEnergy = 0;
        for (int i = 0; i < n; i++) {
            A[i] = in.nextInt();
            sumEnergy += A[i];
        }

        _left = 0;
        _right = MAX_A;
        while (_right - _left > 1e-7) {
            mid =(_left + _right) / 2;
            sumTransfer = 0;
            for (int i = 0; i < n; i++) {
                if (A[i] > mid)
                    sumTransfer += A[i] - mid;
            }
            if (mid * n < sumEnergy - sumTransfer*k/100) {
                    _left = mid;
            }
            else {
                    _right = mid;
            }
        }
        out.printf("%.9f", _left);
    }

    public static class MyScanner {
        BufferedReader br;
        StringTokenizer st;

        public MyScanner() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }
        String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                        st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                        e.printStackTrace();
                }
            }
            return st.nextToken();
        }
        int nextInt() {
                return Integer.parseInt(next());
        }
        long nextLong() {
                return Long.parseLong(next());
        }
        double nextDouble() {
                return Double.parseDouble(next());
        }
        String nextLine() {
            String str = "";
            try {
                str = br.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }
    }
}
"""