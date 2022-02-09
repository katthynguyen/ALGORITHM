# python 3
import queue


class node:
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
        total_cost += dist[i]
    return total_cost


def solve():
    testcase = int(input())
    for t in range(testcase):
        p = int(input())
        n = int(input())
        m = int(input())

        graph = [[] for i in range(n)]
        for i in range(m):
            u, v, val = inp()
            u -= 1
            v -= 1
            graph[u].append(node(val, v))
            graph[v].append(node(val, u))
        print(prim(graph, 0) * p)


solve()
# C++
"""
#include <stdio.h>
#include <algorithm>
#include <iostream>
#include <iterator>
#include <numeric>
#include <sstream>
#include <fstream>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <string>
#include <bits/stdc++.h>
using namespace std;
#define MAX 1005
const int INF = 0x3f3f3f3f;

int dist[MAX];
bool visited[MAX];
vector<pair<int, int> > graph[MAX];

void Prim(int source) {
    priority_queue<pair<int , int>, vector<pair<int, int> >, greater<pair<int, int> > > pq;
    pq.push(make_pair(0 , source));
    dist[source] = 0;

    while (!pq.empty()) {
        pair <int , int> tmp = pq.top();
        pq.pop();
        int u = tmp.second;
        visited[u] = true;

        for (int i = 0; i < graph[u].size(); i++) {
            pair<int , int> neighbor = graph[u][i];
            int v = neighbor.first;
            int c = neighbor.second;

            if (!visited[v] && dist[v] > c) {
                dist[v] = c;
                pq.push(make_pair(c , v));
            }
        }
    }
}

int main()
{
    // freopen("INPUT.INP", "rt", stdin);
    ios::sync_with_stdio(false);
    int t, p, n, m, a, b, c;
    cin >> t;
    while(t--)
    {
        cin >> p >> n >> m;
        for (int i = 0; i < n; i++) {
            graph[i].clear();
            visited[i] = false;
            dist[i] = INF;
        }
        for(int i = 0; i < m; i++)
        {
            cin >> a >> b >> c;
            graph[a - 1].push_back(make_pair(b - 1, c));
            graph[b - 1].push_back(make_pair(a - 1, c));
        }
        Prim(0);
        int res = 0;
        for (int i = 0; i < n; i++)
            res += dist[i];
        cout << res * p << "\n";
    }
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
    static int []key = new int[MAX];
    static boolean[] visited = new boolean[MAX];
    static ArrayList<Pair<Integer,Integer> > graph[];

    public static void main(String[] args) {
        MyScanner in = new MyScanner();
        out = new PrintWriter(new BufferedOutputStream(System.out), true);
        int p,n,m,a,b,c,s;
        int T;
        graph = new ArrayList[MAX];
        // initialize
        for(int i = 0 ; i < MAX ; i++){
            graph[i] = new ArrayList<>();
        }
        T = in.nextInt();
        while(T-->0){
            s = 0;
            // initialize variable
            for(int i = 0 ; i < MAX ; i++){
                graph[i].clear();
                path[i] = -1;
                key[i] = Integer.MAX_VALUE;
                visited[i] = false;
            }
            p = in.nextInt();
            n = in.nextInt();
            m = in.nextInt();
            for (int i = 0; i<m; i++)
            {
                a = in.nextInt();
                b = in.nextInt();
                c = in.nextInt();
                graph[a-1].add(new Pair(b-1, c));
                graph[b-1].add(new Pair(a-1, c));
            }   
            Prim(s);
            long ans = 0;
            for(int i = 0; i < n;i++){
                s = s + key[i];
            }
            out.println(s*p);
        }
    }
    
    
    static void Prim(int source){
        PriorityQueue< Pair<Integer,Integer> > pq = new PriorityQueue<>(new Comparator<Pair<Integer, Integer>>(){
            public int compare(Pair<Integer,Integer> a, Pair<Integer,Integer> b){
                return a.getFirst() - b.getFirst();
            }
        });
        pq.add(new Pair(0,source));
        key[source] = 0;

    	while(!pq.isEmpty())
    	{
            int node = pq.peek().getSecond();
            int d = pq.peek().getFirst();
            pq.remove();
            visited[node]= true;
            for(int i=0; i<graph[node].size(); ++i)
            {
                Pair<Integer,Integer> neighbor = graph[node].get(i);
                if(!visited[neighbor.first] && neighbor.second < key[neighbor.first])
                {
                    key[neighbor.first] = neighbor.second;
                    pq.add(new Pair(key[neighbor.first],neighbor.first));
                    path[neighbor.first] = node;
                }
            }
    	}
        
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

