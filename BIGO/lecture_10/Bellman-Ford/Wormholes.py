# python3
INF = 10 ** 9

class Edge:
    def __init__(self, _source, _target, _weight):
        self.source = _source
        self.target = _target
        self.weight = _weight

def BellmanFord(s):
    dist = [INF] * n
    dist[s] = 0

    for i in range(n - 1):
        for j in range(len(graph)):
        # for edge in graph:
            edge = graph[j]
            u, v, w = edge.source, edge.target, edge.weight
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    
    for j in range(len(graph)):
        # for edge in graph:
        edge = graph[j]
    # for edge in graph:
        u, v, w = edge.source, edge.target, edge.weight
        if dist[u] != INF and dist[u] + w < dist[v]:
            return False
    
    return True


T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    graph = []

    for i in range(m):
        x, y, t = map(int, input().split())
        graph.append(Edge(x, y, t))
    
    print("possible" if not BellmanFord(0) else "not possible")

# C++
"""
#include <bits/stdc++.h>
#define MAX_V 1005
#define MAX_E 2005
using namespace std;
const int INF = 1e9 + 7;

struct Edge {
    int source, target, weight;
};

int n, m;
int dist[MAX_V];
Edge graph[MAX_E];

bool BellmanFord(int s) {
    fill(dist, dist + n, INF);
    dist[s] = 0;

    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < m; j++) {
            int u = graph[j].source;
            int v = graph[j].target;
            int w = graph[j].weight;

            if (dist[u] != INF && dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
            }
        }
    }

    for (int i = 0; i < m; i++) {
        int u = graph[i].source;
        int v = graph[i].target;
        int w = graph[i].weight;

        if (dist[u] != INF && dist[u] + w < dist[v]) {
            return false;
        }
    }
    return true;
}

int main() {
    int T, x, y, t;
    cin >> T;

    while (T--) {
        cin >> n >> m;

        for (int i = 0; i < m; i++) {
            cin >> x >> y >> t;
            graph[i] = (Edge) {x, y, t};
        }

		    cout << (!BellmanFord(0) ? "possible" : "not possible") << endl;
    }
    return 0;
}
"""

# JAVA
"""
import java.util.*;

public class Main {
    static final int MAX_V = 1005;
    static final int MAX_E = 2005;
    static class Edge {
        int source, target, weight;

        public Edge(int _source, int _target, int _weight) {
            this.source = _source;
            this.target = _target;
            this.weight = _weight;
        }
    };

    static int n, m;
    static int dist[] = new int[MAX_V];
    static Edge graph[] = new Edge[MAX_E];

    public static boolean BellmanFord(int s) {
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[s] = 0;

        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < m; j++) {
                int u = graph[j].source;
                int v = graph[j].target;
                int w = graph[j].weight;

                if (dist[u] != Integer.MAX_VALUE && dist[u] + w < dist[v]) {
                    dist[v] = dist[u] + w;
                }
            }
        }

        for (int i = 0; i < m; i++) {
            int u = graph[i].source;
            int v = graph[i].target;
            int w = graph[i].weight;

            if (dist[u] != Integer.MAX_VALUE && dist[u] + w < dist[v]) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] agrs) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        while (T-- > 0) {
            n = sc.nextInt();
            m = sc.nextInt();

            for (int i = 0; i < m; i++) {
                int x = sc.nextInt();
                int y = sc.nextInt();
                int t = sc.nextInt();
                graph[i] = new Edge(x, y, t);
            }

            System.out.println(!BellmanFord(0) ? "possible" : "not possible");
        }
    }
}
"""