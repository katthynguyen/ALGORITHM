#  python3
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
    return r in range(H) and c in range(W)
 
def BFS(s):
    q = queue.Queue()
    q.put(s)
    visited[s.r][s.c] = True
    count = 1
 
    while not q.empty():
        u = q.get()
 
        for i in range(4):
            r = u.r + dr[i]
            c = u.c + dc[i]
 
            if isValid(r, c) and maze[r][c] == '.' and not visited[r][c]:
                visited[r][c] = True
                q.put(Cell(r, c))
                count += 1
     
    return count
 
Q = int(input())
 
for k in range(1, Q + 1):
    W, H = map(int, input().split())
 
    for i in range(H):
        maze[i] = input()
     
    for i in range(H):    
        for j in range(W):
            if maze[i][j] == '@':
                s = Cell(i, j)
            visited[i][j] = False
 
    print("Case {}: {}".format(k, BFS(s)))
# C++
"""
#include <bits/stdc++.h>
#define MAX 21
using namespace std;
 
const int dr[] = {0, 0, 1, -1};
const int dc[] = {1, -1, 0, 0};
int W, H;
bool visited[MAX][MAX];
char maze[MAX][MAX];
 
struct Cell {
    int r, c;
};
 
bool isValid(int r, int c) {
    return r >= 0 && c >= 0 && r < H && c < W;
}
 
int BFS(Cell s) {
    queue<Cell> q;
    q.push(s);
    visited[s.r][s.c] = true;
    int count = 1;
 
    while (!q.empty()) {
        Cell u = q.front();
        q.pop();
 
        for (int i = 0; i < 4; i++) {
            int r = u.r + dr[i];
            int c = u.c + dc[i];
 
            if (isValid(r, c) && maze[r][c] == '.' && !visited[r][c]) {
                visited[r][c] = true;
                q.push((Cell) {r, c});
                count++;
            }
        }
    }
 
    return count;
}
 
int main() {
    Cell s;
    int Q;
    cin >> Q;
 
    for (int k = 1; k <= Q; k++) {
        cin >> W >> H;
 
        for (int i = 0; i < H; i++) {
            for (int j = 0; j < W; j++) {
                cin >> maze[i][j];
                 
                if (maze[i][j] == '@') {
                    s.r = i;
                    s.c = j;
                }
                 
                visited[i][j] = false;
            }
        }
 
        cout << "Case " << k << ": " << BFS(s) << endl;
    }
    return 0;
}
"""
# JAVA
"""
import java.util.*;
 
public class Main {
    static final int MAX = 21;
    static int dr[] = {0, 0, 1, -1};
    static int dc[] = {1, -1, 0, 0};
    static int W, H;
    static boolean visited[][] = new boolean[MAX][MAX];
    static String maze[] = new String[MAX];
 
    static class Cell {
        int r, c;
 
        public Cell(int _r, int _c) {
            this.r = _r;
            this.c = _c;
        }
    };
 
    public static boolean isValid(int r, int c) {
        return r >= 0 && c >= 0 && r < H && c < W;
    }
 
    public static int BFS(Cell s) {
        Queue<Cell> q = new LinkedList<>();
        q.add(s);
        visited[s.r][s.c] = true;
        int count = 1;
 
        while (!q.isEmpty()) {
            Cell u = q.poll();
 
            for (int i = 0; i < 4; i++) {
                int r = u.r + dr[i];
                int c = u.c + dc[i];
 
                if (isValid(r, c) && maze[r].charAt(c) == '.' && !visited[r][c]) {
                    visited[r][c] = true;
                    q.add(new Cell(r, c));
                    count++;
                }
            }
        }
 
        return count;
    }
     
    public static void main(String[] agrs) {
        Scanner sc = new Scanner(System.in);
        int Q = sc.nextInt();
        Cell s = new Cell(0, 0);
 
        for (int k = 1; k <= Q; k++) {
            W = sc.nextInt();
            H = sc.nextInt();
 
            for (int i = 0; i < H; i++) {
                maze[i] = sc.next();
                 
                for (int j = 0; j < W; j++) {
                    if (maze[i].charAt(j) == '@') {
                        s = new Cell(i, j);
                    }
                 
                    visited[i][j] = false;
                }
            }
             
            System.out.println("Case " + k + ": " + BFS(s));
        }   
    }
}
"""