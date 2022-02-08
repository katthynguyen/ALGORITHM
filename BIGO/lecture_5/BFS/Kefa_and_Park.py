# python 3
import queue
 
MAX = 100000 + 5
cat = [0] * MAX
visited = [False] * MAX
graph = [[] for _ in range(MAX)]
 
def BFS(s):
    nrestaurants = 0
    q = queue.Queue()
    visited[s] = True
    q.put(s)
 
    cat[s] = (1 if a[s] == 1 else 0)
 
    while not q.empty():
        u = q.get()
 
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
             
                if a[v] == 1:
                    cat[v] = cat[u] + 1
                 
                if cat[v] <= m:
                    if len(graph[v]) == 1:
                        nrestaurants += 1
                    else:
                        q.put(v)
     
    return nrestaurants
 
n, m = map(int, input().split())
a = [None] + list(map(int, input().split()))
 
for i in range(1, n):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
 
print(BFS(1))

# C++
#include <bits/stdc++.h>
#define MAX 100000 + 5
# using namespace std;
 
# int n, m;
# int a[MAX], cat[MAX];
# bool visited[MAX];
# vector<int> graph[MAX];
 
# int BFS(int s) {
#     int nrestaurants = 0;
#     queue<int> q;
#     visited[s] = true;
#     q.push(s);
 
#     cat[s] = (a[s] == 1);
 
#     while (!q.empty()) {
#         int u = q.front();
#         q.pop();
 
#         for (int &v : graph[u]) {
#             if (!visited[v]) {
#                 visited[v] = true;
 
#                 if (a[v] == 1) {
#                     cat[v] = cat[u] + 1;
#                 }
 
#                 if (cat[v] <= m) {
#                     if (graph[v].size() == 1) {
#                         nrestaurants++;
#                     }
#                     else {
#                         q.push(v);
#                     }
#                 }
#             }
#         }
#     }
 
#     return nrestaurants;
# }
 
# int main() {
#     int u, v;
#     cin >> n >> m;
 
#     for (int i = 1; i <= n; i++) {
#         cin >> a[i];
#     }
 
#     for (int i = 1; i < n; i++) {
#         cin >> u >> v;
#         graph[u].push_back(v);
#         graph[v].push_back(u);
#     }
 
#     cout << BFS(1);
#     return 0;
# }

# # Java
# import java.util.*;
 
# public class Main {
#     static final int MAX = 100000 + 5;
#     static int n, m;
#     static int[] a = new int[MAX];
#     static int[] cat = new int[MAX];
#     static boolean[] visited = new boolean[MAX];
#     static ArrayList<Integer> graph[] = new ArrayList[MAX];
 
#     public static int BFS(int s) {
#         int nrestaurants = 0;
#         Queue<Integer> q = new LinkedList<>();
#         visited[s] = true;
#         q.add(s);
 
#         cat[s] = (a[s] == 1 ? 1 : 0);
 
#         while (!q.isEmpty()) {
#             int u = q.poll();
 
#             for (int v : graph[u]) {
#                 if (!visited[v]) {
#                     visited[v] = true;
 
#                     if (a[v] == 1) {
#                         cat[v] = cat[u] + 1;
#                     }
     
#                     if (cat[v] <= m) {
#                         if (graph[v].size() == 1) {
#                             nrestaurants++;
#                         }
#                         else {
#                             q.add(v);
#                         }
#                     }
#                 }                
#             }
#         }
 
#         return nrestaurants;
#     }
 
#     public static void main(String[] agrs) {
#         Scanner sc = new Scanner(System.in);
#         n = sc.nextInt();
#         m = sc.nextInt();
 
#         for (int i = 1; i <= n; i++) {
#             a[i] = sc.nextInt();
#             graph[i] = new ArrayList<>();
#         }
 
#         for (int i = 1; i < n; i++) {
#             int u = sc.nextInt();
#             int v = sc.nextInt();
#             graph[u].add(v);
#             graph[v].add(u);
#         }
 
#         System.out.print(BFS(1));
#     }   
# }