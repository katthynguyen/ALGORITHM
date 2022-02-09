# python 3
INF = 10 ** 9

def FloydWarshall():
    for k in range(M):
        for i in range(M):
            for j in range(M):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

T = int(input())

for _ in range(T):
    s = input()
    M = len(s)
    dist = [[INF] * M for i in range(M)]
    matrix = []

    for i in range(M):
        if i == 0:
            matrix.append(s)
        else:
            matrix.append(input())

        for j in range(M):
            if matrix[i][j] == 'Y':
                dist[i][j] = 1
            elif i == j:
                dist[i][j] = 0
    
    FloydWarshall()
    nfriends, index = 0, 0

    for i in range(M):
        count = 0
        
        for j in range(M):
            if dist[i][j] == 2:
                count += 1
        
        if count > nfriends:
            nfriends = count
            index = i
    
    print(index, nfriends)
# C++
"""
#include <bits/stdc++.h>
#define MAX 55
using namespace std;
const int INF = 1e9 + 7;

int M;
string matrix[MAX];
int dist[MAX][MAX];

void FloydWarshall() {
    for (int k = 0; k < M; k++) {
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < M; j++) {
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
            }
        }
    }
}

int main() {
    int T;
    string s;
    cin >> T;

    while (T--) {
        cin >> s;
        M = s.length();

        for (int i = 0; i < M; i++) {
            if (i == 0) {
                matrix[0] = s;
			      }
			      else {
				        cin >> matrix[i];
			      }

            for (int j = 0; j < M; j++) {
                if (matrix[i][j] == 'Y') {
                    dist[i][j] = 1;
                }
                else {
                    dist[i][j] = (i == j ? 0 : INF);
                }
            }
        }

        FloydWarshall();
        int nfriends = 0, index = 0;

        for (int i = 0; i < M; i++) {
            int count = 0;
            
            for (int j = 0; j < M; j++) {
                if (dist[i][j] == 2) {
                    count++;
                }
            }

            if (count > nfriends) {
                nfriends = count;
                index = i;
            }
        }

        cout << index << " " << nfriends << endl;
    }
    return 0;
}
"""
# JAVA
"""
import java.util.*;
import java.io.*;

public class Main {
    static final int INF = (int)1e9 + 7;
    static final int MAX = 55;
    static int M;
    static String[] matrix = new String[MAX];
    static int dist[][] = new int[MAX][MAX];

    public static void FloydWarshall() {
        for (int k = 0; k < M; k++) {
            for (int i = 0; i < M; i++) {
                for (int j = 0; j < M; j++) {
                    dist[i][j] = Math.min(dist[i][j], dist[i][k] + dist[k][j]);
                }
            }
        }
    }

    public static void main(String[] agrs) {
        MyScanner in = new MyScanner();
        int T = in.nextInt();
        
        while (T-- > 0) {
            String s = in.next();
            M = s.length();

            for (int i = 0; i < M; i++) {
                if (i == 0) {
                    matrix[0] = s;
                }
                else {
                    matrix[i] = in.next();
                }

                for (int j = 0; j < M; j++) {
                    if (matrix[i].charAt(j) == 'Y') {
                        dist[i][j] = 1;
                    }
                    else {
                        dist[i][j] = (i == j ? 0 : INF);
                    }
                }
            }

            FloydWarshall();
            int nfriends = 0, index = 0;
            
            for (int i = 0; i < M; i++) {
                int count = 0;

                for (int j = 0; j < M; j++) {
                    if (dist[i][j] == 2) {
                        count++;
                    }
                }

                if (count > nfriends) {
                    nfriends = count;
                    index = i;
                }
            }

            System.out.println(index + " " + nfriends);
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