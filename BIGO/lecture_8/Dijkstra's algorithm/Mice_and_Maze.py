# python 3
import queue
MAX = 105
INF = int(1e9) + 7
graph = [[] for _ in range(MAX)]
dist = [INF for _ in range(MAX)]
 
class Node:
    def __init__(self, _id, _weight):
        self.id = _id
        self.weight = _weight
     
    def __lt__(self, other):
        return self.weight < other.weight
 
def Dijkstra(s):
    pq = queue.PriorityQueue()
    pq.put(Node(s, 0))
    dist[s] = 0
 
    while not pq.empty():
        top = pq.get()
        u = top.id
        w = top.weight
 
        for neighbor in graph[u]:
            if w + neighbor.weight < dist[neighbor.id]:
                dist[neighbor.id] = w + neighbor.weight
                pq.put(Node(neighbor.id, dist[neighbor.id]))
 
N = int(input())
E = int(input())
T = int(input())
M = int(input())
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[v].append(Node(u, w))
 
Dijkstra(E)
 
count = 0
for i in range(1, N + 1):
    if dist[i] <= T:
        count += 1
 
print(count)

# C++

"""
#include <bits/stdc++.h>
#define MAX 105
using namespace std;
const int INF = 1e9 + 7;
 
vector<vector<pair<int, int>>> graph;
vector<int> dist(MAX, INF);
 
void Dijkstra(int s) {
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push(make_pair(s, 0));
    dist[s] = 0;
 
    while (!pq.empty()) {
        pair<int, int> top = pq.top();
        pq.pop();
 
        int u = top.first;
        int w = top.second;
 
        for (pair<int, int> &neighbor : graph[u]) {
            if (w + neighbor.second < dist[neighbor.first]) {
                dist[neighbor.first] = w + neighbor.second;
                pq.push(make_pair(neighbor.first, dist[neighbor.first]));
            }
        }
    }
}
 
int main() {
    int N, E, T, M;
    int u, v, w;
    cin >> N >> E >> T >> M;
    graph = vector<vector<pair<int, int>>>(MAX, vector<pair<int, int>>());
 
    for (int i = 0; i < M; i++) {
        cin >> u >> v >> w;
        graph[v].push_back(make_pair(u, w));
    }
 
    Dijkstra(E);
 
    int count = 0;
    for (int i = 1; i <= N; i++) {
        if (dist[i] <= T) {
            count++;
        }
    }
 
    cout << count;
    return 0;
}
"""
# JAVA

"""
import java.util.*;
 
public class Main {
    static final int MAX = 105;
    static final int INF = (int)1e9 + 7;
    static final int[] dist = new int[MAX];
 
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
 
    public static void Dijsktra(int s) {
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.add(new Node(s, 0));
        dist[s] = 0;
 
        while (!pq.isEmpty()) {
            Node top = pq.poll();
            int u = top.id;
            int w = top.weight;
 
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
        int N = sc.nextInt();
        int E = sc.nextInt();
        int T = sc.nextInt();
        int M = sc.nextInt();
 
        for (int i = 0; i <= N; i++) {
            dist[i] = INF;
            graph[i] = new ArrayList<Node>();
        }
 
        for (int i = 0; i < M; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            int w = sc.nextInt();
            graph[v].add(new Node(u, w));
        }
 
        Dijsktra(E);
         
        int count = 0;
        for (int i = 1; i <= N; i++) {
            if (dist[i] <= T) {
                count++;
            }
        }
 
        System.out.print(count);
    }
}
    """