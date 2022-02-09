#  python 3

class Scanner:
    def __gen__():
        while True:
            buff = input().strip().split()
            for x in buff:
                yield x
    __sc__ = __gen__()
    def next():
        return Scanner.__sc__.__next__()

INF = 1029
MAX = 105
x = [None] * MAX
y = [None] * MAX
dist = [[0] * MAX for _ in range(MAX)]

def getDistance(i, j):
    return ((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2) ** 0.5

def FloydWarshall():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

N = int(Scanner.next())

for t in range(1, N + 1):
    n = int(Scanner.next())
    
    for i in range(n):
        for j in range(n):
            dist[i][j] = (0 if i == j else INF)
    
    for i in range(n):
        x[i] = int(Scanner.next())
        y[i] = int(Scanner.next())
    
    for i in range(n):
        for j in range(n):
            d = getDistance(i, j)
            if d <= 10:
                dist[i][j] = d
    
    FloydWarshall()

    res = 0
    for i in range(n):
        for j in range(n):
            res = max(res, dist[i][j])
    
    print('Case #{}:'.format(t))
    print(res if res != INF else 'Send Kurdy')
    print()
# C++

"""
#include <bits/stdc++.h>
#define MAX 105
using namespace std;
const int INF = 2049;        
// Khoảng cách lớn nhất là từ điểm (0, 0) đến (1024, 1024) nên phải khởi tạo INF lớn hơn khoảng cách này

int n;
int x[MAX], y[MAX];
double dist[MAX][MAX];

double getDistance(int i, int j) {
    return sqrt(pow(x[i] - x[j], 2) + pow(y[i] - y[j], 2));
}

void FloydWarshall() {
    for (int k = 0; k < n; k++) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
            }
        }
    }
}

int main() {
    int N;
    cin >> N;
    
    for (int t = 1; t <= N; t++) {
        cin >> n;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                dist[i][j] = (i == j ? 0 : INF);
            }
        }

        for (int i = 0; i < n; i++) {
            cin >> x[i] >> y[i];
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                double d = getDistance(i, j);
                if (d <= 10) {
                    dist[i][j] = d;
                }
            }
        }

        FloydWarshall();
        double res = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                res = max(res, dist[i][j]);
            }
        }

        cout << "Case #" << t << ":" << endl;
        if (res != INF) {
            cout << fixed << setprecision(4) << res << endl;
        }
        else {
            cout << "Send Kurdy" << endl;
        }

        cout << endl;
    }
    return 0;
}
"""

# JAVA
"""
import java.util.*;

public class Main {
    static final int INF = 2049;
    static final int MAX = 105;
    static int n;
    static int[] x = new int[MAX], y = new int[MAX];
    static double[][] dist = new double[MAX][MAX];

    public static double getDistance(int i, int j) {
        return Math.sqrt(Math.pow(x[i] - x[j], 2) + Math.pow(y[i] - y[j], 2));
    }

    public static void FloydWarshall() {
        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    dist[i][j] = Math.min(dist[i][j], dist[i][k] + dist[k][j]);
                }
            }
        }
    }

    public static void main(String[] agrs) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        for (int t = 1; t <= N; t++) {
            n = sc.nextInt();

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    dist[i][j] = (i == j ? 0 : INF);
                }
            }

            for (int i = 0; i < n; i++) {
                x[i] = sc.nextInt();
                y[i] = sc.nextInt();
            }

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    double d = getDistance(i, j);
                    if (d <= 10) {
                        dist[i][j] = d;
                    }
                }
            }

            FloydWarshall();

            double res = 0;
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    res = Math.max(res, dist[i][j]);
                }
            }

            System.out.println("Case #" + t + ":");
            if (res != INF) {
                System.out.printf("%.4f\n", res);
            }
            else {
                System.out.println("Send Kurdy");
            }
            System.out.println();
        }
    }
}
"""