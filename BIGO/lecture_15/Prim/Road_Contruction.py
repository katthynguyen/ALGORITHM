# python 3
import queue

class node:
    dist = 0
    index = 0

    def __init__(self, dist, index):
        self.dist = dist
        self.index = index

    def __lt__(self, other):
        return self.dist < other.dist

def inp():
    return map(int, input().split())

def prim(graph, src):
    n = len(graph)
    dist = [1e18 for i in range(n)]
    visited = [0 for i in range(n)]
    total_cost = 0
    dist[src] = 0
    Q = queue.PriorityQueue()
    Q.put(node(0, src))

    while not Q.empty():
        temp = Q.get()
        u = temp.index
        visited[u] = True
        for item in graph[u]:
            v = item.index
            if not visited[v] and dist[v] > item.dist:
                dist[v] = item.dist
                Q.put(node(dist[v], v))

    for i in range(n):
        if dist[i] >= 1e18:
            return "Impossible"
        total_cost += dist[i]
    return total_cost

def solve():
    testcase = int(input())
    for t in range(testcase):
        input()
        m = int(input())
        cities = dict()
        cnt = 0
        graph = []
        for i in range(m):
            name1, name2, cost = input().split()
            if name1 in cities:
                u = cities[name1]
            else:
                u = cnt
                cities[name1] = cnt
                graph.append([])
                cnt+=1
            if name2 in cities:
                v = cities[name2]
            else:
                v = cnt
                cities[name2] = cnt
                graph.append([])
                cnt+=1
            cost = int(cost)
            graph[u].append(node(cost, v))
            graph[v].append(node(cost, u))

        print("Case {}: {}".format(t + 1, prim(graph, 0)))

solve()
# C++
"""
#include <bits/stdc++.h>
using namespace std;

const int MAX = 105;
const int inf = 1e7;

int test;
map <string , int> my_map;
int n, m;
int dist[MAX];
bool visited[MAX];
vector<pair<int, int> > adj[MAX];

void Prim(int source) {
    priority_queue<pair<int , int>, vector<pair<int, int> >, greater<pair<int, int> > > pq;

    for (int i = 1; i <= n; i++) {
        dist[i] = inf;
        visited[i] = false;
    }
    pq.push(make_pair(0 , source));
    dist[source] = 0;

    while (!pq.empty()) {
        pair <int , int> tmp = pq.top();
        pq.pop();
        int u = tmp.second;
        visited[u] = true;

        for (int i = 0; i < adj[u].size(); i++) {
            pair<int , int> neighbor = adj[u][i];
            int v = neighbor.first;
            int c = neighbor.second;

            if (!visited[v] && dist[v] > c) {
                dist[v] = c;
                pq.push(make_pair(c , v));
            }
        }
    }

    int res = 0;
    for (int i = 1; i <= n; i++)
        res += dist[i];

    if (res >= inf) {
        cout << "Impossible\n";
    }
    else {
        cout << res << endl;
    }
}

int main () {
    //freopen("input.txt" , "r" , stdin);
    cin >> test;
    int t = test;

    while (test--) {
        cout << "Case " << t - test << ": ";
        cin >> m;

        my_map.clear();
        n = 0;

        for (int i = 1; i <= 2*m; i++)
            adj[i].clear();

        for (int i = 1; i <= m; i++) {
            string s1 , s2;
            int w;

            cin >> s1 >> s2 >> w;
            if (my_map.find(s1) == my_map.end()) {
                my_map[s1] = ++n;
            }

            if (my_map.find(s2) == my_map.end()) {
                my_map[s2] = ++n;
            }

            int u = my_map[s1];
            int v = my_map[s2];
            adj[u].push_back(make_pair(v , w));
            adj[v].push_back(make_pair(u , w));
        }
        Prim(1);
    }
    return 0;
}
"""
# JAVA
"""
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.TreeMap;
import java.util.Scanner;

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

public class Main {
    private static int[] dist;
    private static int[] path;
    private static boolean[] visited;
    
    public static int prim(ArrayList<ArrayList<Node>> graph) {
        PriorityQueue<Node> pq = new PriorityQueue<Node>();
        int n = graph.size();
        dist = new int[n];
        path = new int[n];
        visited = new boolean[n];
        Arrays.fill(dist, Integer.MAX_VALUE);
        Arrays.fill(path, -1);
        Arrays.fill(visited, false);
        pq.add(new Node(1, 0));
        dist[1] = 0;
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
                    path[v] = u;
                }
            }
        }
        
        int mst = 0;
        for (int i = 1; i < n; i++) {
            if (dist[i] == Integer.MAX_VALUE) {
                return -1;
            }
            mst += dist[i];
        }
        return mst;
    }
    
    public static void main (String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        for (int cs = 1; cs <= t; cs++) {
            TreeMap<String, Integer> my_map = new TreeMap<String, Integer>();
            ArrayList<ArrayList<Node>> graph = new ArrayList<ArrayList<Node>>();
            int m = sc.nextInt();
            int n = 0;
            int u, v, w;
            String s1, s2;
            
            // graph index from 1
            // add temporary graph[0]
            graph.add(new ArrayList<Node>());
            for (int i = 0; i < m; i++) {
                s1 = sc.next();
                s2 = sc.next();
                w = sc.nextInt();
                
                if (my_map.containsKey(s1) == false){
                    my_map.put(s1, ++n);
                    graph.add(new ArrayList<Node>());
                }
                if (my_map.containsKey(s2) == false) {
                    my_map.put(s2, ++n);
                    graph.add(new ArrayList<Node>());
                }
                u = my_map.get(s1);
                v = my_map.get(s2);
                graph.get(u).add(new Node(v, w));
                graph.get(v).add(new Node(u, w));
            }
            int mst = prim(graph);
            System.out.print("Case " + cs + ": ");
            if (mst == -1) {
                System.out.println("Impossible");
            }
            else {
                System.out.println(mst);
            }
        }
        return;
    }
}
"""

