# python 3
import sys
sys.setrecursionlimit(10000000)

DIR = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

case = 0
while True:
    case += 1
    h, w = map(int, input().split())
    if h == 0 and w == 0:
        break
    a = []
    for i in range(h):
        a.append(input())
    dist = [[0] * w for i in range(h)]

    def find_path(u, v):
        if dist[u][v]:
            return dist[u][v]
        max_path = 0
        for dx, dy in DIR:
            n_u, n_v = u + dx, v + dy
            if n_u < 0 or n_u >= h or n_v < 0 or n_v >= w or ord(a[n_u][n_v]) != ord(a[u][v]) + 1:
                continue
            max_path = max(max_path, find_path(n_u, n_v))
        dist[u][v] = max_path + 1
        return dist[u][v]

    res = 0
    for x in range(h):
        for y in range(w):
            if a[x][y] == 'A':
                res = max(res, find_path(x, y))
    print('Case {}: {}'.format(case, res))
# C++
"""
#include <bits/stdc++.h>
#define MAX 51
using namespace std;

const int dr[] = {0, 0, 1, 1, 1, -1, -1, -1};
const int dc[] = {1, -1, 0, 1, -1, 0, 1, -1};

int W, H, res;
char table[MAX][MAX];
int visited[MAX][MAX];

bool isValid(int r, int c) {
    return r >= 0 && c >= 0 && r < H && c < W;
}

int DFS(int sr, int sc) {
    int count = 0;

    for (int i = 0; i < 8; i++) {
        int r = sr + dr[i];
        int c = sc + dc[i];

        if (isValid(r, c) && table[r][c] - table[sr][sc] == 1 && visited[r][c] == 0) {
            DFS(r, c);
            count = max(count, visited[r][c]);
        }
    }

    visited[sr][sc] = count + 1;
    return visited[sr][sc];
}

int main() {
    int T = 1;

    while (true) {
        int res = 0;
        cin >> H >> W;

        if (H == 0 && W == 0) {
            break;
        }

        for (int i = 0; i < H; i++) {
            for (int j = 0; j < W; j++) {
                cin >> table[i][j];
                visited[i][j] = 0;
            }
        }

        for (int i = 0; i < H; i++) {
            for (int j = 0; j < W; j++) {
                if (table[i][j] == 'A') {
                    res = max(res, DFS(i, j));
                }
            }
        }

        cout << "Case " << T++ << ": " << res << endl;
    }
    return 0;
}
"""
# JAVA

"""
import java.util.Scanner;
public class Main {
	static final int maxn = 1000;
	static int dx[] = {-1, -1, -1, 0, 0, 1, 1, 1};
	static int dy[] = {-1, 0, 1, -1, 1, -1, 0, 1};
	static Scanner sc = new Scanner(System.in);
	static int n, m, ans;
	static int visited[][] = new int[maxn][maxn];
	static String a[] = new String[maxn];

	static int max(int x, int y) {
		if (x > y) return x;
		return y;
	}

	static int dfs(int u, int v) {
		int s = 0;
		for (int i = 0; i < 8; i++) {
			int n_u = u + dx[i];
			int n_v = v + dy[i];
			if (n_u >= 0 && n_u < n && n_v >= 0 && n_v < m)
				if (a[n_u].charAt(n_v) - a[u].charAt(v) == 1) {
					if (visited[n_u][n_v] == 0) dfs(n_u, n_v);
					s = max(s, visited[n_u][n_v]);
				}
		}
		visited[u][v] = s + 1;
		return visited[u][v];
	}

	public static void main(String[] args) {
		int p = 0;
		while (true) {
			ans = 0;
			n = sc.nextInt();
			m = sc.nextInt();
			for (int i = 0; i < n; i++)
				for (int j = 0; j < m; j++)
					visited[i][j] = 0;
			if (n * m == 0) break;
			for (int i = 0; i < n; i++)
				a[i] = sc.next();
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < m; j++) {
					if (a[i].charAt(j) == 'A') {
						ans = max(ans, dfs(i, j));
					}
				}
			}
			p++;
			System.out.println("Case " + p + ": " + ans);
		}

	}
}
"""