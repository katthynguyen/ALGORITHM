# python 3
INF = 10 ** 9

class Edge:
    def __init__(self, _source, _target, _weight):
        self.source = _source
        self.target = _target
        self.weight = _weight

def BellmanFord(s):
    dist[s] = 0
    for i in range(n - 1):
        for edge in graph:
            u, v, w = edge.source, edge.target, edge.weight

            if dist[u] != INF:
                dist[v] = min(dist[v], dist[u] + w)
    
    for i in range(n):
        for e in graph:
            u, v, w = e.source, e.target, e.weight
            if dist[u] != INF and dist[v] > dist[u] + w:
                dist[v] = -INF

T = int(input())

for t in range(1, T + 1):
    input()
    n = int(input())
    weight = [0] + list(map(int, input().split()))
    m = int(input())
    
    graph = []
    dist = [INF] * (n + 1)

    for _ in range(m):
        u, v = map(int, input().split())
        graph.append(Edge(u, v, (weight[v] - weight[u]) ** 3))
    
    BellmanFord(1)
    q = int(input())
    print("Case {}:".format(t))

    for _ in range(q):
        f = int(input())
        print(dist[f] if dist[f] != INF and dist[f] >= 3 else "?")

# C++
"""
#include <bits/stdc++.h>
#define MAX_V 205
#define MAX_E 205 * 204
using namespace std;
const int INF = 1e9 + 7;

struct Edge {
    int source, target, weight;
};

int n, m;
int weight[MAX_V];
int dist[MAX_V];
Edge graph[MAX_E];

void BellmanFord(int s) {
    fill(dist, dist + (n + 1), INF);
    dist[s] = 0;

    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < m; j++) {
            int u = graph[j].source;
            int v = graph[j].target;
            int w = graph[j].weight;

            if (dist[u] != INF) {
                dist[v] = min(dist[v], dist[u] + w);
            }
        }
    }
  
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < m; j++) {
            int u = graph[j].source;
            int v = graph[j].target;
            int w = graph[j].weight;

            if (dist[u] != INF && dist[v] > dist[u] + w) {
                dist[v] = -INF;
            }
        }
    }
}

int main() {
    int T, q, u, v, f;
    cin >> T;

    for (int t = 1; t <= T; t++) {
        cin >> n;
        for (int i = 1; i <= n; i++) {
            cin >> weight[i];
        }

        cin >> m;
        for (int i = 0; i < m; i++) {
            cin >> u >> v;
            graph[i] = (Edge) {u, v, int(pow(weight[v] - weight[u], 3))};
        }

        BellmanFord(1);
        cin >> q;
        cout << "Case " << t << ":" << endl;

        for (int i = 0; i < q; i++) {
            cin >> f;

            if (dist[f] != INF && dist[f] >= 3) {
                cout << dist[f] << endl;
            }
            else {
                cout << "?" << endl;
            }
        }
    }
    return 0;
}
"""

# JAVA
"""
import java.util.*;
import java.io.*;
 
public class test {
    static final long INF = (long)1e18;
    static final int MAX_V = 205;
    static final int MAX_E = 205 * 204;
    static class Edge {
        int source, target, weight;
 
        public Edge(int _source, int _target, int _weight) {
            this.source = _source;
            this.target = _target;
            this.weight = _weight;
        }
    }
 
    static int n, m;
    static int[] weight = new int[MAX_V];
    static long[] dist = new long[MAX_V];
    static Edge[] graph = new Edge[MAX_E];
 
    public static void BellmanFord(int s) {
        Arrays.fill(dist, INF);
        dist[s] = 0;
 
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < m; j++) {
                int u = graph[j].source;
                int v = graph[j].target;
                int w = graph[j].weight;
 
                if (dist[u] != INF) {
                    dist[v] = Math.min(dist[v], dist[u] + w);
                }
            }
        }
      
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                int u = graph[j].source;
                int v = graph[j].target;
                int w = graph[j].weight;
 
                if (dist[u] != INF && dist[v] > dist[u] + w) {
                    dist[v] = -INF;
                }
            }
        }
    }
 
    public static void main(String[] agrs) {
        MyScanner in = new MyScanner();
        int T = in.nextInt();
 
        for (int t = 1; t <= T; t++) {
            n = in.nextInt();
            for (int i = 1; i <= n; i++) {
                weight[i] = in.nextInt();
            }
 
            m = in.nextInt();
            for (int i = 0; i < m; i++) {
                int u = in.nextInt();
                int v = in.nextInt();
                graph[i] = new Edge(u, v, (int)Math.pow(weight[v] - weight[u], 3));
            }
 
            BellmanFord(1);
            System.out.println("Case " + t + ":");
            int q = in.nextInt();
 
            for (int i = 0; i < q; i++) {
                int f = in.nextInt();
                System.out.println(dist[f] != INF && dist[f] >= 3 ? dist[f] : "?");
            }
        }
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