#  python 3
maxCost = [[None] * 85 for _ in range(85)]
INF = 10 ** 9
t = 1

def FloydWarshall():
    for _ in range(2):
        for k in range(1, C + 1):
            for i in range(1, C + 1):
                for j in range(1, C + 1):
                    maxFeast = max(maxCost[i][k], maxCost[k][j])
                    if dist[i][j] + maxCost[i][j] > dist[i][k] + dist[k][j] + maxFeast:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        maxCost[i][j] = maxFeast

while True:
    C, R, Q = map(int, input().split())

    if C == 0:
        break
    
    f = [0] + list(map(int, input().split()))
    
    for i in range(1, C + 1):
        for j in range(1, C + 1):
            maxCost[i][j] = max(f[i], f[j])

    dist = [[INF] * (C + 1) for _ in range(C + 1)]

    for _ in range(R):
        u, v, w = map(int, input().split())
        dist[u][v] = dist[v][u] = w
    
    FloydWarshall()

    if t > 1:
        print()
    
    print('Case #{}'.format(t))
    t += 1

    for _ in range(Q):
        u, v = map(int, input().split())
        print(-1 if dist[u][v] == INF else dist[u][v] + maxCost[u][v])

# C++

"""
#include <bits/stdc++.h>
#define MAX 85
using namespace std;
const int INF = 1e9 + 7;

int C, R;
int dist[MAX][MAX];
int maxCost[MAX][MAX];
int f[MAX];

void FloydWarshall() {
    int times = 2;

    while (times--) {
        for (int k = 1; k <= C; k++) {
            for (int i = 1; i <= C; i++) {
                for (int j = 1; j <= C; j++) {
                    int maxFeast = max(maxCost[i][k], maxCost[k][j]);
                    if (dist[i][j] + maxCost[i][j] > dist[i][k] + dist[k][j] + maxFeast) {
                        dist[i][j] = dist[i][k] + dist[k][j];
                        maxCost[i][j] = maxFeast;
                    }
                }
            }
        }
    }
}

int main() {
    int u, v, w, Q, t = 1;

    while (cin >> C >> R >> Q) {
        if (C == 0) {
            break;
        }

        for (int i = 1; i <= C; i++) {
            cin >> f[i];
        }

        for (int i = 1; i <= C; i++) {
            for (int j = 1; j <= C; j++) {
                dist[i][j] = INF;
                maxCost[i][j] = max(f[i], f[j]);
            }
        }

        for (int i = 0; i < R; i++) {
            cin >> u >> v >> w;
            dist[u][v] = dist[v][u] = w;
        }

        FloydWarshall();

        if (t > 1) {
            cout << endl;
        }
        cout << "Case #" << t++ << endl;

        for (int i = 0; i < Q; i++) {
            cin >> u >> v;
            cout << (dist[u][v] == INF ? -1 : dist[u][v] + maxCost[u][v]) << endl;
        }
    }
    return 0;
}
"""

# JAVA
"""
import java.util.*;

public class Main {
    static final int INF = (int)1e9 + 7;
    static final int MAX = 85;
    static int C, R;
    static int[] f = new int[MAX];
    static int[][] dist = new int[MAX][MAX];
    static int[][] maxCost = new int[MAX][MAX];

    public static void FloydWarshall() {
        int times = 2;

        while (times-- > 0) {
            for (int k = 1; k <= C; k++) {
                for (int i = 1; i <= C; i++) {
                    for (int j = 1; j <= C; j++) {
                        int maxFeast = Math.max(maxCost[i][k], maxCost[k][j]);
                        if (dist[i][j] + maxCost[i][j] > dist[i][k] + dist[k][j] + maxFeast) {
                            dist[i][j] = dist[i][k] + dist[k][j];
                            maxCost[i][j] = maxFeast;
                        }
                    }
                }
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = 1;

        while (true) {
            C = sc.nextInt();
            R = sc.nextInt();
            int Q = sc.nextInt();

            if (C == 0) {
                break;
            }

            for (int i = 1; i <= C; i++) {
                f[i] = sc.nextInt();
            }

            for (int i = 1; i <= C; i++) {
                for (int j = 1; j <= C; j++) {
                    dist[i][j] = INF;
                    maxCost[i][j] = Math.max(f[i], f[j]);
                }
            }

            for (int i = 0; i < R; i++) {
                int u = sc.nextInt();
                int v = sc.nextInt();
                int w = sc.nextInt();
                dist[u][v] = dist[v][u] = w;
            }

            FloydWarshall();

            if (t > 1) {
                System.out.println();
            }
            System.out.println("Case #" + t++);

            for (int i = 0; i < Q; i++) {
                int u = sc.nextInt();
                int v = sc.nextInt();
                System.out.println(dist[u][v] == INF ? -1 : dist[u][v] + maxCost[u][v]);
            }
        }
    }
}
"""