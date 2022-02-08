# python3
MAX = 1000 + 5
visited = [False] * MAX
dist = [0] * MAX
graph = [[] for _ in range(MAX)]

def DFS(scr):
    s = [scr]
    visited[scr] = True
    
    while len(s):
        u = s.pop()

        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                dist[v] = dist[u] + 1
                s.append(v)

V = int(input())
E = V - 1

for _ in range(E):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

DFS(1)
ans = 0
min_dist = MAX

Q = int(input())

for _ in range(Q):
    u = int(input())
    if dist[u] < min_dist or (dist[u] == min_dist and u < ans):
        min_dist = dist[u]
        ans = u

print(ans)
# C++
"""
#include <bits/stdc++.h>
#define MAX 1000 + 5
using namespace std;

int V, E;
bool visited[MAX];
int dist[MAX];
vector<int> graph[MAX];

void DFS(int scr) {
    stack<int> s;
    visited[scr] = true;
    s.push(scr);

    while (!s.empty()) {
        int u = s.top();
        s.pop();

        for (int &v : graph[u]) {
            if (!visited[v]) {
                visited[v] = true;
                dist[v] = dist[u] + 1;
                s.push(v);
            }
        }
    }
}

int main() {
    int Q, u, v;
    cin >> V;
    E = V - 1;

    for (int i = 0; i < E; i++) {
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    DFS(1);
    int ans = 0, min_dist = MAX;
    cin >> Q;

    for (int i = 0; i < Q; i++) {
        cin >> u;

        if (dist[u] < min_dist || (dist[u] == min_dist && u < ans)) {
            min_dist = dist[u];
            ans = u;
        }
    }
    
    cout << ans;
    return 0;
}
"""
# java
"""
import java.util.*;

public class Main {
    static final int MAX = 1000 + 5;
    static int V, E;
    static boolean[] visited = new boolean[MAX];
    static int[] dist = new int[MAX];
    static ArrayList<Integer> graph[] = new ArrayList[MAX];

    public static void DFS(int scr) {
        Stack<Integer> s = new Stack<>();
        visited[scr] = true;
        s.add(scr);

        while (!s.isEmpty()) {
            int u = s.pop();

            for (int v : graph[u]) {
                if (!visited[v]) {
                    visited[v] = true;
                    dist[v] = dist[u] + 1;
                    s.add(v);
                }
            }
        }
    }

    public static void main(String[] agrs) {
        Scanner sc = new Scanner(System.in);;
        V = sc.nextInt();
        E = V - 1;

        for (int i = 0; i < MAX; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < E; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            graph[u].add(v);
            graph[v].add(u);
        }

        DFS(1);
        int ans = 0;
        int min_dist = MAX;
        int Q = sc.nextInt();

        for (int i = 0; i < Q; i++) {
            int u = sc.nextInt();

            if (dist[u] < min_dist || (dist[u] == min_dist && u < ans)) {
                min_dist = dist[u];
                ans = u;
            }
        }

        System.out.print(ans);
    }
}
"""
