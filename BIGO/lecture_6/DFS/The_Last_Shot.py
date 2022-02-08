# Python 3
class Scanner:
    import sys
    def __init__(self, istream = sys.stdin):
        self.tokenizer = Scanner.__tokenizer__(istream)
    def __tokenizer__(istream):
        for line in istream:
            for token in line.strip().split():
                yield token
        while True:
            yield None
    def next(self, type = str, rep = 1):
        if rep == 1:
            return type(self.tokenizer.__next__())
        return [type(self.tokenizer.__next__()) for i in range(rep)]

graph = [[] for _ in range(10005)]

def DFS(scr):
    visited = [False] * (N + 1)
    s = [scr]
    visited[scr] = True
    nbombs = 0

    while len(s):
        u = s.pop()
        nbombs += 1

        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                s.append(v)

    return nbombs

sc = Scanner()
N, M = sc.next(int, 2)

for _ in range(M):
    u, v = sc.next(int, 2)
    graph[u].append(v)

max_bombs = 0

for i in range(1, N + 1):
    max_bombs = max(max_bombs, DFS(i))

print(max_bombs)
#  C++
"""
#include <bits/stdc++.h>
#define MAX 10005
using namespace std;

int N, M;
bool visited[MAX];
vector<int> graph[MAX];

int DFS(int src) {
    memset(visited, false, sizeof(visited));
    stack<int> s;
    visited[src] = true;
    s.push(src);

    int nbombs = 0;

    while (!s.empty()) {
        int u = s.top();
        s.pop();
        nbombs++;

        for (int &v : graph[u]) {
            if (!visited[v]) {
                visited[v] = true;
                s.push(v);
            }
        }
    }

    return nbombs;
}

int main() {
    int u, v;
    cin >> N >> M;

    for (int i = 0; i < M; i++) {
        cin >> u >> v;
        graph[u].push_back(v);
    }

    int max_bombs = 0;

    for (int i = 1; i <= N; i++) {
        max_bombs = max(max_bombs, DFS(i));
    }

    cout << max_bombs;
    return 0;
}
"""

# JAVA
"""
import java.util.*;

public class Main {
    static final int MAX = 10005;
    static int N, M;
    static ArrayList<Integer> graph[] = new ArrayList[MAX];

    public static int DFS(int src) {
        boolean[] visited = new boolean[N + 1];
        Stack<Integer> s = new Stack<>();
        visited[src] = true;
        s.add(src);

        int nbombs = 0;

        while (!s.isEmpty()) {
            int u = s.pop();
            nbombs++;

            for (int v : graph[u]) {
                if (!visited[v]) {
                    visited[v] = true;
                    s.add(v);
                }
            }
        }

        return nbombs;
    }

    public static void main(String[] agrs) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        M = sc.nextInt();

        for (int i = 0; i < MAX; i++) {
            graph[i] = new ArrayList<Integer>();
        }

        for (int i = 0; i < M; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            graph[u].add(v);
        }

        int max_bombs = 0;

        for (int i = 1; i <= N; i++) {
            max_bombs = Math.max(max_bombs, DFS(i));
        }

        System.out.print(max_bombs);
    }
}
"""
