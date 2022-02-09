# python 3

import queue
INF = 10 ** 9
energy = [0] * 105

class Edge:
    def __init__(self, _source, _target):
        self.source = _source
        self.target = _target

def hasPathBFS(s, f):
    visited = [False] * (n + 1)
    q = queue.Queue()
    q.put(s)
    visited[s] = True

    while not q.empty():
        u = q.get()

        for edge in graph:
            if edge.source == u:
                v = edge.target

                if not visited[v]:
                    visited[v] = True
                    q.put(v)
                
                if v == f:
                    return True
    
    return False

def BellmanFord(s, f):
    dist = [-INF] * (n + 1)
    dist[1] = 100

    for i in range(n - 1):
        for edge in graph:
            u = edge.source
            v = edge.target
            if dist[u] > 0:
                dist[v] = max(dist[v], dist[u] + energy[v])
    
    for edge in graph:
        u = edge.source
        v = edge.target
        if dist[u] > 0 and dist[u] + energy[v] > dist[v] and hasPathBFS(u, f):
            return True
    
    return dist[f] >0
            
while True:
    n = int(input())
    if n == -1:
        break
    
    graph = []

    for u in range(1, n + 1):
        line = list(map(int, input().split()))
        energy[u] = line.pop(0)

        if not line:    # input could be ill-formated
            line.extend(list(map(int, input().split())))

        m = line.pop(0)

        while len(line) != m:
            line.extend(list(map(int, input().split())))
        
        for v in line:
            graph.append(Edge(u, v))
        
    canGo = BellmanFord(1, n)
    print("winnable" if canGo else "hopeless")
# C++
"""
#include <bits/stdc++.h>
#define MAX 105
using namespace std;
const int INF = 1e9 + 7;

int n, m;
bool visited[MAX];
int dist[MAX], energy[MAX];
vector<pair<int, int>> graph;

bool hasPathBFS(int s, int f) {
    fill(visited, visited + (n + 1), false);
    queue<int> q;
    q.push(s);
    visited[s] = true;

    while (!q.empty()) {
        int u = q.front();
        q.pop();

        for (pair<int, int> &edge : graph) {
            if (edge.first == u) {
                int v = edge.second;

                if (!visited[v]) {
                    visited[v] = true;
                    q.push(v);

                    if (v == f) {
                        return true;
                    }
                }
            }
        }        
    }
    return false;
}

bool BellmanFord(int s, int f) {
    fill(dist, dist + (n + 1), -INF);
    dist[1] = 100;

    for (int i = 0; i < n - 1; i++) {
        for (pair<int, int> &edge : graph) {
            int u = edge.first;
            int v = edge.second;
            if (dist[u] > 0) {
                dist[v] = max(dist[v], dist[u] + energy[v]);
            }
        }
    }

    for (pair<int, int> &edge : graph) {
        int u = edge.first;
        int v = edge.second;
        if (dist[u] > 0 && dist[u] + energy[v] > dist[v] && hasPathBFS(u, f)) {
            return true;
        }
    }

    return dist[f] > 0;
}

int main() {
    int v;

    while (cin >> n, n != -1) {
        graph.clear();

        for (int u = 1; u <= n; u++) {
            cin >> energy[u] >> m;
            
            for (int i = 0; i < m; i++) {
                cin >> v;
                graph.push_back(make_pair(u, v));
            }
        }

        bool canGo = BellmanFord(1, n);
        cout << (canGo ? "winnable" : "hopeless") << endl;
    }
    return 0;
}
"""

# JAVA
"""
import java.util.*;

public class Main {
    static final int MAX = 105;
    static int n, m;
    static class Edge {
        int source, target;

        public Edge(int _source, int _target) {
            this.source = _source;
            this.target = _target;
        }
    };

    static int[] energy = new int[MAX];
    static int[] dist = new int[MAX];
    static boolean[] visited = new boolean[MAX];
    static ArrayList<Edge> graph = new ArrayList<>();

    public static boolean hasPathBFS(int s, int f) {
        Arrays.fill(visited, false);
        Queue<Integer> q = new LinkedList<>();
        q.add(s);
        visited[s] = true;

        while (!q.isEmpty()) {
            int u = q.poll();

            for (Edge edge : graph) {
                if (edge.source == u) {
                    int v = edge.target;

                    if (!visited[v]) {
                        visited[v] = true;
                        q.add(v);
                    }

                    if (v == f) {
                        return true;
                    }
                }
            }
        }
        return false;
    }

    public static boolean BellmanFord(int s, int f) {
        Arrays.fill(dist, Integer.MIN_VALUE);
        dist[1] = 100;

        for (int i = 0; i < n - 1; i++) {
            for (Edge edge : graph) {
                int u = edge.source;
                int v = edge.target;
                if (dist[u] > 0) {
                    dist[v] = Math.max(dist[v], dist[u] + energy[v]);
                }
            }
        }

        for (Edge edge : graph) {
            int u = edge.source;
            int v = edge.target;
            if (dist[u] > 0 && dist[u] + energy[v] > dist[v] && hasPathBFS(u, f)) {
                return true;
            }
        }

        return dist[f] > 0;
    }

    public static void main(String[] agrs) {
        Scanner sc = new Scanner(System.in);

        while (true) {
            graph.clear();
            
            n = sc.nextInt();
            if (n == -1) {
                break;
            }

            for (int u = 1; u <= n; u++) {
                energy[u] = sc.nextInt();
                m = sc.nextInt();

                for (int i = 0; i < m; i++) {
                    int v = sc.nextInt();
                    graph.add(new Edge(u, v));
                }
            }

            boolean canGo = BellmanFord(1, n);
            System.out.println(canGo ? "winnable" : "hopeless");
        }
    }
}
"""