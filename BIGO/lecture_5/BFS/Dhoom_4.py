# python 3
import queue
MAX = 100000 + 5
MOD = 100000
 
def BFS(s, f):
    dist = [-1] * MAX
    q = queue.Queue()
    q.put(s)
    dist[s] = 0
 
    while not q.empty():
        u = q.get()
 
        for x in a:
            v = (x * u) % MOD
 
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.put(v)
 
                if v == f:
                    return dist[v]
     
    return -1
 
s, f = map(int, input().split())
N = int(input())
a = list(map(int, input().split()))
print(BFS(s, f))
#  C++
"""
#include <bits/stdc++.h>
#define MAX 100000 + 5
#define MOD 100000
using namespace std;
 
int N;
int dist[MAX];
int a[MAX];
 
int BFS(int s, int f) {
    memset(dist, -1, sizeof(dist));
    queue<int> q;
    q.push(s);
    dist[s] = 0;
 
    while (!q.empty()) {
        int u = q.front();
        q.pop();
 
        for (int i = 0; i < N; i++) {
            int v = (1LL * a[i] * u) % MOD;
 
            if (dist[v] == -1) {
                dist[v] = dist[u] + 1;
                q.push(v);
 
                if (v == f) {
                    return dist[v];
                }
            }
        }
    }
 
    return -1;
}
 
int main() {
    int s, f;
    cin >> s >> f >> N;
 
    for (int i = 0; i < N; i++) {
        cin >> a[i];
    }
 
    cout << BFS(s, f);
    return 0;
}
"""

#  JAVA 
"""
import java.util.*;
 
public class Main {
    static final int MAX = 100000 + 5;
    static final int MOD = 100000;
    static int N;
    static int[] dist = new int[MAX];
    static int[] a = new int[MAX];
 
    public static int BFS(int s, int f) {
        Arrays.fill(dist, -1);
        Queue<Integer> q = new LinkedList<>();
        q.add(s);
        dist[s] = 0;
 
        while (!q.isEmpty()) {
            int u = q.poll();
 
            for (int i = 0; i < N; i++) {
                Long temp = (1L * a[i] * u) % MOD;
                int v = temp.intValue();
 
                if (dist[v] == -1) {
                    dist[v] = dist[u] + 1;
                    q.add(v);
 
                    if (v == f) {
                        return dist[v];
                    }
                }
            }
        }
 
        return -1;
    }
 
    public static void main(String[] agrs) {
        Scanner sc = new Scanner(System.in);
        int s = sc.nextInt();
        int f = sc.nextInt();
        N = sc.nextInt();
 
        for (int i = 0; i < N; i++) {
            a[i] = sc.nextInt();
        }
 
        System.out.print(BFS(s, f));
    }
}
"""