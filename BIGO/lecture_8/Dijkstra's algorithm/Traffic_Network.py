# python 3
from heapq import heappush, heappop
INF = 10 ** 9
MAX = 10001
 
def Dijkstra(s, dist, graph):
    pq = [(0, s)]
    dist[s] = 0
     
    while pq:
        w, u = heappop(pq)
         
        if w > dist[u]:
            continue
         
        for weight, v in graph[u]:
            if w + weight < dist[v]:
                dist[v] = w + weight
                heappush(pq, (dist[v], v))
 
T = int(input())
 
for _ in range(T):
    n, m, k, s, t = map(int, input().split())
     
    graphS = [[] for _ in range(MAX)]
    graphT = [[] for _ in range(MAX)]
    distT = [INF] * MAX
    distS = [INF] * MAX
     
    for i in range(m):
        u, v, d = map(int, input().split())
        graphS[u].append((d, v))
        graphT[v].append((d, u))
     
    Dijkstra(s, distS, graphS)
    Dijkstra(t, distT, graphT)
    res = distS[t]
     
    for i in range(k):
        u, v, d = map(int, input().split())
        res = min(res, distS[u] + d + distT[v], distS[v] + d + distT[u])
     
    print(res if res != INF else -1)
# C++
"""
#include <bits/stdc++.h>
#define MAX 10005
using namespace std;
const int INF = 1e9 + 7;
 
vector<pair<int, int>> graphS[MAX], graphT[MAX];
int distS[MAX], distT[MAX];
 
void Dijkstra(int s, int dist[], vector<pair<int, int>> (&graph)[MAX]) {
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push(make_pair(0, s));
    dist[s] = 0;
     
    while (!pq.empty()) {
        pair<int, int> top = pq.top();
        pq.pop();
         
        int u = top.second;
        int w = top.first;
         
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
    ios::sync_with_stdio(false);
    cin.tie(0);
 
    int T, n, m, k, s, t, u, v, d;
    cin >> T;
     
    while (T--) {
        cin >> n >> m >> k >> s >> t;
         
        for (int i = 1; i <= n; i++) {
            graphS[i].clear();
            graphT[i].clear();
            distS[i] = INF;
            distT[i] = INF;
        }
         
        for (int i = 0; i < m; i++) {
            cin >> u >> v >> d;
            graphS[u].push_back(make_pair(d, v));
            graphT[v].push_back(make_pair(d, u));
        }
         
        Dijkstra(s, distS, graphS);
        Dijkstra(t, distT, graphT);
        int res = distS[t];
         
        for (int i = 0; i < k; i++) {
            cin >> u >> v >> d;
            int a = distS[u] + d + distT[v];
            int b = distS[v] + d + distT[u];
            res = min(res, min(a, b));
        }
         
        cout << (res != INF ? res : -1) << endl;
    }
    return 0;
}
"""

# JAVA
"""
import java.util.*;
 
public class Main {
    static final int MAX = 10005;
    static final int INF = (int)1e9 + 7;
    static int n, m, k, s, t, u, v, d;
     
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
     
    static ArrayList<Node> graphS[] = new ArrayList[MAX], graphT[] = new ArrayList[MAX];
    static int[] distS = new int[MAX], distT = new int[MAX];
     
    public static void Dijkstra(int s, int[] dist, ArrayList<Node> graph[]) {
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.add(new Node(s, 0));
        dist[s] = 0;
         
        while (!pq.isEmpty()) {
            Node top = pq.poll();
            int u = top.id;
            int w = top.weight;
             
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
     
    public static void main(String[] agrs) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
         
        while (T-- > 0) {
            n = sc.nextInt();
            m = sc.nextInt();
            k = sc.nextInt();
            s = sc.nextInt();
            t = sc.nextInt();
             
            for (int i = 1; i <= n; i++) {
                graphS[i] = new ArrayList<Node>();
                graphT[i] = new ArrayList<Node>();
                distS[i] = INF;
                distT[i] = INF;
            }
             
            for (int i = 0; i < m; i++) {
                u = sc.nextInt();
                v = sc.nextInt();
                d = sc.nextInt();
                graphS[u].add(new Node(v, d));
                graphT[v].add(new Node(u, d));
            }
             
            Dijkstra(s, distS, graphS);
            Dijkstra(t, distT, graphT);
            int res = distS[t];
             
            for (int i = 0; i < k; i++) {
                u = sc.nextInt();
                v = sc.nextInt();
                d = sc.nextInt();
                int a = distS[u] + d + distT[v];
                int b = distS[v] + d + distT[u];
                res = Math.min(res, Math.min(a, b));
            }
             
            System.out.println(res != INF ? res : -1);
        }
    }
}
"""