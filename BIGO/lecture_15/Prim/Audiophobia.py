# python 3
import queue

INF = 10 ** 9

class Node:
    def __init__(self, id, dist):
        self.dist = dist
        self.id = id

    def __lt__(self, other):
        return self.dist < other.dist

    def __str__(self):
        return "%d %d" % (self.id, self.dist)

def prim(src):
    global mstGraph
    global graph
    global visited
    global dist
    global path
    
    pq = queue.PriorityQueue()
    pq.put(Node(src, 0))
    dist[src] = 0
    while not pq.empty():
        u = pq.get().id
        visited[u] = True
        for neighbor in graph[u]:
            v, w = neighbor.id, neighbor.dist
            if not visited[v] and dist[v] > w:
                dist[v] = w
                pq.put(Node(v, w))
                path[v] = u
    
    for u in range(2, C + 1):
        if path[u] != -1:
            v, w = path[u], dist[u]
            mstGraph[u].append(Node(v, w))
            mstGraph[v].append(Node(u, w))

def dfs(src, dst, level):
    global mstGraph
    global visited
    if src == dst:
        return level
    visited[src] = True
    for neighbor in mstGraph[src]:
        v, w = neighbor.id, neighbor.dist
        if not visited[v]:
            tmpLevel = dfs(v, dst, max(level, w))
            if tmpLevel != INF:
                return tmpLevel
    return INF

tc = 1
while (tc != 0):
    C, S, Q = map(int, input().split())
    if C == S == Q == 0:
        break
    
    mstGraph = [[] for i in range(C + 1)]
    graph = [[] for i in range(C + 1)]
    visited = [False] * (C + 1)
    dist = [INF] * (C + 1)
    path = [-1] * (C + 1)

    for i in range(S):
        u, v, w = map(int, input().split())
        graph[u].append(Node(v, w))
        graph[v].append(Node(u, w))

    for i in range(1, C + 1):
        if not visited[i]:
            prim(i)

    if tc != 1:
        print()
    print('Case #' + str(tc))
    tc += 1
    for i in range(Q):
        u, v = map(int, input().split())
        visited = [False] * (C + 1)
        level = dfs(u, v, 0)
        print(level if level < INF else 'no path')
# C++
"""
#include <bits/stdc++.h>
using namespace std;
#define pii pair<int, int>
#define MAX 110
const int INF = 1e9;
vector<pii > mstGraph[MAX];
vector<pii > graph[MAX];
bool visited[MAX];
int dist[MAX];
int path[MAX];
int C, S, Q;

struct option {
    bool operator() (const pii &a, const pii &b) const {
        return a.second > b.second;
    }
};

void prim(int src) {
    priority_queue<pii, vector<pii >, option> pq;
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
                path[v] = u;
            }
        }
    }
    
    for (int u = 2; u <= C; u++) {
        if (path[u] != -1) {
            int v = path[u];
            int w = dist[u];
            mstGraph[u].push_back(make_pair(v, w));
            mstGraph[v].push_back(make_pair(u, w));
        }
    }
}

int dfs(int src, int dst, int level) {
    if (src == dst)
        return level;
    visited[src] = true;
    for (int i = 0; i < mstGraph[src].size(); i++) {
        int v = mstGraph[src][i].first;
        int w = mstGraph[src][i].second;
        if (!visited[v]) {
            int tmpLevel = dfs(v, dst, max(level, w));
            if (tmpLevel != INF)
                return tmpLevel;
        }
    }
    return INF;
}

int main() {
    int u, v, w;
    int tc = 1;
    while (true) {
        cin >> C >> S >> Q;
        if (C == 0 && S == 0 && Q == 0)
            break;
        
        for (int i = 1; i <= C; i++) {
            mstGraph[i].clear();
            graph[i].clear();
            visited[i] = false;
            dist[i] = INF;  
            path[i] = -1;
        }
        
        for (int i = 0; i < S; i++) {
            cin >> u >> v >> w;
            graph[u].push_back(make_pair(v, w));
            graph[v].push_back(make_pair(u, w));
        }
        
        for (int i = 1; i <= C; i++)
            if (!visited[i])
                prim(i);
        
        if (tc != 1)
            cout << endl;
        cout << "Case #" << tc++ << "\n";
        for (int i = 0; i < Q; i++) {
            cin >> u >> v;
            memset(visited, false, sizeof(visited));
            int level = dfs(u, v, 0);
            if (level != INF)
                cout << level;
            else
                cout << "no path";
            cout<<"\n";
        }
    }
    return 0;
}
"""
# JAVA
"""
import java.util.*;
import java.io.*;

class Main
{ 
    static final int MAX = 110;
    static final int INF = (int)1e9;
    static ArrayList<Node> mstGraph[] = new ArrayList[MAX];
    static ArrayList<Node> graph[] = new ArrayList[MAX];
    static boolean visited[] = new boolean[MAX];
    static int path[] = new int[MAX];
    static int dist[] = new int[MAX];
    static int C, S, Q;
 
    public static void prim(int src) {
        PriorityQueue<Node> pq = new PriorityQueue<Node>();
        pq.add(new Node(src, 0));
        dist[src] = 0; 
        while (!pq.isEmpty()) {
            Node top = pq.poll();
            int u = top.id;
            visited[u] = true;
            for (int i = 0; i < graph[u].size(); i++) {
                Node neighbor = graph[u].get(i);
                int v = neighbor.id, w = neighbor.dist;
                if (!visited[v] && dist[v] > w) {
                    dist[v] = w;
                    pq.add(new Node(v, w));
                    path[v] = u;
                }
            }
        }
    
        for (int u = 2; u <= C; u++) {
            if (path[u] != -1) {
                int v = path[u];
                int w = dist[u];
                mstGraph[u].add(new Node(v, w));
                mstGraph[v].add(new Node(u, w));
            }
        }
    } 
    
    static int dfs(int src, int dst, int level) {
        if (src == dst)
            return level;
        visited[src] = true;
        for (int i = 0; i < mstGraph[src].size(); i++) {
            int v = mstGraph[src].get(i).id;
            int w = mstGraph[src].get(i).dist;
            if (!visited[v]) {
                int tmpLevel = dfs(v, dst, Math.max(level, w));
                if (tmpLevel != INF)
                    return tmpLevel;
            }
        }
        return INF;
    }
    
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int u, v, w;
        int tc = 1;
        for(int i = 0 ; i < MAX; i++) {
            graph[i] = new ArrayList<>();
            mstGraph[i] = new ArrayList<>();
        }
        while (true) {
            C = in.nextInt();
            S = in.nextInt();
            Q = in.nextInt();
            if (C == 0 && S == 0 && Q == 0)
                break;
            
            for (int i = 1; i <= C; i++) {
                mstGraph[i].clear();
                graph[i].clear();
                visited[i] = false;
                dist[i] = INF;  
                path[i] = -1;
            }

            for (int i = 0; i < S; i++) {
                u = in.nextInt();
                v = in.nextInt();
                w = in.nextInt();
                graph[u].add(new Node(v, w));
                graph[v].add(new Node(u, w));
            }
            
            for (int i = 1; i <= C; i++)
                if (!visited[i])
                    prim(i);

            if (tc != 1)
                System.out.println();
            System.out.printf("Case #%d\n", tc++);
            for (int i = 0; i < Q; i++) {
                u = in.nextInt();
                v = in.nextInt();
                Arrays.fill(visited, false);
                int level = dfs(u, v, 0);
                if (level != INF)
                    System.out.printf("%d\n", level);
                else
                    System.out.printf("no path\n");
            }
        }
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
"""

