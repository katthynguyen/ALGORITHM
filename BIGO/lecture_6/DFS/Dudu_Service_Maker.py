# python 3
import sys
visited = [False] * 10005
graph = [[] for _ in range(10005)]
 
sys.setrecursionlimit(10005)
def DFS(u):
    visited[u] = 1
 
    for v in graph[u]:
        if visited[v] == 1:
            return True
        elif visited[v] == 0:
            if DFS(v):
                return True
     
    visited[u] = 2
    return False
 
T = int(input())
 
for _ in range(T):
    N, M = map(int, input().split())
 
    for i in range(N + 1):
        graph[i].clear()
        visited[i] = 0
     
    for i in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
     
    isCyclic = False
 
    for i in range(1, N + 1):
        if visited[i] == 0:
            isCyclic = DFS(i)
            if isCyclic:
                break
     
    print("YES" if isCyclic else "NO")
# C++

"""

#include <bits/stdc++.h>
#define MAX 10005
using namespace std;

int N, M;
int visited[MAX];
vector<int> graph[MAX];

bool DFS(int u) {
    visited[u] = 1;

    for (int &v : graph[u]) {
        if (visited[v] == 1) {
            return true;
        }
        else if (visited[v] == 0) {
            if (DFS(v)) {
                return true;
            }
        }
    }

    visited[u] = 2;
    return false;
}

int main() {
    int T, u, v;
    cin >> T;

    while (T--) {
        cin >> N >> M;

        for (int i = 1; i <= N; i++) {
            graph[i].clear();
            visited[i] = 0;
        }

        for (int i = 0; i < M; i++) {
            cin >> u >> v;
            graph[u].push_back(v);
        }

        bool isCyclic = false;

        for (int i = 1; i <= N; i++) {
            if (visited[i] == 0) {
                isCyclic = DFS(i);
                if (isCyclic) {
                    break;
                }
            }
        }

        cout << (isCyclic ? "YES" : "NO") << endl;
    }
    return 0;
}
"""

# JAVA

"""
import java.util.*;

public class Main {
    static final int MAX = 10005;
    static int N, M;
    static int[] visited = new int[MAX];
    static ArrayList<Integer> graph[] = new ArrayList[MAX];

    public static boolean DFS(int u) {
        visited[u] = 1;

        for (int v : graph[u]) {
            if (visited[v] == 1) {
                return true;
            }
            else if (visited[v] == 0) {
                if (DFS(v)) {
                    return true;
                }
            }
        }

        visited[u] = 2;
        return false;
    }

    public static void main(String[] agrs) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        
        while (T-- > 0) {
            N = sc.nextInt();
            M = sc.nextInt();

            for (int i = 1; i <= N; i++) {
                graph[i] = new ArrayList<Integer>();
                visited[i] = 0;
            }

            for (int i = 0; i < M; i++) {
                int u = sc.nextInt();
                int v = sc.nextInt();
                graph[u].add(v);
            }

            boolean isCyclic = false;

            for (int i = 1; i <= N; i++) {
                if (visited[i] == 0) {
                    isCyclic = DFS(i);
                    if (isCyclic) {
                        break;
                    }
                }
            }

            System.out.println(isCyclic ? "YES" : "NO");
        }
    }
}
"""