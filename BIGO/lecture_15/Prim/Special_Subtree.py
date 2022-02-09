# python 3
import queue

INF = 10 ** 9


class node:
    def __init__(self, dist, index):
        self.dist = dist
        self.index = index

    def __lt__(self, other):
        return self.dist < other.dist

    def __str__(self):
        return "%d %d" % (self.index, self.dist)


def prim(graph, src):
    n = len(graph)
    dist = [INF] * n
    path = [-1] * n
    visited = [False] * n
    dist[src] = 0
    visited[src] = True

    Q = queue.PriorityQueue()
    Q.put(node(0, src))

    while not Q.empty():
        u = Q.get().index
        visited[u] = True
        for nxt in graph[u]:
            v, w = nxt.index, nxt.dist
            if not visited[v] and dist[v] > w:
                dist[v] = w
                Q.put(node(dist[v], v))
                path[v] = u

    total_cost = 0
    for i in range(n):
        if path[i] != -1:
            total_cost += dist[i]

    return total_cost


n, m = map(int, input().split())
graph = [[] for i in range(n)]
for i in range(m):
    u, v, w = map(int, input().split())
    graph[u - 1].append(node(w, v - 1))
    graph[v - 1].append(node(w, u - 1))

s = int(input())
print(prim(graph, s - 1))

# C++
"""
#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;

const int INF = 1e9;

struct node {
    int vertex;
    int weight;

    node(int d, int w) : vertex(d), weight(w) {}
};

class comparator {
public:
    bool operator()(const node& a, const node& b) const {
        return a.weight > b.weight;
    }
};

int n, m, s;
vector<vector<node>> graph;

int prim(int s) {
    priority_queue<node, vector<node>, comparator> pq;
    vector<int> dist(n + 1, INF);
    vector<bool> visited(n + 1, false);

    dist[s] = 0;
    visited[s] = true;
    pq.push(node(s, 0));

    while (!pq.empty()) {
        int u = pq.top().vertex;
        pq.pop();
        visited[u] = true;

        for (node neighbor : graph[u]) {
            int v = neighbor.vertex;
            int w = neighbor.weight;

            if (!visited[v] && dist[v] > w) {
                dist[v] = w;
                pq.push(node(v, w));
            }
        }
    }

    int ans = 0;
    for (int i = 1; i <= n; i++) {
        if (dist[i] != INF) {
            ans += dist[i];
        }
    }

    return ans;
}

int main() {
    cin >> n >> m;

    graph.resize(n + 1);

    for (int i = 0; i < m; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        graph[u].push_back(node(v, w));
        graph[v].push_back(node(u, w));
    }

    cin >> s;

    int ans = prim(s);

    cout << ans << endl;
    return 0;
}

"""
# JAVA
"""
import java.io.*;
import java.util.*;

class Pair implements Comparable<Pair> {
    public Integer id;
    public Integer dist;

    public Pair(Integer id, Integer dist) {
        this.id = id;
        this.dist = dist;
    }

    @Override
    public int compareTo(Pair other) {
        return this.dist.compareTo(other.dist);
    }
}

public class Main {
    private static int[] dist;
    private static int[] path;
    private static boolean[] visited;

    public static void Prim(int src, ArrayList<ArrayList<Pair>> graph) {
        PriorityQueue<Pair> pq = new PriorityQueue<Pair>();
        int n = graph.size();
        dist = new int[n];
        path = new int[n];
        visited = new boolean[n];
        Arrays.fill(dist, Integer.MAX_VALUE);
        Arrays.fill(path, -1);
        Arrays.fill(visited, false);

        pq.add(new Pair(src, 0));
        dist[src] = 0;

        while (!pq.isEmpty()) {
            Pair top = pq.poll();
            int u = top.id;
            visited[u] = true;
            for (int i = 0; i < graph.get(u).size(); i++) {
                Pair neighbor = graph.get(u).get(i);
                int v = neighbor.id;
                int w = neighbor.dist;

                if (!visited[v] && w < dist[v]) {
                    dist[v] = w;
                    pq.add(new Pair(v, w));
                    path[v] = u;
                }
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();

        ArrayList<ArrayList<Pair>> graph = new ArrayList<ArrayList<Pair>>();

        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<Pair>());
        }

        for (int i = 0; i < m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            int w = sc.nextInt();
            graph.get(v).add(new Pair(u, w));
            graph.get(u).add(new Pair(v, w));
        }

        int start = sc.nextInt();

        Prim(start, graph);

        int result = 0;

        for (int i = 0; i <= n; i++)
            if (path[i] != -1)
                result += dist[i];

        System.out.println(result);

        sc.close();
    }
}
"""

