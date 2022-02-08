# python 3

import queue
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

MAX = 500 + 1
backyard = [None] * MAX
nsheeps = nwolves = 0

def BFS(sr, sc):
    global nsheeps, nwolves
    q = queue.Queue()
    q.put((sr, sc))

    sheep = (1 if backyard[sr][sc] == 'k' else 0)
    wolf = (1 if backyard[sr][sc] == 'v' else 0)

    canEscape = False
    backyard[sr][sc] = '#'

    while not q.empty():
        ur, uc = q.get()

        for i in range(4):
            r = ur + dr[i]
            c = uc + dc[i]

            if not (r in range(N) and c in range(M)):
                canEscape = True
                continue
            
            if backyard[r][c] != '#':
                sheep += (1 if backyard[r][c] == 'k' else 0)
                wolf += (1 if backyard[r][c] == 'v' else 0)
                backyard[r][c] = '#'
                q.put((r, c))

    if canEscape:
        nsheeps += sheep
        nwolves += wolf
    else:
        if sheep > wolf:
            nsheeps += sheep
        else:
            nwolves += wolf

line = ''
while line == '':
    line = input().strip()
    
N, M = map(int, line.split())

for i in range(N):
    backyard[i] = list(input())

for i in range(N):
    for j in range(M):
        if backyard[i][j] != '#':
            BFS(i, j)

print(nsheeps, nwolves)

# C++
"""
#include <bits/stdc++.h>
#define MAX 500 + 1
using namespace std;

const int dr[] = {0, 0, 1, -1};
const int dc[] = {1, -1, 0, 0};
int N, M;
int nsheeps, nwolves;
string backyard[MAX];

struct Cell {
    int r, c;
};

bool isValid(int r, int c) {
    return r >= 0 && c >= 0 && r < N && c < M;
}

void BFS(Cell s) {
    queue<Cell> q;
    q.push(s);

    int sheep = (backyard[s.r][s.c] == 'k');
    int wolf = (backyard[s.r][s.c] == 'v');

    bool canEscape = false;
    backyard[s.r][s.c] = '#';

    while (!q.empty()) {
        Cell u = q.front();
        q.pop();

        for (int i = 0; i < 4; i++) {
            int r = u.r + dr[i];
            int c = u.c + dc[i];

            if (!isValid(r, c)) {
                canEscape = true;
                continue;
            }

            if (backyard[r][c] != '#') {
                sheep += (backyard[r][c] == 'k');
                wolf += (backyard[r][c] == 'v');
                backyard[r][c] = '#';
                q.push((Cell) {r, c});
            }
        }
    }

    if (canEscape) {
        nsheeps += sheep;
        nwolves += wolf;
    }
    else {
        sheep > wolf ? nsheeps += sheep : nwolves += wolf;
    }
}

int main() {
    cin >> N >> M;

    for (int i = 0; i < N; i++) {
        cin >> backyard[i];
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if (backyard[i][j] != '#') {
                BFS((Cell) {i, j});
            }
        }
    }

    cout << nsheeps << " " << nwolves;
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
    static int N, M;
    static int nsheeps, nwolves;
    static char[][] backyard = new char[MAX][MAX];

    static class Cell {
        int r, c;

        public Cell(int _r, int _c) {
            this.r = _r;
            this.c = _c;
        }
    };

    public static boolean isValid(int r, int c) {
        return r >= 0 && c >= 0 && r < N && c < M;
    }

    public static void BFS(Cell s) {
        Queue<Cell> q = new LinkedList<>();
        q.add(s);

        int sheep = (backyard[s.r][s.c] == 'k' ? 1 : 0);
        int wolf = (backyard[s.r][s.c] == 'v' ? 1 : 0);

        boolean canEscape = false;
        backyard[s.r][s.c] = '#';

        while (!q.isEmpty()) {
            Cell u = q.poll();

            for (int i = 0; i < 4; i++) {
                int r = u.r + dr[i];
                int c = u.c + dc[i];

                if (!isValid(r, c)) {
                    canEscape = true;
                    continue;
                }

                if (backyard[r][c] != '#') {
                    sheep += (backyard[r][c] == 'k' ? 1 : 0);
                    wolf += (backyard[r][c] == 'v' ? 1 : 0);
                    backyard[r][c] = '#';
                    q.add(new Cell(r, c));
                }
            }
        }

        if (canEscape) {
            nsheeps += sheep;
            nwolves += wolf;
        }
        else {
            if (sheep > wolf) {
                nsheeps += sheep;
            }
            else {
                nwolves += wolf;
            }
        }
    }

    public static void main(String[] agrs) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        M = sc.nextInt();

        for (int i = 0; i < N; i++) {
            backyard[i] = sc.next().toCharArray();
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (backyard[i][j] != '#') {
                    BFS(new Cell(i, j));
                }
            }
        }

        System.out.print(nsheeps + " " + nwolves);
    }
}
"""