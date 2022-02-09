# python 3
import queue

class Node:
    def __init__(self, dist, index):
        self.dist = dist
        self.index = index
    
    def __lt__(self, other):
        return self.dist < other.dist

def Prim(s):
    dist = [10 ** 9] * (N + 1)
    visited = [False] * (N + 1)
    pq = queue.PriorityQueue()
    pq.put(Node(0, s))
    dist[s] = 0

    while not pq.empty():
        u = pq.get().index
        visited[u] = True

        for neighbor in graph[u]:
            v = neighbor.index
            w = neighbor.dist
            if not visited[v] and w < dist[v]:
                dist[v] = w
                pq.put(Node(w, v))
    
    res = 0
    for i in range(1, N + 1):
        if not visited[i]:
            continue
        res += dist[i]
    return res

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append(Node(w, v))
    graph[v].append(Node(w, u))

print(Prim(N))
# C++
"""
#include <bits/stdc++.h>
#define MAX 10005
using namespace std;
const int INF = 1e9 + 7;

int N, M;
bool visited[MAX];
int dist[MAX];
vector<pair<int, int>> graph[MAX];

long long Prim(int s) {
    fill(dist, dist + (N + 1), INF);
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push(make_pair(0, s));
    dist[s] = 0;

    while (!pq.empty()) {
        int u = pq.top().second;
        pq.pop();
        visited[u] = true;

        for (pair<int, int> &neighbor : graph[u]) {
            int v = neighbor.second;
            int w = neighbor.first;

            if (!visited[v] && w < dist[v]) {
                dist[v] = w;
                pq.push(make_pair(w, v));
            }
        }
    }

    long long res = 0;
    for (int i = 1; i <= N; i++) {
        if (!visited[i]) {
            continue;
        }
        res += dist[i];
    }
    return res;
}

int main() {
    int u, v, w;
    cin >> N >> M;

    for (int i = 0; i < M; i++) {
        cin >> u >> v >> w;
        graph[u].push_back(make_pair(w, v));
        graph[v].push_back(make_pair(w, u));
    }

    cout << Prim(N);
    return 0;
}
"""
# JAVA
"""
import java.util.*;
import java.io.*;


public class Main
{ 
    static PrintWriter out;
    final static int MAX =  10005;
    static int N;
    static int []path = new int[MAX];
    static int []dist = new int[MAX];
    static boolean[] visited = new boolean[MAX];
    static ArrayList<Pair<Integer,Integer> > graph[];

    public static void main(String[] args) {
        MyScanner in = new MyScanner();
        out = new PrintWriter(new BufferedOutputStream(System.out), true);
        int M,u,v,w;
        
        N = in.nextInt();
        M = in.nextInt();
        graph = new ArrayList[MAX];
        
        
        // initialize variable
        for(int i = 0 ; i < MAX ; i++){
            graph[i] = new ArrayList<>();
            path[i] = -1;
            dist[i] = Integer.MAX_VALUE;
            visited[i] = false;
        }
        int s = 0;
        for (int i = 0; i<M; i++)
    	{
            u = in.nextInt();
            v = in.nextInt();
            w = in.nextInt();
            s = u-1;
            graph[u-1].add(new Pair(v-1, w));
            graph[v-1].add(new Pair(u-1, w));
    	}
        Prim(s);
        PrintMST();
    }
    
    
    static void Prim(int source){
        PriorityQueue< Pair<Integer,Integer> > pq = new PriorityQueue<>(new Comparator<Pair<Integer, Integer>>(){
            public int compare(Pair<Integer,Integer> a, Pair<Integer,Integer> b){
                return a.getFirst() - b.getFirst();
            }
        });
        pq.add(new Pair(0,source));
        dist[source] = 0;

    	while(!pq.isEmpty())
    	{
            int node = pq.peek().getSecond();
            int d = pq.peek().getFirst();
            pq.remove();
            visited[node]= true;
            for(int i=0; i<graph[node].size(); ++i)
            {
                Pair<Integer,Integer> neighbor = graph[node].get(i);
                if(!visited[neighbor.first] && neighbor.second < dist[neighbor.first])
                {
                    dist[neighbor.first] = neighbor.second;
                    pq.add(new Pair(dist[neighbor.first],neighbor.first));
                    path[neighbor.first] = node;
                }
            }
    	}
        
    }
    
    static void PrintMST()
    {
        long ans = 0;
        for (int i = 0; i<N; i++)
        {
            if (path[i] == -1)
                continue;
            ans += dist[i];
            //cout << path[i] << " - " << i << ": " << dist[i]<<endl;	
        }
        System.out.print(ans);
        //cout<<"Weight of MST: "<<ans<<endl;
    }
    
    public static class Pair<F,S>{

        public F getFirst() {
            return first;
        }

        public void setFirst(F first) {
            this.first = first;
        }

        public S getSecond() {
            return second;
        }

        public void setSecond(S second) {
            this.second = second;
        }

        public Pair(F first, S second) {
            this.first = first;
            this.second = second;
        }
        public F first;
        public S second;
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

