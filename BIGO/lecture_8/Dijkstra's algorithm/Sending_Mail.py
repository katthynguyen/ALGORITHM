# python 3
from heapq import heappush, heappop
INF = 10 ** 9 + 7
 
def Dijkstra(s, f):
    global dist
    pq = [(0, s)]
    dist[s] = 0
     
    while pq:
        w, u = heappop(pq)
        if u == f:
            break
         
        if w > dist[u]:
            continue
         
        for weight, v in graph[u]:
            if w + weight < dist[v]:
                dist[v] = w + weight
                heappush(pq, (dist[v], v))
 
Q = int(input())
 
for t in range(1, Q + 1):
    n, m, S, T = map(int, input().split())
    graph = [[] for _ in range(n)]
     
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((w, v))
        graph[v].append((w, u))
     
    dist = [INF] * n
    Dijkstra(S, T)
     
    print('Case #{}: '.format(t), end='')
    print(dist[T] if dist[T] != INF else "unreachable")
# C++

"""
#include <bits/stdc++.h>
#define MAX 20005
using namespace std;
const int INF = 1e9 + 7;
 
int Q;
vector<pair<int, int>> graph[MAX];
int dist[MAX];
 
void Dijkstra(int s, int f) {
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push(make_pair(0, s));
    dist[s] = 0;
     
    while (!pq.empty()) {
        pair<int, int> top = pq.top();
        pq.pop();
        int u = top.second;
        int w = top.first;
         
        if (u == f) {
            break;
        }
         
        if (w > dist[u]) {
            continue;
        }
         
        for (pair<int, int> &neighbor : graph[u]) {
            if (w + neighbor.first < dist[neighbor.second]) {
                dist[neighbor.second] = w + neighbor.first;
                pq.push(make_pair(dist[neighbor.second], neighbor.second));
            }
        }
    }
}
 
int main() {
    int n, m, S, T, u, v, w;
    cin >> Q;
     
    for (int t = 1; t <= Q; t++) {
        cin >> n >> m >> S >> T;
         
        for (int i = 0; i < n; i++) {
            graph[i].clear();
            dist[i] = INF;
        }
         
        for (int i = 0; i < m; i++) {
            cin >> u >> v >> w;
            graph[u].push_back(make_pair(w, v));
            graph[v].push_back(make_pair(w, u));
        }
         
        Dijkstra(S, T);
         
        cout << "Case #" << t << ": ";
         
        if (dist[T] != INF) {
            cout << dist[T] << endl;
        }
        else {
            cout << "unreachable" << endl;
        }
    }
    return 0;
}
"""

# JAVA
"""
import java.util.*;
 
public class Main {
    static final int MAX = 20005;
    static final int INF = (int)1e9 + 7;
    static int Q;
    static int[] dist = new int[MAX];
     
    static class Node implements Comparable<Node> {
        int id, weight;
         
        public Node(int _id, int _weight) {
            this.id = _id;
            this.weight = _weight;
        }
         
        @Override
        public int compareTo(Node other) {
            return this.weight - other.weight;
        }
    }
     
    static ArrayList<Node> graph[] = new ArrayList[MAX];
     
    public static void Dijkstra(int s, int f) {
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.add(new Node(s, 0));
        dist[s] = 0;
         
        while (!pq.isEmpty()) {
            Node top = pq.poll();
            int u = top.id;
            int w = top.weight;
             
            if (u == f) {
                break;
            }
             
            if (w > dist[u]) {
                continue;
            }
             
            for (Node neighbor : graph[u]) {
                if (w + neighbor.weight < dist[neighbor.id]) {
                    dist[neighbor.id] = w + neighbor.weight;
                    pq.add(new Node(neighbor.id, dist[neighbor.id]));
                }
            }
        }
    }
     
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Q = sc.nextInt();
         
        for (int t = 1; t <= Q; t++) {
            int n = sc.nextInt();
            int m = sc.nextInt();
            int S = sc.nextInt();
            int T = sc.nextInt();
             
            for (int i = 0; i < n; i++) {
                graph[i] = new ArrayList<Node>();
                dist[i] = INF;
            }
             
            for (int i = 0; i < m; i++) {
                int u = sc.nextInt();
                int v = sc.nextInt();
                int w = sc.nextInt();
                graph[u].add(new Node(v, w));
                graph[v].add(new Node(u, w));
            }
             
            Dijkstra(S, T);
             
            System.out.print("Case #" + t + ": ");
            System.out.println(dist[T] != INF ? dist[T] : "unreachable");
        }
    }
}
"""