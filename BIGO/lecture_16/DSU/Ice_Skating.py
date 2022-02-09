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
    n = int(input())
    x = [0 for i in range(n)]
    y = [0 for i in range(n)]
    for i in range(n):
        x[i], y[i] = inp()
    ans = 0
    lab = [-1 for i in range(n)]
    cou = [1 for i in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            if x[i] == x[j] or y[i] == y[j]:
                u = getroot(lab, i)
                v = getroot(lab, j)
                if u != v:
                    union(lab, cou, u, v)

    # for i in range(n):
    #     for j in range(i + 1, n):
    #         u = getroot(lab, i)
    #         v = getroot(lab, j)
    #         if u != v:
    #             ans+=1
    #             union(lab, cou, u, v)
    # improve
    ans = lab.count(-1) - 1

    print(ans)
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

bool isSameSet(pair<int, int>& p1, pair<int, int>& p2) {
    return p1.first == p2.first || p1.second == p2.second;
}

int main() {
    int u, v, n;
    cin >> n;
    vector<pair<int, int>> p(n);

    for (int i = 0; i < n; ++i) {
        parent[i] = i;
        cin >> p[i].first >> p[i].second;

        for (int j = 0; j < i; j++) {
            if (isSameSet(p[i], p[j])) {
                unionSet(i, j);
            }
        }
    }

    int nGroup = 0;
    for (int i = 0; i < n; i++) {
        if (i == parent[i]) {
            nGroup++;
        }
    }

    cout << nGroup - 1;
    return 0;
}
"""
# JAVA
"""
import java.io.*;
import java.util.*;

public class Main {
    public static class DSU { // chỉ được để 1 class
        Integer[] parent;
        public DSU(int size) {
            parent = new Integer[size];
            for (int i = 0; i < size; i++)
                parent[i] = i;
        }
        public int find(int u) {
            if (u == parent[u])
                return u;
            return parent[u] = find(parent[u]);
        }
        public void union(int u, int v) {
            u = find(u);
            v = find(v);
            parent[v] = u;
        }
        public int count() {
            int res = 0;
            for (int i = 0; i < parent.length; i++)
                if (i == parent[i])
                    res++;
            return res;
        }
    }
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] x = new int[n];
        int[] y = new int[n];
        for (int i = 0; i < n; i++) {
            x[i] = sc.nextInt();
            y[i] = sc.nextInt();
        }
        DSU dsu = new DSU(n);
        for (int i = 0; i < n; i++)
            for (int j = 0; j < i; j++)
                if (x[i] == x[j] || y[i] == y[j])
                    dsu.union(i, j);
        System.out.println(dsu.count() - 1);
    }
}
"""

