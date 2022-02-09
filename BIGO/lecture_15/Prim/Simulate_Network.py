# python 3
import queue

INF = 1e9

class Node:
    def __init__(self, dist, index):
        self.dist = dist
        self.index = index

    def __lt__(self, other):
        return self.dist < other.dist

def prim(src):
    dist[src] = 0
    pq = queue.PriorityQueue()
    pq.put(Node(0, src))
    while not pq.empty():
        u = pq.get().index
        visited[u] = True
        for item in graph[u]:
            v, w = item.index, item.dist
            if not visited[v] and dist[v] > w:
                dist[v] = w
                pq.put(Node(dist[v], v))

    return dist

n, m = map(int, input().split())
graph = [[] for i in range(n + 1)]
dist = [INF for i in range(n + 1)]
visited = [False for i in range(n + 1)]
for i in range(m):
    u, v, w = map(int, input().split())
    graph[u].append(Node(w, v))
    graph[v].append(Node(w, u))
mstCables = prim(1)[2: ]
mstCables.sort(reverse=True)
newCables = queue.PriorityQueue() # min heap
q = int(input())
if (q > 0):
    for cable in list(map(int, input().split())):
        newCables.put(cable)
res = 0
for oldCable in mstCables:
    usedCable = oldCable
    if not newCables.empty() and newCables.queue[0] < usedCable:
        usedCable = newCables.get()
    res += usedCable
print(res)
# C++
"""
#include <bits/stdc++.h>
using namespace std;
#define pii pair<int, int>
const int MAX = 1e5 + 10;
const int INF = 1e9;

vector<pii > graph[MAX];
vector<int> dist(MAX, INF);
bool visited[MAX];

struct option {
    bool operator() (const pii &a, const pii &b) const {
        return a.second > b.second;
    }
}; 

void prim(int src) {
    priority_queue<pii, vector<pii >, option > pq;
    pq.push(make_pair(src, 0));
    dist[src] = 0;
    while (!pq.empty()) {
        int u = pq.top().first;
        pq.pop();
        visited[u] = true;
        for (int i = 0; i < graph[u].size(); i++) {
            int v = graph[u][i].first;
            int w = graph[u][i].second;
            if (!visited[v] && dist[v] > w) {
                dist[v] = w;
                pq.push(make_pair(v, w));
            }
        }
    }
}

int main() {
    int n, m, q;
    cin >> n >> m;
    for (int u, v, w, i = 0; i < m; i++) {
        cin >> u >> v >> w;
        graph[u].push_back(make_pair(v, w));
        graph[v].push_back(make_pair(u, w));
    }
    prim(1);
    priority_queue<int> mstCable;
    for (int i = 2; i <= n; i++) {
        mstCable.push(dist[i]); // add all edges in mst to max heap
    }
    cin >> q;
    priority_queue<int, vector<int>, greater<int> > newCables;
    for (int x, i = 0; i < q; i++) {
        cin >> x;
        newCables.push(x);
    }
    long long res = 0;
    while (!mstCable.empty()) {
        int usedCable = mstCable.top();
        mstCable.pop();
        if (!newCables.empty() && newCables.top() < usedCable) {
            usedCable = newCables.top(); // replace old cable by new cable
            newCables.pop();
        }
        res += usedCable;
    }
    cout << res;
    return 0;
}
"""
# JAVA
"""
import java.util.*;

class Main {
    static ArrayList<ArrayList<Node>> graph;
    static int[] dist;
    static boolean[] visited;
    
    public static void prim(int src) {
        PriorityQueue<Node> pq = new PriorityQueue<Node>();
        pq.add(new Node(src, 0));
        dist[src] = 0; 
        while (!pq.isEmpty()) {
            Node top = pq.poll();
            int u = top.id;
            visited[u] = true;
            for (int i = 0; i < graph.get(u).size(); i++) {
                Node neighbor = graph.get(u).get(i);
                int v = neighbor.id, w = neighbor.dist;
                if (!visited[v] && w < dist[v]) {
                    dist[v] = w;
                    pq.add(new Node(v, w));
                }
            }
        }
    } 
    
    public static void main(String[] args) {
        Scanner in= new Scanner(System.in);
        int n = in.nextInt();
        int m = in.nextInt();
        graph = new ArrayList<ArrayList<Node>>();
        dist = new int[n + 1];
        visited = new boolean[n + 1];
        Arrays.fill(dist, Integer.MAX_VALUE);
        Arrays.fill(visited, false);
        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<Node>());
        }
        for (int i = 0; i < m; i++) {
            int u = in.nextInt();
            int v = in.nextInt();
            int w = in.nextInt();
            graph.get(u).add(new Node(v, w));
            graph.get(v).add(new Node(u, w));
        }
        prim(1);
        PriorityQueue<Integer> mstCable = 
            new PriorityQueue<Integer>(new MaxHeapComparator());
        for (int i = 2; i <= n; i++) {
            mstCable.add(dist[i]); // add all edges in mst to max heap
        }
        int q = in.nextInt();
        PriorityQueue<Integer> newCables = new PriorityQueue<Integer>();
        for (int i = 0; i < q; i++) {
            int x = in.nextInt();
            newCables.add(x);
        }
        long res = 0;
        while (!mstCable.isEmpty()) {
            int usedCable = mstCable.poll();
            if (!newCables.isEmpty() && newCables.peek() < usedCable)
                usedCable = newCables.poll(); // replace old cable by new cable
            res += usedCable;
        }
        System.out.print(res);
    }
}

class Node implements Comparable<Node> {
    public Integer id;
    public Integer dist;
    public Node(Integer id, Integer dist) {
        this.id = id;
        this.dist = dist;
    }
    @Override
    public int compareTo(Node other) {
        return this.dist.compareTo(other.dist);
    }
} 

class MaxHeapComparator implements Comparator<Integer> {
    @Override
    public int compare(Integer o1, Integer o2) {
        return o2.compareTo(o1);
    }
}
"""

