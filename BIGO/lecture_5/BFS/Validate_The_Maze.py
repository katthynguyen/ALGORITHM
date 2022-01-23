# python3

import queue
 
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
MAX = 21
visited = [[False] * MAX for _ in range(MAX)]
maze = [None] * MAX
 
class Cell:
    def __init__(self, _r, _c):
        self.r = _r
        self.c = _c
 
def isValid(r, c):
    return r in range(n) and c in range(m)
 
def BFS(s, f):
    q = queue.Queue()
    visited[s.r][s.c] = True
    q.put(s)
 
    while not q.empty():
        u = q.get()
        if u.r == f.r and u.c == f.c:
            return True
 
        for i in range(4):
            r = u.r + dr[i]
            c = u.c + dc[i]
 
            if isValid(r, c) and maze[r][c] == '.' and not visited[r][c]:
                visited[r][c] = True
                q.put(Cell(r, c))
     
    return False
 
Q = int(input())
 
for _ in range(Q):
    n, m = map(int, input().split())
 
    for i in range(n):
        maze[i] = input()
     
    entrance = []
 
    for i in range(n):
        for j in range(m):
            visited[i][j] = False
            if maze[i][j] == '.' and (i == 0 or j == 0 or i == n - 1 or j == m - 1):
                entrance.append(Cell(i, j))
     
    if (len(entrance)) != 2:
        print("invalid")
    else:
        s = entrance[0]
        f = entrance[1]
        print("valid" if BFS(s, f) else "invalid")

# C++

"""
#include <bits/stdc++.h>
#define MAX 21
using namespace std;
 
const int dr[] = {0, 0, 1, -1};
const int dc[] = {1, -1, 0, 0};
int n, m;
bool visited[MAX][MAX];
string maze[MAX];
 
struct Cell {
    int r, c;
};
 
bool isValid(int r, int c) {
    return r >= 0 && r < n && c >= 0 && c < m; 
}
 
bool BFS(Cell s, Cell f) {
    queue<Cell> q;
    visited[s.r][s.c] = true;
    q.push(s);
 
    while (!q.empty()) {
        Cell u = q.front();
        q.pop();
  
        if (u.r == f.r && u.c == f.c) {
            return true;
        }
 
        for (int i = 0; i < 4; i++) {
            int r = u.r + dr[i];
            int c = u.c + dc[i];
 
            if (isValid(r, c) && maze[r][c] == '.' && !visited[r][c]) {
                visited[r][c] = true;
                q.push((Cell) {r, c});
            }
        }
    }
     
    return false;
}
 
int main() {
    int Q;
    cin >> Q;
 
    while (Q--) {
        cin >> n >> m;
 
        for (int i = 0; i < n; i++) {
            cin >> maze[i];
        }
 
        vector<Cell> entrance;
 
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                visited[i][j] = false;
                if (maze[i][j] == '.' && (i == 0 || j == 0 || i == n - 1 || j == m - 1)) {
                    entrance.push_back((Cell) {i, j});
                }
            }
        }
 
        if (entrance.size() != 2) {
            cout << "invalid" << endl;
        }
        else {
            Cell s = entrance[0];
            Cell f = entrance[1];
            cout << (BFS(s, f) ? "valid" : "invalid") << endl;
        }
    }
    return 0;
}
"""


#  JAVA
"""
import java.util.*;
import java.io.*;
 
public class Main {
    static final int MAX = 21;
    static int dr[] = {0, 0, 1, -1};
    static int dc[] = {1, -1, 0, 0};
    static int n, m;
    static boolean visited[][] = new boolean[MAX][MAX];
    static String maze[] = new String[MAX];
 
    static class Cell {
        int r, c;
 
        public Cell(int _r, int _c) {
            r = _r;
            c = _c;
        }
    };
 
    public static boolean isValid(int r, int c) {
        return r >= 0 && r < n && c >= 0 && c < m;
    }
 
    public static boolean BFS(Cell s, Cell f) {
        Queue<Cell> q = new LinkedList<>();
        visited[s.r][s.c] = true;
        q.add(s);
 
        while (!q.isEmpty()) {
            Cell u = q.poll();
 
            if (u.r == f.r && u.c == f.c) {
                return true;
            }
 
            for (int i = 0; i < 4; i++) {
                int r = u.r + dr[i];
                int c = u.c + dc[i];
 
                if (isValid(r, c) && maze[r].charAt(c) == '.' && !visited[r][c]) {
                    visited[r][c] = true;
                    q.add(new Cell(r, c));
                }
            }
        }
 
        return false;
    }
 
    public static void main(String[] agrs) {
        MyScanner in = new MyScanner();
        PrintWriter out = new PrintWriter(new BufferedOutputStream(System.out), true);
        int Q = in.nextInt();
 
        while (Q-- > 0) {
            n = in.nextInt();
            m = in.nextInt();
 
            for (int i = 0; i < n; i++) {
                maze[i] = in.nextLine();
            }
 
            ArrayList<Cell> entrance = new ArrayList<>();
 
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    visited[i][j] = false;
                    if (maze[i].charAt(j) == '.' && (i == 0 || j == 0 || i == n - 1 || j == m - 1)) {
                        entrance.add(new Cell(i, j));
                    }
                }
            }
 
            if (entrance.size() != 2) {
                out.println("invalid");
            }
            else {
                Cell s = entrance.get(0);
                Cell f = entrance.get(1);
                out.println(BFS(s, f) ? "valid" : "invalid");
            }
        }
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