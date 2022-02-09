# python 3
import math

def inp():
    return map(int, input().split(' '))

def f(p , q , r , s , t , u , x):
    return p * math.exp(-x) + q * math.sin(x) + r * math.cos(x) + s * math.tan(x) + t * x * x + u

def solve():
    while True:
        try:
            p, q, r, s, t, u = map(float, input().split(' '))

            if f(p, q, r, s, t, u, 1.0) > 1e-9 or p + r + u < 0:
                print("No solution")
                continue

            res = -1
            lo = 0.000
            hi = 1.000
            for i in range(100):
                mid = (lo + hi) / 2.0
                F = f(p, q, r, s, t, u, mid)
                if F > 0:
                    lo = mid
                else:
                    hi = mid
            print('{:0.4f}'.format(lo))
        except EOFError:
            break

solve()
# C++

"""
#include <bits/stdc++.h> 

using namespace std; 

const double eps = 1e-8; 

double f(double p , double q , double r , double s , double t , double u , double x) {
	return (p * exp(-x) + q * sin(x) + r * cos(x) + s * tan(x) + t * x * x + u);  
}

double p , q , r , s , t , u; 

int main () {
	while (cin >> p >> q >> r >> s >> t >> u) {
		double lo = 0.000; 
		double hi = 1.000;

		if (f(p , q , r , s , t , u , 1.0) > 1e-9 || p + r + u < 0) {
			cout << "No solution" << endl; 
			continue; 
		}

		double res = -1;  

		for (int i = 0; i <= 1000; i++) {
			double x = (lo + hi) / 2.0; 
			double F = f(p , q , r , s , t , u , x);

			if (F > 0) lo = x; 
			else hi = x; 
		}

		cout << fixed << setprecision(4) << lo << endl;  
	}
	return 0; 
} 
"""


# JAVA
"""
import java.io.*;
import java.util.*;

class Main {

    static final double eps = 1e-8;

    public static double f(double p , double q , double r , double s , double t , double u , double x) {
        return (p * Math.exp(-x) + q * Math.sin(x)
                + r * Math.cos(x) + s * Math.tan(x) + t * x * x + u);
    }

    public static void main(String[] args) throws IOException {
        Scanner in = new Scanner(System.in);
        double p , q , r , s , t , u;

        while (in.hasNext()) {
            p = in.nextDouble();
            q = in.nextDouble();
            r = in.nextDouble();
            s = in.nextDouble();
            t = in.nextDouble();
            u = in.nextDouble();
            double lo = 0.000;
            double hi = 1.000;
            if (f(p , q , r , s , t , u , 1.0) > 1e-9 || p + r + u < 0) {
                System.out.println("No solution");
                continue;
            }
            double res = -1;
            for (int i = 0; i <= 1000; i++) {
                double x = (lo + hi) / 2.0;
                double F = f(p , q , r , s , t , u , x);

                if (F > 0)
                    lo = x;
                else
                    hi = x;
            }
            System.out.printf("%.4f\n", lo);
        }

        return;
    }
}
"""