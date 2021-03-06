# python 3
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
visited = [[False] * 51 for _ in range(51)]
table = []
lakes = []

def DFS(sr, sc):
    s = [(sr, sc)]
    visited[sr][sc] = True

    isOcean = False
    temp = []

    while len(s):
        ur, uc = s.pop()
        temp.append((ur, uc))

        if ur == 0 or uc == 0 or ur == n - 1 or uc == m - 1:
            isOcean = True
        
        for i in range(4):
            r = ur + dr[i]
            c = uc + dc[i]

            if r in range(n) and c in range(m) and table[r][c] == '.' and not visited[r][c]:
                visited[r][c] = True
                s.append((r, c))
    
    if not isOcean:
        lakes.append(temp)

n, m, k = map(int, input().split())

for _ in range(n):
    table.append(list(input()))

for i in range(n):
    for j in range(m):
        if not visited[i][j] and table[i][j] == '.':
            DFS(i, j)

lakes.sort(key=lambda lake: len(lake))
sum_cell = 0

for i in range(len(lakes) - k):
    sum_cell += len(lakes[i])
    for r, c in lakes[i]:
        table[r][c] = '*'

print(sum_cell)

for i in range(n):
    print(''.join(table[i]))
#  C++
"""
#include <bits/stdc++.h>
#define MAX 51
using namespace std;

const int dr[] = {0, 0, 1, -1};
const int dc[] = {1, -1, 0, 0};
int n, m, k;
bool visited[MAX][MAX];
string table[MAX];

struct Cell {
    int r, c;
};

vector<vector<Cell>> lakes;

bool sortBySize(const vector<Cell> &a, const vector<Cell> &b) {
    return a.size() < b.size();
}

bool isValid(int r, int c) {
    return r >= 0 && c >= 0 && r < n && c < m;
}

bool onBorder(int r, int c) {
    return r == 0 || c == 0 || r == n - 1 || c == m - 1;
}

void DFS(Cell scr) {
    stack<Cell> s;
    visited[scr.r][scr.c] = true;
    s.push(scr);
    
    bool isOcean = false;
    vector<Cell> temp;

    while (!s.empty()) {
        Cell u = s.top();
        temp.push_back(u);
        s.pop();

        if (onBorder(u.r, u.c)) {
            isOcean = true;
        }

        for (int i = 0; i < 4; i++) {
            int r = u.r + dr[i];
            int c = u.c + dc[i];

            if (isValid(r, c) && table[r][c] == '.' && !visited[r][c]) {
                visited[r][c] = true;
                s.push((Cell) {r, c});
            }
        }
    }

    if (!isOcean) {
        lakes.push_back(temp);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> n >> m >> k;

    for (int i = 0; i < n; i++) {
        cin >> table[i];
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (!visited[i][j] && table[i][j] == '.') {
                DFS((Cell) {i, j});
            }
        }
    }

    sort(lakes.begin(), lakes.end(), sortBySize);

    int sum_cell = 0;

    for (int i = 0; i < lakes.size() - k; i++) {
        sum_cell += lakes[i].size();
        
        for (int j = 0; j < lakes[i].size(); j++) {
            Cell u = lakes[i][j];
            table[u.r][u.c] = '*';
        }
    }

    cout << sum_cell << endl;

    for (int i = 0; i < n; i++) {
        cout << table[i] << endl;
    }

    return 0;
}
"""
# JAVA

"""
import java.util.*;

public class Main {
    static final int MAX = 51;
    static int[] dr = {0, 0, 1, -1};
    static int[] dc = {1, -1, 0, 0};
    static int n, m, k;
    static boolean[][] visited = new boolean[MAX][MAX];
    static char[][] table = new char[MAX][MAX];

    static class Cell {
        int r, c;

        public Cell(int _r, int _c) {
            this.r = _r;
            this.c = _c;
        }
    };

    static ArrayList<ArrayList<Cell>> lakes = new ArrayList<ArrayList<Cell>>();

    public static boolean isValid(int r, int c) {
        return r >= 0 && c >= 0 && r < n && c < m;
    }

    public static boolean onBorder(int r, int c) {
        return r == 0 || c == 0 || r == n - 1 || c == m - 1;
    }

    public static void DFS(Cell scr) {
        Stack<Cell> s = new Stack<>();
        visited[scr.r][scr.c] = true;
        s.add(scr);

        boolean isOcean = false;
        ArrayList<Cell> temp = new ArrayList<>();

        while (!s.isEmpty()) {
            Cell u = s.pop();
            temp.add(u);

            if (onBorder(u.r, u.c)) {
                isOcean = true;
            }

            for (int i = 0; i < 4; i++) {
                int r = u.r + dr[i];
                int c = u.c + dc[i];

                if (isValid(r, c) && table[r][c] == '.' && !visited[r][c]) {
                    visited[r][c] = true;
                    s.add(new Cell(r, c));
                }
            }
        }

        if (!isOcean) {
            lakes.add(temp);
        }
    }

    public static void main(String[] agrs) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        k = sc.nextInt();

        for (int i = 0; i < n; i++) {
            table[i] = sc.next().toCharArray();
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (!visited[i][j] && table[i][j] == '.') {
                    DFS(new Cell(i, j));
                }
            }
        }

        Collections.sort(lakes, new Comparator<ArrayList<Cell>>() {
            public int compare(ArrayList<Cell> a, ArrayList<Cell> b) {
                return a.size() - b.size();
            }
        });

        int sum_cell = 0;

        for (int i = 0; i < lakes.size() - k; i++) {
            sum_cell += lakes.get(i).size();
            for (Cell u : lakes.get(i)) {
                table[u.r][u.c] = '*';
            }
        }

        System.out.println(sum_cell);

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                System.out.print(table[i][j]);
            }
            System.out.println();
        }
    }
}
"""