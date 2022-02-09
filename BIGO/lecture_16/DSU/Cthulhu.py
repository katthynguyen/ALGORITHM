# python 3
import sys

def getroot(lab, u):
    if lab[u] == -1:
        return u
    lab[u] = getroot(lab, lab[u])
    return lab[u]

def union(lab, cou, a, b):
    if cou[a] > cou[b]:
        cou[a] += cou[b]
        lab[b] = a
    else:
        cou[b] += cou[a]
        lab[a] = b

def inp():
    return map(int, input().split())

def solve():
    n, m = inp()
    lab = [-1 for i in range(n)]
    cou = [1 for i in range(n)]

    if n != m:
        print("NO") #impossible
        return

    for i in range(m):
        u, v = inp()
        u = getroot(lab, u-1)
        v = getroot(lab, v-1)
        if u != v:
            union(lab, cou, u, v)
    if lab.count(-1) > 1: #not connected
        print("NO")
        return 

    print("FHTAGN!")

solve()
# C++
"""
#include <bits/stdc++.h>
using namespace std;
const int MAX = 105;

int parent[MAX];

int findSet(int u) {
    while (u != parent[u]) {
        u = parent[u];
    }
    return u;
}

void unionSet(int u, int v) {
    int up = findSet(u);
    int vp = findSet(v);
    parent[up] = vp;
}

int main() {
    int u, v, N, M;
    cin >> N >> M;
    
    if (N != M) {
        cout << "NO";
        return 0;
    }

    for (int i = 1; i <= N; i++) {
        parent[i] = i;
    }

    for (int i = 0; i < M; i++) {
        cin >> u >> v;
        unionSet(u, v);
    }

    int nGroup = 0;
    for (int i = 1; i <= N; i++) {
        if (i == parent[i]) {
            nGroup++;
            if (nGroup > 1) {
                break;
            }
        }
    }

    cout << (nGroup == 1 ? "FHTAGN!" : "NO");
    return 0;
}
"""
# JAVA
"""
package main;

import java.util.*;
import java.io.*;


public class Main
{ 
    static PrintWriter out;
    static final int MAX  = 110;
    static int parent[] = new int[MAX];
    static int ranks[] = new int[MAX];
    public static int Findset(int parent[], int i) {
        if(parent[i]!=i){
            return Findset(parent, parent[i]);
        }
        else
            return i;
    }
    public static void Unionset(int parent[], int x, int y)
    {
        int xroot = Findset(parent, x);
        int yroot = Findset(parent, y);

        if (ranks[xroot] < ranks[yroot])
            parent[xroot] = yroot;
        else if (ranks[xroot] > ranks[yroot])
            parent[yroot] = xroot;
        else{
            parent[yroot] = xroot;
            ranks[xroot]++;
        }
    }
    
    public static void main(String[] args) {
        MyScanner in = new MyScanner();
        out = new PrintWriter(new BufferedOutputStream(System.out), true);
        int i, j, k, n, m;
        n = in.nextInt();
        m = in.nextInt();
        for(i=0; i<=n; i++)
            parent[i] = i;
        for(i=0; i<m; i++)
        {
            int x, y, f1, f2;
            x = in.nextInt();
            y = in.nextInt();
            f1 = Findset(parent, x);
            f2 = Findset(parent, y);
            Unionset(parent, f1, f2);
        }
        int flag = 1;
        if(m!=n)
            flag = 0;
        for(i=1; i<=n; i++)
        {
            int temp1 = Findset(parent, i);
            int temp2 = Findset(parent, 1);
            if(temp1 != temp2)
                    flag = 0;
        }
        if(flag==1)
                out.printf("FHTAGN!");
        else
                out.printf("NO");
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

