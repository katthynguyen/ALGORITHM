# python 3
def DFS(src):
    global leaf, max_dist
    dist = [-1] * (V + 1)
    s = [src]
    dist[src] = 0

    while len(s):
        u = s.pop()

        for v, w in graph[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + w
                max_dist = max(max_dist, dist[v])
                s.append(v)
    
    leaf = dist.index(max(dist))

t = int(input())

for _ in range(t):
    V = int(input())
    E = V - 1
    graph = [[] for _ in range(V + 1)]

    for i in range(E):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    leaf = 0
    max_dist = 0

    DFS(1)
    DFS(leaf)

    print(max_dist)
# C++
"""
#include <bits/stdc++.h>
#define MAX 50000 + 5
using namespace std;

struct Triad {
    int v, w;
};

int V, E, leaf;
long long max_dist;
long long dist[MAX];
vector<Triad> graph[MAX];

void DFS(int src) {
    memset(dist, -1, sizeof(dist));
    stack<int> s;
    dist[src] = 0;
    s.push(src);

    while (!s.empty()) {
        int u = s.top();
        s.pop();

        for (Triad &neighbor : graph[u]) {
            int v = neighbor.v;
            int w = neighbor.w;

            if (dist[v] == -1) {
                dist[v] = dist[u] + w;
                s.push(v);

                if (dist[v] > max_dist) {
                    max_dist = dist[v];
                    leaf = v;
                }
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int t, u, v, w;
    cin >> t;

    while (t--) {
        cin >> V;
        E = V - 1;

				for (int i = 0; i <= V; i++) {
            graph[i].clear();
        }      
      
        for (int i = 0; i < E; i++) {
            cin >> u >> v >> w;
            graph[u].push_back((Triad) {v, w});
            graph[v].push_back((Triad) {u, w});
        }

        max_dist = 0;
        
        DFS(1);
        DFS(leaf);

        cout << max_dist << endl;
    }

    return 0;
}
"""

# JAVA
"""
import java.util.*;

public class Main {
    static final int MAX = 50000 + 5;
    static int V, E, leaf;
    static long max_dist;
    static long[] dist = new long[MAX];
    
    static class Triad {
        int v, w;

        public Triad(int _v, int _w) {
            this.v = _v;
            this.w = _w;
        }
    };

    static ArrayList<Triad> graph[] = new ArrayList[MAX];

    public static void DFS(int src) {
        for (int i = 0; i <= V; i++) {
            dist[i] = -1;
        }

        Stack<Integer> s = new Stack<>();
        s.add(src);
        dist[src] = 0;

        while (!s.isEmpty()) {
            int u = s.pop();

            for (Triad neighbor : graph[u]) {
                int v = neighbor.v;
                int w = neighbor.w;

                if (dist[v] == -1) {
                    dist[v] = dist[u] + w;
                    s.add(v);

                    if (dist[v] > max_dist) {
                        max_dist = dist[v];
                        leaf = v;
                    }
                }
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();

        while (t-- > 0) {
            V = sc.nextInt();
            E = V - 1;

            for (int i = 0; i <= V; i++) {
                graph[i] = new ArrayList<Triad>();
            }

            for (int i = 0; i < E; i++) {
                int u = sc.nextInt();
                int v = sc.nextInt();
                int w = sc.nextInt();
                graph[u].add(new Triad(v, w));
                graph[v].add(new Triad(u, w));
            }

            max_dist = 0;

            DFS(1);
            DFS(leaf);

            System.out.println(max_dist);
        }
    }
}
"""