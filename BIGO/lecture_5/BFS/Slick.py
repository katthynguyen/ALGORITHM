# python 3
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
 
MAX = 251
table = [None] * MAX
slick = [0] * (MAX * MAX)
q = [None] * (MAX * MAX)
 
def BFS(sr, sc):
    left = right = 0
    q[0] = (sr, sc)
    table[sr][sc] = '0'
    count = 1
 
    while left <= right:
        ur, uc = q[left]
        left += 1
 
        for i in range(4):
            r = ur + dr[i]
            c = uc + dc[i]
 
            if r in range(N) and c in range(M) and table[r][c] == '1':
                right += 1
                q[right] = (r, c)
                table[r][c] = '0'
                count += 1
 
    slick[count] += 1
 
while True:
    N, M = map(int, input().split())
 
    if N == 0 and M == 0:
        break
     
    for i in range(N):
        table[i] = input().split()
        for j in range(M):
            slick[i * M + j + 1] = 0
     
    nslicks = 0
 
    for i in range(N):
        for j in range(M):
            if table[i][j] == '1':
                nslicks += 1
                BFS(i, j)
     
    print(nslicks)
 
    for i in range(1, N * M  + 1):
        if slick[i]:
            print(i, slick[i], sep=' ')

# C++
"""
#include <bits/stdc++.h>
#define MAX 251
using namespace std;
 
const int dr[] = {0, 0, 1, -1};
const int dc[] = {1, -1, 0, 0};
int N, M;
int slick[MAX * MAX];
int table[MAX][MAX];
 
struct Cell {
    int r, c;
};
 
bool isValid(int r, int c) {
    return r >= 0 && c >= 0 && r < N && c < M;
}
 
void BFS(Cell s) {
    queue<Cell> q;
    q.push(s);
    table[s.r][s.c] = 0;
    int count = 1;
 
    while (!q.empty()) {
        Cell u = q.front();
        q.pop();
 
        for (int i = 0; i < 4; i++) {
            int r = u.r + dr[i];
            int c = u.c + dc[i];
 
            if (isValid(r, c) && table[r][c] == 1) {
                table[r][c] = 0;
                q.push((Cell) {r, c});
                count++;
            }
        }
    }
 
    slick[count]++;
}
 
int main() {
    while (true) {
        cin >> N >> M;
 
        if (N == 0 && M == 0) {
            break;
        }
 
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                cin >> table[i][j];
                slick[i * M + j + 1] = 0;
            }
        }
 
        int nslicks = 0;
 
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (table[i][j] == 1) {
                    nslicks++;
                    BFS((Cell) {i, j});
                }
            }
        }
 
        cout << nslicks << endl;
 
        for (int i = 1; i <= N * M; i++) {
            if (slick[i]) {
                cout << i << " " << slick[i] << endl;
            }
        }
    }
 
    return 0;
}
"""

# JAVA
"""
import java.util.*;
 
public class Main {
    static final int MAX = 251;
    static int[] dr = {0, 0, 1, -1};
    static int[] dc = {1, -1, 0, 0};
    static int N, M;
    static int[][] table = new int[MAX][MAX];
    static int[] slick = new int[MAX * MAX];
 
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
        table[s.r][s.c] = 0;
        int count = 1;
 
        while (!q.isEmpty()) {
            Cell u = q.poll();
 
            for (int i = 0; i < 4; i++) {
                int r = u.r + dr[i];
                int c = u.c + dc[i];
 
                if (isValid(r, c) && table[r][c] == 1) {
                    table[r][c] = 0;
                    q.add(new Cell(r, c));
                    count++;
                }
            }
        }
 
        slick[count]++;
    }
 
    public static void main(String[] agrs) {
        Scanner sc = new Scanner(System.in);
        while (true) {
            N = sc.nextInt();
            M = sc.nextInt();
 
            if (N == 0 && M == 0) {
                break;
            }
 
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    table[i][j] = sc.nextInt();
                    slick[i * M + j + 1] = 0;
                }
            }
 
            int nslicks = 0;
 
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    if (table[i][j] == 1) {
                        nslicks++;
                        BFS(new Cell(i, j));
                    }
                }
            }
 
            System.out.println(nslicks);
 
            for (int i = 1; i <= N * M; i++) {
                if (slick[i] != 0) {
                    System.out.println(i + " " + slick[i]);
                }
            }
        }
    }
}
"""