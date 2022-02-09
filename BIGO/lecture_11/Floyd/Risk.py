#  python 3
N = 20
t = 1

def FloydWarshall():
    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

while True:
    try:
        dist = [[10 ** 9] * (N + 1) for _ in range(N + 1)]
        for i in range(1, N):
            for j in list(map(int, input().split()))[1:]:
                dist[i][j] = dist[j][i] = 1
        
        FloydWarshall()
        
        print("Test Set #{}".format(t))
        t += 1

        Q = int(input())
        for _ in range(Q):
            u, v = map(int, input().split())
            print('{:2d} to {:2d}: {}'.format(u, v, dist[u][v]))
        print()

    except EOFError:
        break

# C++

"""
#include <bits/stdc++.h>
#define N 20
using namespace std;
const int INF = 1e9 + 7;

int dist[N + 1][N + 1];

string formatted(int n) {
    return (n >= 10 ? to_string(n) : " " + to_string(n));
}

void FloydWarshall() {
    for (int k = 1; k <= N; k++) {
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= N; j++) {
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
            }
        }
    }
}

int main() {
    int X, Q, u, v, j, t = 1;

    while (true) {
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= N; j++) {
                dist[i][j] = INF;
            }
        }

        for (int i = 1; i < N; i++) {
            if (!(cin >> X)) {
                return 0;
            }

            while (X--) {
                cin >> j;
                dist[i][j] = dist[j][i] = 1;
            }
        }

        FloydWarshall();
        
        cout << "Test Set #" << t++ << endl;

        cin >> Q;
        for (int i = 0; i < Q; i++) {
            cin >> u >> v;
            cout << formatted(u) << " to " << formatted(v) << ": " << dist[u][v] << endl;
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
    static final int INF = (int)1e9 + 7;
    static final int N = 20;
    static int[][] dist = new int[N + 1][N + 1];

    public static void FloydWarshall() {
        for (int k = 1; k <= N; k++) {
            for (int i = 1; i <= N; i++) {
                for (int j = 1; j <= N; j++) {
                    dist[i][j] = Math.min(dist[i][j], dist[i][k] + dist[k][j]);
                }
            }
        }
    }
    
    public static void main(String[] agrs) {
        Scanner sc = new Scanner(System.in);
        int t = 1;

        while (sc.hasNext()) {
            for (int i = 1; i <= N; i++) {
                Arrays.fill(dist[i], INF);
            }

            for (int i = 1; i < N; i++) {
                int X = sc.nextInt();

                while (X-- > 0) {
                    int j = sc.nextInt();
                    dist[i][j] = dist[j][i] = 1;
                }
            }

            FloydWarshall();
            System.out.println("Test Set #" + t++);

            int Q = sc.nextInt();
            for (int i = 0; i < Q; i++) {
                int u = sc.nextInt();
                int v = sc.nextInt();
                System.out.format("%2d to %2d: %d\n", u, v, dist[u][v]);
            }
            System.out.println();
        }
    }
}
"""