#  python 3

INF = 10 ** 9
MAX = 28

def FloydWarshall(dist):
    for k in range(MAX):
        for i in range(MAX):
            for j in range(MAX):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

while True:
    N = int(input())
    if N == 0:
        break
    
    distS = [[0 if i == j else INF for j in range(MAX)] for i in range(MAX)]
    distD = [[0 if i == j else INF for j in range(MAX)] for i in range(MAX)]

    for _ in range(N):
        age, dir, x, y, c = input().split()
        u, v = map(lambda char: ord(char) - ord('A'), (x, y))
        c = int(c)

        if age == 'Y':
            distS[u][v] = min(distS[u][v], c)
            if dir == 'B':
                distS[v][u] = min(distS[v][u], c)
        else:
            distD[u][v] = min(distD[u][v], c)
            if dir == 'B':
                distD[v][u] = min(distD[v][u], c)
        
    s, d = map(lambda char: ord(char) - ord('A'), input().split())
    FloydWarshall(distS)
    FloydWarshall(distD)

    res = []
    minDist = INF

    for i in range(MAX):
        dist1 = distS[s][i]
        dist2 = distD[d][i]

        if dist1 != INF and dist2 != INF and dist1 + dist2 <= minDist:
            res.append((dist1 + dist2, i))
            minDist = dist1 + dist2
    
    if not res:
        print('You will never meet.')
    else:
        res.sort()
        print(minDist, end='')

        for place in res:
            if place[0] != minDist:
                break
            print(' ' + chr(place[1] + ord('A')), end = '')
        print()

# C++

"""
#include <bits/stdc++.h>
#define MAX 28
using namespace std;
const int INF = 1e9 + 7;

struct Place {
    int cost, id;

    bool operator<(const Place &other) const {
        return cost < other.cost || (cost == other.cost && id < other.id);
    }
};

int distS[MAX][MAX], distD[MAX][MAX];
vector<Place> res;

void FloydWarshall(int dist[MAX][MAX]) {
    for (int k = 0; k < MAX; k++) {
        for (int i = 0; i < MAX; i++) {
            for (int j = 0; j < MAX; j++) {
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
            }
        }
    }
}

int main() {
    int N, c;
    char age, dir, x, y;

    while (cin >> N && N != 0) {
        for (int i = 0; i < MAX; i++) {
            for (int j = 0; j < MAX; j++) {
                distS[i][j] = (i == j ? 0 : INF);
                distD[i][j] = (i == j ? 0 : INF);
            }
        }

        for (int i = 0; i < N; i++) {
            cin >> age >> dir >> x >> y >> c;
            int u = x - 'A';
            int v = y - 'A';

            if (age == 'Y') {
                distS[u][v] = min(distS[u][v], c);
                if (dir == 'B') {
                    distS[v][u] = min(distS[v][u], c);
                }
            }
            else {
                distD[u][v] = min(distD[u][v], c);
                if (dir == 'B') {
                    distD[v][u] = min(distD[v][u], c);
                }
            }
        }

        cin >> x >> y;
        int s = x - 'A';
        int d = y - 'A';
        FloydWarshall(distS);
        FloydWarshall(distD);

        res.clear();
        int minDist = INF;

        for (int i = 0; i < MAX; i++) {
            int dist1 = distS[s][i];
            int dist2 = distD[d][i];

            if (dist1 != INF && dist2 != INF && dist1 + dist2 <= minDist) {
                res.push_back({dist1 + dist2, i});
                minDist = dist1 + dist2;
            }
        }

        if (res.empty()) {
            cout << "You will never meet.";
        }
        else {
            sort(res.begin(), res.end());
            cout << minDist;

            for (Place &place : res) {
                if (place.cost != minDist) {
                    break;
                }
                cout << " " << char(place.id + 'A');
            }
        }
        cout << endl;
    }
    return 0;
}
"""

# JAVA
"""
import java.util.*;

public class Main {
    static final int INF = (int)1e9 + 7;
    static final int MAX = 28;
    static class Place implements Comparable<Place>{
        int cost, id;

        public Place(int _cost, int _id) {
            this.cost = _cost;
            this.id = _id;
        }

        @Override
        public int compareTo(Place other) {
            return (this.cost == other.cost ? this.id - other.id : this.cost - other.cost);
        }
    }

    static int[][] distS = new int[MAX][MAX];
    static int[][] distD = new int[MAX][MAX];
    static ArrayList<Place> res = new ArrayList<>();

    public static void FloydWarshall(int[][] dist) {
        for (int k = 0; k < MAX; k++) {
            for (int i = 0; i < MAX; i++) {
                for (int j = 0; j < MAX; j++) {
                    dist[i][j] = Math.min(dist[i][j], dist[i][k] + dist[k][j]);
                }
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while (true) {
            int N = sc.nextInt();
            if (N == 0) {
                break;
            }

            for (int i = 0; i < MAX; i++) {
                for (int j = 0; j < MAX; j++) {
                    distS[i][j] = (i == j ? 0 : INF);
                    distD[i][j] = (i == j ? 0 : INF);
                }
            }

            for (int i = 0; i < N; i++) {
                char age = sc.next().charAt(0);
                char dir = sc.next().charAt(0);
                char x = sc.next().charAt(0);
                char y = sc.next().charAt(0);
                int c = sc.nextInt();

                int u = x - 'A';
                int v = y - 'A';

                if (age == 'Y') {
                    distS[u][v] = Math.min(distS[u][v], c);
                    if (dir == 'B') {
                        distS[v][u] = Math.min(distS[v][u], c);
                    }
                }
                else {
                    distD[u][v] = Math.min(distD[u][v], c);
                    if (dir == 'B') {
                        distD[v][u] = Math.min(distD[v][u], c);
                    }
                }
            }

            char x = sc.next().charAt(0);
            char y = sc.next().charAt(0);
            int s = x - 'A';
            int d = y - 'A';
            FloydWarshall(distS);
            FloydWarshall(distD);

            res.clear();
            int minDist = INF;

            for (int i = 0; i < MAX; i++) {
                int dist1 = distS[s][i];
                int dist2 = distD[d][i];

                if (dist1 != INF && dist2 != INF && dist1 + dist2 <= minDist) {
                    res.add(new Place(dist1 + dist2, i));
                    minDist = dist1 + dist2;
                }
            }

            if (res.isEmpty()) {
                System.out.print("You will never meet.");
            }
            else {
                Collections.sort(res);
                System.out.print(minDist);

                for (Place place : res) {
                    if (place.cost != minDist) {
                        break;
                    }
                    System.out.print(" " + (char)(place.id + 'A'));
                }
            }
            System.out.println();
        }
    }
}
"""