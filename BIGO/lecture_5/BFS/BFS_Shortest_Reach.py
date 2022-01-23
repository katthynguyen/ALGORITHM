# python3
import queue
 
MAX = 1000 + 5
visited = [False] * MAX
dist = [0] * MAX
graph = [[] for i in range(MAX)]
 
def BFS(s):
    q = queue.Queue()
    visited[s] = True
    q.put(s)
 
    while not q.empty():
        u = q.get()
 
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                dist[v] = dist[u] + 1
                q.put(v)
 
Q = int(input())
 
for _ in range(Q):
    V, E = map(int, input().split())
 
    for i in range(MAX):
        graph[i].clear()
        visited[i] = False
        dist[i] = 0
     
    for i in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
     
    s = int(input())
    BFS(s)
 
    for i in range(1, V + 1):
        if i == s:
            continue
         
        print(dist[i] * 6 if visited[i] else -1, end=' ')
 
    print()

#  C++

"""
#include <bits/stdc++.h>
#define MAX 1000 + 5
using namespace std;
 
int V, E;
bool visited[MAX];
int dist[MAX];
vector<int> graph[MAX];
 
void BFS(int s) {
    queue<int> q;
    visited[s] = true;
    q.push(s);
 
    while (!q.empty()) {
        int u = q.front();
        q.pop();
 
        for (int &v : graph[u]) {
            if (!visited[v]) {
                visited[v] = true;
                dist[v] = dist[u] + 1;
                q.push(v);
            }
        }
    }
}
 
int main() {
    int Q, u, v, s;
    cin >> Q;
 
    while (Q--) {
        cin >> V >> E;
 
        for (int i = 0; i < MAX; i++) {
            graph[i].clear();
            visited[i] = false;
            dist[i] = 0;
        }
         
        for (int i = 0; i < E; i++) {
            cin >> u >> v;
            graph[u].push_back(v);
            graph[v].push_back(u);
        }
 
        cin >> s;
        BFS(s);
 
        for (int i = 1; i <= V; i++) {
            if (i == s) {
                continue;
            }
 
            cout << (visited[i] ? dist[i] * 6 : -1) << " ";
        }
 
        cout << endl;
    }
    return 0;
}
"""

# JAVA 

"""
import java.util.*;
 
public class Main {
    static final int MAX = 1000 + 5;
    static int V, E;
    static boolean[] visited = new boolean[MAX];
    static int[] dist = new int[MAX];
    static ArrayList<Integer> graph[] = new ArrayList[MAX];
 
    public static void BFS(int s) {
        Queue<Integer> q = new LinkedList<>();
        visited[s] = true;
        q.add(s);
 
        while (!q.isEmpty()) {
            int u = q.poll();
 
            for (int v : graph[u]) {
                if (!visited[v]) {
                    visited[v] = true;
                    dist[v] = dist[u] + 1;
                    q.add(v);
                }
            }
        }
    }
 
    public static void main(String[] agrs) {
        Scanner sc = new Scanner(System.in);
        int Q = sc.nextInt();
         
        for (int i = 0; i < MAX; i++) {
            graph[i] = new ArrayList<>();
        }
 
        while (Q-- > 0) {
            V = sc.nextInt();
            E = sc.nextInt();
 
            for (int i = 0; i < MAX; i++) {
                graph[i].clear();
                visited[i] = false;
                dist[i] = 0;
            }
 
            for (int i = 0; i < E; i++) {
                int u = sc.nextInt();
                int v = sc.nextInt();
                graph[u].add(v);
                graph[v].add(u);
            }
 
            int s = sc.nextInt();
            BFS(s);
 
            for (int i = 1; i <= V; i++) {
                if (i == s) {
                    continue;
                }
 
                System.out.print((visited[i] ? dist[i] * 6 : -1) + " ");
            }
 
            System.out.println();
        }
    }
}
"""