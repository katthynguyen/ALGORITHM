# python 3
import queue
MAX = 505
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
for _ in range(N):
    A, B, W = map(int, input().split())
    graph[A].append(Node(B, W))
    graph[B].append(Node(A, W))
 
S = int(input())
Dijkstra(S)
 
Q = int(input())
for _ in range(Q):
    V = int(input())
    print(dist[V] if dist[V] != INF else "NO PATH")

# C++
"""
#include <bits/stdc++.h>
#define MAX 500 + 5
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
    int N, A, B, W;
    cin >> N;
    graph = vector<vector<pair<int, int>>>(MAX, vector<pair<int, int>>());
 
    for (int i = 0; i < N; i++) {
        cin >> A >> B >> W;
        graph[A].push_back(make_pair(B, W));
        graph[B].push_back(make_pair(A, W));
    }
 
    int S, Q, V;
    cin >> S;
    Dijkstra(S);
    cin >> Q;
 
    for (int i = 0; i < Q; i++) {
        cin >> V;
         
        if (dist[V] != INF) {
            cout << dist[V] << endl;
        }
        else {
            cout << "NO PATH" << endl;
        }
    }
 
    return 0;
}
"""
# JAVA
"""
import java.util.*;
 
public class Main {
    static final int MAX = 505;
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
 
        for (int i = 0; i < MAX; i++) {
            dist[i] = INF;
            graph[i] = new ArrayList<Node>();
        }
 
        for (int i = 0; i < N; i++) {
            int A = sc.nextInt();
            int B = sc.nextInt();
            int W = sc.nextInt();
            graph[A].add(new Node(B, W));
            graph[B].add(new Node(A, W));
        }
 
        int S = sc.nextInt();
        Dijsktra(S);
        int Q = sc.nextInt();
         
        for (int i = 0; i < Q; i++) {
            int V = sc.nextInt();
            System.out.println(dist[V] != INF ? dist[V] : "NO PATH");
        }
    }
}
"""
