# python 3
INF = 10 ** 9

def BellmanFord(s):
    dist = [INF] * (n + 1)
    dist[s] = 0

    for i in range(n):
        for edge in graph:
            u, v, w = edge
            
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                
                if i == n - 1:
                    return True
    
    return False

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    graph = []

    for i in range(m):
        u, v, w = map(int, input().split())
        graph.append((u, v, -w))
    
    print("Yes" if BellmanFord(1) else "No")

# C++
"""
#include <bits/stdc++.h>
#define MAX_N 105
#define MAX_M 1005
using namespace std;
const int INF = 1e9 + 7;

struct Edge {
    int source, target, weight;
};

int n, m;
int dist[MAX_N];
Edge graph[MAX_M];

bool BellmanFord(int s) {
    fill(dist, dist + (n + 1), INF);
    dist[s] = 0;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            int u = graph[j].source;
            int v = graph[j].target;
            int w = graph[j].weight;

            if (dist[u] != INF && dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;

                if (i == n - 1) {
                    return true;
                }
            }
        }
    }

    return false;
}

int main() {
    int T, u, v, w;
    cin >> T;

    while (T--) {
        cin >> n >> m;

        for (int i = 0; i < m; i++) {
            cin >> u >> v >> w;
            graph[i] = (Edge) {u, v, -w};
        }

        cout << (BellmanFord(1) ? "Yes" : "No") << endl;
    }
    return 0;
}
"""

# JAVA
"""
import java.util.*;

public class Main {
    static final int MAX_N = 105;
    static final int MAX_M = 1005;
    static class Edge {
        int source, target, weight;

        public Edge(int _source, int _target, int _weight) {
            this.source = _source;
            this.target = _target;
            this.weight = _weight;
        }
    }

    static int n, m;
    static int[] dist = new int[MAX_N];
    static Edge[] graph = new Edge[MAX_M];

    public static boolean BellmanFord(int s) {
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[s] = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                int u = graph[j].source;
                int v = graph[j].target;
                int w = graph[j].weight;

                if (dist[u] != Integer.MAX_VALUE && dist[u] + w < dist[v]) {
                    dist[v] = dist[u] + w;

                    if (i == n - 1) {
                        return true;
                    }
                }
            }
        }

        return false;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        
        while (T-- > 0) {
            n = sc.nextInt();
            m = sc.nextInt();

            for (int i = 0; i < m; i++) {
                int u = sc.nextInt();
                int v = sc.nextInt();
                int w = sc.nextInt();
                graph[i] = new Edge(u, v, -w);
            }

            System.out.println(BellmanFord(1) ? "Yes" : "No");
        }
    }
}
"""