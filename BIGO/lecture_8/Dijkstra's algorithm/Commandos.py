# python 3
from heapq import heappush, heappop
 
def Dijkstra(s):
    dist = [10 ** 9] * N
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
     
    return dist
 
T = int(input())
 
for t in range(1, T + 1):
    N = int(input())
    R = int(input())
    graph = [[] for _ in range(N)]
     
    for _ in range(R):
        u, v = map(int, input().split())
        graph[u].append((1, v))
        graph[v].append((1, u))
     
    s, d = map(int, input().split())
    distS = Dijkstra(s)
    distD = Dijkstra(d)
    res = 0
     
    for i in range(N):
        res = max(res, distS[i] + distD[i])
     
    print("Case {}: {}".format(t, res))
# C++

"""
#include <bits/stdc++.h>
#define MAX 105
using namespace std;
const int INF = 1e9 + 7;
 
int N, R;
vector<pair<int, int> > graph[MAX];
 
vector<int> Dijkstra(int s) {
    vector<int> dist(N, INF);
    priority_queue<pair<int, int>, vector<pair<int, int> >, greater<pair<int, int> > > pq;
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
         
        for (int i = 0; i < graph[u].size(); i++) {
            pair<int, int> neighbor = graph[u][i];
             
            if (w + neighbor.first < dist[neighbor.second]) {
                dist[neighbor.second] = w + neighbor.first;
                pq.push(make_pair(dist[neighbor.second], neighbor.second));
            }
        }
    }
     
    return dist;
}
 
int main() {
    int T, s, d, u, v;
    cin >> T;
     
    for (int t = 1; t <= T; t++) {
        cin >> N >> R;
         
        for (int i = 0; i < N; i++) {
            graph[i].clear();
        }
         
        for (int i = 0; i < R; i++) {
            cin >> u >> v;
            graph[u].push_back(make_pair(1, v));
            graph[v].push_back(make_pair(1, u));
        }
         
        cin >> s >> d;
         
        vector<int> distS = Dijkstra(s);
        vector<int> distD = Dijkstra(d);
        int res = 0;
         
        for (int i = 0; i < N; i++) {
            res = max(res, distS[i] + distD[i]);
        }
         
        cout << "Case " << t << ": " << res << endl;
    }
    return 0;
}
"""

# JAVA
"""
import java.util.*;
 
public class Main {
    static final int MAX = 105;
    static final int INF = (int)1e9 + 7;
    static int N, R;
     
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
     
    public static int[] Dijkstra(int s) {
        int[] dist = new int[N];
        Arrays.fill(dist, INF);
         
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
         
        return dist;
    }
     
    public static void main(String[] agrs) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
         
        for (int t = 1; t <= T; t++) {
            N = sc.nextInt();
            R = sc.nextInt();
             
            for (int i = 0; i < N; i++) {
                graph[i] = new ArrayList<Node>();
            }
             
            for (int i = 0; i < R; i++) {
                int u = sc.nextInt();
                int v = sc.nextInt();
                graph[u].add(new Node(v, 1));
                graph[v].add(new Node(u, 1));
            }
             
            int s = sc.nextInt();
            int d = sc.nextInt();
             
            int[] distS = Dijkstra(s);
            int[] distD = Dijkstra(d);
            int res = 0;
             
            for (int i = 0; i < N; i++) {
                res = Math.max(res, distS[i] + distD[i]);
            }
             
            System.out.println("Case " + t + ": " + res);
        }
    }
}
"""