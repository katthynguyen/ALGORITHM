# python 3
def BellmanFord():
    prob[1] = 1.0

    for i in range(n - 1):
        for edge in graph:
            u, v, w = edge
            prob[u] = max(prob[u], prob[v] * w)
            prob[v] = max(prob[v], prob[u] * w)

while True:
    line = list(map(int, input().split()))
    if len(line) == 1:
        break
    
    graph = []
    n, m = line[0], line[1]
    
    for _ in range(m):
        u, v, c = map(int, input().split())
        graph.append((u, v, c / 100))
    
    prob = [-1.0] * (n + 1)
    BellmanFord()

    print("{:.6f} percent".format(prob[n] * 100))

# C++
"""
#include <bits/stdc++.h>
#define MAX_N 100 + 5
#define MAX_M 100 * 50 + 5
using namespace std;

struct Edge {
    int source, target;
    double weight;
};

int n, m;
double prob[MAX_N];
Edge graph[MAX_M];

void BellmanFord() {
    fill(prob, prob + (n + 1), -1.0);
    prob[1] = 1.0;

    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < m; j++) {
            int u = graph[j].source;
            int v = graph[j].target;
            double w = graph[j].weight;

            prob[u] = max(prob[u], prob[v] * w);
            prob[v] = max(prob[v], prob[u] * w);
        }
    }
}

int main() {
    int u, v, c;

    while (cin >> n, n != 0) {
        cin >> m;

        for (int i = 0; i < m; i++) {
            cin >> u >> v >> c;
            graph[i] = (Edge) {u, v, c / 100.0};
        }

        BellmanFord();
        cout << fixed << setprecision(6) << prob[n] * 100.0 << " percent" << endl;
    }
    return 0;
}
"""

# JAVA
"""
import java.util.*;

public class Main {
    static final int MAX_N = 100 + 5;
    static final int MAX_M = 100 * 50 + 5;
    static class Edge {
        int source, target;
        double weight;

        public Edge(int _source, int _target, double _weight) {
            this.source = _source;
            this.target = _target;
            this.weight = _weight;
        }
    }

    static int n, m;
    static double[] prob = new double[MAX_N];
    static Edge[] graph = new Edge[MAX_M];

    public static void BellmanFord() {
        Arrays.fill(prob, -1.0);
        prob[1] = 1.0;

        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < m; j++) {
                int u = graph[j].source;
                int v = graph[j].target;
                double w = graph[j].weight;

                prob[u] = Math.max(prob[u], prob[v] * w);
                prob[v] = Math.max(prob[v], prob[u] * w);
            }
        }
    }

    public static void main(String[] agrs) {
        Scanner sc = new Scanner(System.in);

        while (true) {
            n = sc.nextInt();
            if (n == 0) {
                break;
            }

            m = sc.nextInt();
            
            for (int i = 0; i < m; i++) {
                int u = sc.nextInt();
                int v = sc.nextInt();
                double w = sc.nextInt();
                graph[i] = new Edge(u, v, w / 100.0);
            }

            BellmanFord();
            System.out.printf("%.6f percent\n", prob[n] * 100.0);
        }
    }
}
"""