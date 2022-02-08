# python 3
from heapq import heappush, heappop
 
def Dijkstra(s, f):
    dist = [10 ** 9] * (N + 1)
    pq = [(0, s)]
    dist[s] = 0
     
    while pq:
        w, u = heappop(pq)
         
        if u == f:
            break
         
        for weight, v in graph[u]:
            if w + weight < dist[v]:
                dist[v] = w + weight
                heappush(pq, (dist[v], v))
     
    return dist[f]
     
T = int(input())
 
for t in range(T):
    N = int(input())
    graph = [[] for i in range(N + 1)]
    cities = []
     
    for u in range(1, N + 1):
        name = input()
        cities.append(name)
        neighbors = int(input())
         
        for i in range(neighbors):
            v, w = map(int, input().split())
            graph[u].append((w, v))
     
    Q = int(input())
     
    for i in range(Q):
        sCity, fCity = input().split()
        s = cities.index(sCity) + 1
        f = cities.index(fCity) + 1
        print(Dijkstra(s, f))
     
    input()

# C++

"""
#include <bits/stdc++.h>
#define MAX 10005
using namespace std;
const int INF = 1e9 + 7;
 
vector<pair<int, int>> graph[MAX];
vector<int> dist(MAX, INF);
vector<string> cities;
 
int getIndex(string name) {
    for (int i = 0; i < cities.size(); i++) {
        if (name == cities[i]) {
            return i;
        }
    }
    return -1;
}
 
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
 
        for (pair<int, int> &neighbor : graph[u]) {
            if (w + neighbor.first < dist[neighbor.second]) {
                dist[neighbor.second] = w + neighbor.first;
                pq.push(make_pair(dist[neighbor.second], neighbor.second));
            }
        }
    }
}
 
int main() {
    int T, N, Q;
    int neighbors, u, v, w;
    string name, sCity, fCity;
    cin >> T;
 
    while (T--) {
        cin >> N;
         
        for (int i = 1; i <= N; i++) {
            graph[i].clear();
        }
        cities.clear();
         
        for (int u = 1; u <= N; u++) {
            cin >> name >> neighbors;
            cities.push_back(name);
 
            for (int i = 0; i < neighbors; i++) {
                cin >> v >> w;
                graph[u].push_back(make_pair(w, v));
            }
        }
 
        cin >> Q;
 
        for (int i = 0; i < Q; i++) {
            cin >> sCity >> fCity;
            int s = getIndex(sCity) + 1;
            int f = getIndex(fCity) + 1;
            dist = vector<int>(N + 1, INF);
            Dijkstra(s, f);
            cout << dist[f] << endl;
        }
    }
    return 0;
}
"""

# JAVA 
"""
import java.util.*;
import java.io.*;
 
public class Main {
    static final int MAX = 10005;
    static final int INF = (int)1e9 + 7;
    static int[] dist = new int[MAX];
    static ArrayList<String> cities = new ArrayList<>();
     
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
        Arrays.fill(dist, INF);
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
 
            for (Node neighbor : graph[u]) {
                if (w + neighbor.weight < dist[neighbor.id]) {
                    dist[neighbor.id] = w + neighbor.weight;
                    pq.add(new Node(neighbor.id, dist[neighbor.id]));
                }
            }
        }
    }
 
    public static void main(String[] args) {
        MyScanner in = new MyScanner();
        int T = in.nextInt();
 
        while (T-- > 0) {
            int N = in.nextInt();
             
            for (int i = 1; i <= N; i++) {
                graph[i] = new ArrayList<Node>();
            }
            cities.clear();
 
            for (int u = 1; u <= N; u++) {
                String name = in.next();
                cities.add(name);
                int neighbors = in.nextInt();
                 
                for (int i = 0; i < neighbors; i++) {
                    int v = in.nextInt();
                    int w = in.nextInt();
                    graph[u].add(new Node(v, w));
                }
            }
 
            int Q = in.nextInt();
            for (int i = 0; i < Q; i++) {
                String sCity = in.next();
                String fCity = in.next();
                int s = cities.indexOf(sCity) + 1;
                int f = cities.indexOf(fCity) + 1;
                Dijkstra(s, f);
                System.out.println(dist[f]);
            }
        }
    }
 
    public static class MyScanner {
        BufferedReader br;
        StringTokenizer st;
 
        public MyScanner() {
                br = new BufferedReader(new InputStreamReader(System.in));
        }
        String next() {
                while (st == null || !st.hasMoreElements()) {
                        try {
                                st = new StringTokenizer(br.readLine());
                        } catch (IOException e) {
                                e.printStackTrace();
                        }
                }
                return st.nextToken();
        }
        int nextInt() {
                return Integer.parseInt(next());
        }
        long nextLong() {
                return Long.parseLong(next());
        }
        double nextDouble() {
                return Double.parseDouble(next());
        }
        String nextLine() {
                String str = "";
                try {
                        str = br.readLine();
                } catch (IOException e) {
                        e.printStackTrace();
                }
                return str;
        }
    }
}
"""