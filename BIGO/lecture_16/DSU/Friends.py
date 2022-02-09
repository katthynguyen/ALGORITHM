# python 3
def findSet(u):
    while u != parent[u]:
        u = parent[u]
    return u

def unionSet(u, v):
    up = findSet(u)
    vp = findSet(v)
    if vp != up:
        if ranks[up] < ranks[vp]:
            parent[up] = vp
            cnt[vp] += cnt[up]
        else:
            parent[vp] = up
            cnt[up] += cnt[vp]
            if ranks[up] == ranks[vp]:
                ranks[up] += 1

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    parent = [i for i in range(n + 1)]
    cnt = [1 for i in range(n + 1)]
    ranks = [0 for i in range(n + 1)]

    for i in range(m):
        u, v = map(int, input().split())
        unionSet(u, v)
    
    print(max(cnt))

# C++
"""
#include <bits/stdc++.h>
using namespace std;
const int MAX = 30005;

int parent[MAX], cnt[MAX], ranks[MAX];

int findSet(int u) {
    while (u != parent[u]) {
        u = parent[u];
    }
    return u;
}

void unionSet(int u, int v) {
    int up = findSet(u);
    int vp = findSet(v);
    if (up != vp) {
        if (ranks[up] < ranks[vp]) {
            parent[up] = vp;
            cnt[vp] += cnt[up];
        }
        else {
            parent[vp] = up;
            cnt[up] += cnt[vp];
            if (ranks[up] == ranks[vp]) {
                ranks[up] += 1;
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int u, v, t, n, m;
    cin >> t;

    while (t--) {
        cin >> n >> m;

        for (int i = 1; i <= n; i++) {
            parent[i] = i;
            cnt[i] = 1;
            ranks[i] = 0;
        }

        for (int i = 0; i < m; i++) {
            cin >> u >> v;
            unionSet(u, v);
        }

        int res = -1;
        for (int i = 1; i <= n; i++) {
            res = max(res, cnt[i]);
        }
        cout << res << endl;
    }

    return 0;
}

"""
# JAVA
"""
import java.util.*;

public class Main {
    static final int MAX = 30005;
    static int[] parent = new int[MAX];
    static int[] cnt = new int[MAX];
    static int[] ranks = new int[MAX];

    private static int findSet(int u) {
        while (u != parent[u]) {
            u = parent[u];
        }
        return u;
    }

    private static void unionSet(int u, int v) {
        int up = findSet(u);
        int vp = findSet(v);
        if (up != vp) {
            if (ranks[up] < ranks[vp]) {
                parent[up] = vp;
                cnt[vp] += cnt[up];
            }
            else {
                parent[vp] = up;
                cnt[up] += cnt[vp];
                if (ranks[up] == ranks[vp]) {
                    ranks[up] += 1;
                }
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();

        while (t-- > 0) {
            int n = sc.nextInt();
            int m = sc.nextInt();

            for (int i = 1; i <= n; i++) {
                parent[i] = i;
                cnt[i] = 1;
                ranks[i] = 0;
            }

            for (int i = 0; i < m; i++) {
                int u = sc.nextInt();
                int v = sc.nextInt();
                unionSet(u, v);
            }

            int res = -1;
            for (int i = 1; i <= n; i++) {
                res = Math.max(res, cnt[i]);
            }

            System.out.println(res);
        }
    }
}
"""

