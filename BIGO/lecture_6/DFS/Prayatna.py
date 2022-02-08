# python 3
def DFS(src):
    s = [src]
    visited[src] = True

    while len(s):
        u = s.pop()
        
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                s.append(v)
    
Q = int(input())

for _ in range(Q):
    line = ''
    while line == '':
        line = input().strip()

    V = int(line)
    E = int(input())
    graph = [[] for _ in range(V)]
    visited = [False] * V

    for i in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    count = 0

    for i in range(V):
        if not visited[i]:
            count += 1
            DFS(i)
    
    print(count)

# C++

"""
#include <bits/stdc++.h>
#define MAX 100000 + 5
using namespace std;

int V, E;
bool visited[MAX];
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
                s.push(v);
            }
        }
    }
}

int main() {
    int Q, u, v;
    cin >> Q;

    while (Q--) {
        cin >> V >> E;

        for (int i = 0; i < V; i++) {
            visited[i] = false;
            graph[i].clear();
        }

        for (int i = 0; i < E; i++) {
            cin >> u >> v;
            graph[u].push_back(v);
            graph[v].push_back(u);
        }

        int count = 0;

        for (int i = 0; i < V; i++) {
            if (!visited[i]) {
                count++;
                DFS(i);
            }
        }

        cout << count << endl;
    }
    return 0;
}
"""

#  JAVA

"""
import java.util.*;
import java.io.*;

public class Main {
    static final int MAX = 100000 + 5;
    static int V, E;
    static boolean[] visited = new boolean[MAX];
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
                    s.add(v);
                }
            }
        }
    }

    public static void main(String[] agrs) {
        MyScanner in = new MyScanner();
        PrintWriter out = new PrintWriter(new BufferedOutputStream(System.out), true);
        int Q = in.nextInt();

        while (Q-- > 0) {
            V = in.nextInt();
            E = in.nextInt();

            for (int i = 0; i < V; i++) {
                visited[i] = false;
                graph[i] = new ArrayList<>();
            }

            for (int i = 0; i < E; i++) {
                int u = in.nextInt();
                int v = in.nextInt();
                graph[u].add(v);
                graph[v].add(u);
            }

            int count = 0;

            for (int i = 0; i < V; i++) {
                if (!visited[i]) {
                    count++;
                    DFS(i);
                }
            }

            out.println(count);
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