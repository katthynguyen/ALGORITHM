# python 3
from queue import Queue

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

MAX = 500 + 1
level = [None] * MAX

def BFS(sr, sc, fr, fc):
    q = Queue()
    q.put((sr, sc))
    level[sr][sc] = 'X'

    while q.qsize() > 0:
        ur, uc = q.get()

        for i in range(4):
            r = ur + dr[i]
            c = uc + dc[i]

            if r == fr and c == fc and level[r][c] == 'X':
                return True

            if r in range(n) and c in range(m) and level[r][c] == '.':
                level[r][c] = 'X'
                q.put((r, c))

    return False

n, m = map(int, input().split())

for i in range(n):
    level[i] = list(input())

sr, sc = map(int, input().split())
fr, fc = map(int, input().split())

print("YES" if BFS(sr - 1, sc - 1, fr - 1, fc - 1) else "NO")
# C++

"""
#include <bits/stdc++.h>
#define MAX 500 + 1
using namespace std;

const int dr[] = {0, 0, 1, -1};
const int dc[] = {1, -1, 0, 0};
int n, m;
char level[MAX][MAX];

struct Cell {
    int r, c;
};

bool isValid(int r, int c) {
    return r >= 0 && c >= 0 && r < n && c < m;
}

bool BFS(Cell s, Cell f) {
    queue<Cell> q;
    level[s.r][s.c] = 'X';
    q.push(s);

    while (!q.empty()) {
        Cell u = q.front();
        q.pop();

        for (int i = 0; i < 4; i++) {
            int r = u.r + dr[i];
            int c = u.c + dc[i];

            if (r == f.r && c == f.c && level[r][c] == 'X') {
                return true;
            }
            
            if (isValid(r, c) && level[r][c] == '.') {
                level[r][c] = 'X';
                q.push((Cell) {r, c});
            }
        }
    }

    return false;
}

int main() {
    Cell s, f;
    cin >> n >> m;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> level[i][j];
        }
    }

    cin >> s.r >> s.c >> f.r >> f.c;
    s.r -= 1, s.c -= 1, f.r -= 1, f.c -= 1;

    cout << (BFS(s, f) ? "YES" : "NO");
    return 0;
}
"""
# JAVA

"""
import java.util.*;

public class Main {
    static final int MAX = 500 + 1;
    static int[] dr = {0, 0, 1, -1};
    static int[] dc = {1, -1, 0, 0};
    static int n, m;
    static char[][] level = new char[MAX][MAX];

    static class Cell {
        int r, c;

        public Cell(int _r, int _c) {
            this.r = _r;
            this.c = _c;
        }
    };

    public static boolean isValid(int r, int c) {
        return r >= 0 && c >= 0 && r < n && c < m;
    }

    public static boolean BFS(Cell s, Cell f) {
        Queue<Cell> q = new LinkedList<>();
        level[s.r][s.c] = 'X';
        q.add(s);

        while (!q.isEmpty()) {
            Cell u = q.poll();

            for (int i = 0; i < 4; i++) {
                int r = u.r + dr[i];
                int c = u.c + dc[i];

                if (r == f.r && c == f.c && level[r][c] == 'X') {
                    return true;
                }

                if (isValid(r, c) && level[r][c] == '.') {
                    level[r][c] = 'X';
                    q.add(new Cell(r, c));
                }
            }
        }

        return false;
    }

    public static void main(String[] agrs) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();

        for (int i = 0; i < n; i++) {
            level[i] = sc.next().toCharArray();
        }

        Cell s = new Cell(sc.nextInt() - 1, sc.nextInt() - 1);
        Cell f = new Cell(sc.nextInt() - 1, sc.nextInt() - 1);

        System.out.print(BFS(s, f) ? "YES" : "NO");
    }
}
"""