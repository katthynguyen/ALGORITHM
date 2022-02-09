# python 3
def FloydWarshall():
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = max(dist[i][j], dist[i][k] * dist[k][j])

t = 1
while True:
    N = int(input())
    if N == 0:
        break
    
    dist = [[1 if i == j else 0 for j in range(N)] for i in range(N)]
    currencies = []

    for _ in range(N):
        currencies.append(input().strip())
    
    M = int(input())
    for _ in range(M):
        sourceCur, rate, desCur = input().split()
        u, v = map(lambda x: currencies.index(x), (sourceCur, desCur))
        dist[u][v] = float(rate)
    input()

    FloydWarshall()

    arbitrage = False
    for i in range(N):
        if dist[i][i] > 1:
            arbitrage = True
            break
    
    print('Case {}: {}'.format(t, "Yes" if arbitrage else "No"))
    t += 1
# C++

"""
#include <iostream>
using namespace std;
const int MAX = 40;

string currencies[MAX];
double dist[MAX][MAX];
int n, m;

int findCurrency(string s){
    for (int i = 0; i < n; i++)
        if (currencies[i] == s)
            return i;
    return -1;
}

void floydWarshall() {
    for (int k = 0; k < n; k++) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (dist[i][j] < dist[i][k] * dist[k][j]) {
                    dist[i][j] = dist[i][k] * dist[k][j];
                }
            }
        }
    }
}

int main() {
    int tc = 1;
    string u, v;
    double w;

    while (true) {
        cin >> n;
        if (n == 0)
            break;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                dist[i][j] = 0;
                if (i == j)
                    dist[i][j] = 1;
            }
        }
        for (int i = 0; i < n; i++)
            cin >> currencies[i];
        cin >> m;
        for (int i = 0; i < m; i++){
            cin >> u >> w >> v;
            dist[findCurrency(u)][findCurrency(v)] = w;
        }
        floydWarshall();
        bool flag = false;
        for (int i = 0; i < n; i++) {
            if (dist[i][i] > 1) {
                flag = true;
                break;
            }
        }
        cout << "Case " << tc++ << ": " << (flag ? "Yes" : "No") << "\n";
    }
    return 0;
}
"""

# JAVA
"""
import java.util.*;
import java.io.*;

public class Solution {
    static final int MAX = 35;
    static int N, M;
    static ArrayList<String> currencies = new ArrayList<>();
    static double[][] dist = new double[MAX][MAX];

    public static void FloydWarshall() {
        for (int k = 0; k < N; k++) {
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    dist[i][j] = Math.max(dist[i][j], dist[i][k] * dist[k][j]);
                }
            }
        }
    }

    public static void main(String[] args) {
        MyScanner in = new MyScanner();
        int t = 1;

        while (true) {
            N = in.nextInt();
            if (N == 0) {
                break;
            }

            currencies.clear();
            for (int i = 0; i < N; i++) {
                currencies.add(in.next());
                for (int j = 0; j < N; j++) {
                    dist[i][j] = (i == j ? 1 : 0);
                }
            }

            M = in.nextInt();
            for (int i = 0; i < M; i++) {
                String sourceCur = in.next();
                double rate = in.nextDouble();
                String desCur = in.next();
                int u = currencies.indexOf(sourceCur);
                int v = currencies.indexOf(desCur);
                dist[u][v] = rate;
            }

            FloydWarshall();

            boolean arbitrage = false;
            for (int i = 0; i < N; i++) {
                if (dist[i][i] > 1) {
                    arbitrage = true;
                    break;
                }
            }

            System.out.print("Case " + t++ + ": ");
            System.out.println(arbitrage ? "Yes" : "No");
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