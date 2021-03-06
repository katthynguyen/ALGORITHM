# python 3
def findSet(u):
    if u != parent[u]:
        parent[u] = findSet(parent[u])
    return parent[u]

def unionSet(u, v):
    up = findSet(u)
    vp = findSet(v)

    if up == vp:
        return
    
    if ranks[up] > ranks[vp]:
        parent[vp] = up
    elif ranks[up] < ranks[vp]:
        parent[up] = vp
    else:
        parent[up] = vp
        ranks[vp] += 1

Q = int(input())
input()

while Q > 0:
    P, T = map(int, input().split())
    trees = [set() for i in range(P + 1)]
    parent = [i for i in range(P + 1)]
    ranks = [0 for i in range(P + 1)]

    while True:
        try:
            line = input()
            if not line:
                break
            person, tree = map(int, line.split())
            trees[person].add(tree)
        except EOFError:
            break

    for i in range(1, P + 1):
        for j in range(i + 1, P + 1):
            if trees[i] == trees[j]:
                unionSet(i, j)
    
    nSets = sum(1 for i in range(1, P + 1) if i == parent[i])
    print(nSets)
    Q -= 1

    if Q > 0:
        print()
# C++
"""
#include <bits/stdc++.h>
using namespace std;
const int MAX = 105;

int parent[MAX], ranks[MAX];
set<int> trees[MAX];

int findSet(int u) {
    if (u != parent[u]) {
        parent[u] = findSet(parent[u]);
    }
    return parent[u];
}

void unionSet(int u, int v) {
    int up = findSet(u);
    int vp = findSet(v);

    if (up == vp) {
        return;
    }

    if (ranks[up] > ranks[vp]) {
        parent[vp] = up;
    }
    else if (ranks[up] < ranks[vp]) {
        parent[up] = vp;
    }
    else {
        parent[up] = vp;
        ranks[vp]++;
    }
}

int main() {
    int Q, P, T, person, tree;
    string line;
    cin >> Q;

    while (Q--) {
        cin >> P >> T;
        cin.ignore();

        while (getline(cin, line) && !line.empty()) {
            stringstream ss(line);
            ss >> person >> tree;
            trees[person].insert(tree);
        }

        for (int i = 1; i <= P; i++) {
            parent[i] = i;
            ranks[i] = 0;
        }

        for (int i = 1; i <= P; i++) {
            for (int j = i + 1; j <= P; j++) {
                if (trees[i] == trees[j]) {
                    unionSet(i, j);
                }
            }
        }

        int nSets = 0;
        for (int i = 1; i <= P; i++) {
            if (i == parent[i]) {
                nSets++;
            }
            trees[i].clear();
        }

        cout << nSets << endl;
        if (Q > 0) {
            cout << endl;
        }
    }
    return 0;
}
"""
# JAVA
"""
import java.util.*;

public class Main {
    static final int MAX = 105;
    static int[] parent = new int[MAX];
    static int[] ranks = new int[MAX];
    static Set<Integer>[] trees = new TreeSet[MAX];

    private static int findSet(int u) {
        if (u != parent[u]) {
            parent[u] = findSet(parent[u]);
        }
        return parent[u];
    }

    private static void unionSet(int u, int v) {
        int up = findSet(u);
        int vp = findSet(v);

        if (up == vp) {
            return;
        }

        if (ranks[up] > ranks[vp]) {
            parent[vp] = up;
        }
        else if (ranks[up] < ranks[vp]) {
            parent[up] = vp;
        }
        else {
            parent[up] = vp;
            ranks[vp]++;
        }
    }

    public static void main(String[] agrs) {
        Scanner sc = new Scanner(System.in);
        int Q = sc.nextInt();

        for (int i = 0; i < MAX; i++) {
            trees[i] = new TreeSet<>();
        }

        while (Q-- > 0) {
            int P = sc.nextInt();
            int T = sc.nextInt();
            sc.nextLine();

            while (sc.hasNextLine()) {
                String line = sc.nextLine();
                if (line.length() == 0) {
                    break;
                }

                String[] arrOfStr = line.split(" ");
                int person = Integer.parseInt(arrOfStr[0]);
                int tree = Integer.parseInt(arrOfStr[1]);
                trees[person].add(tree);
            }

            for (int i = 1; i <= P; i++) {
                parent[i] = i;
                ranks[i] = 0;
            }

            for (int i = 1; i <= P; i++) {
                for (int j = i + 1; j <= P; j++) {
                    if (trees[i].equals(trees[j])) {
                        unionSet(i, j);
                    }
                }
            }

            int nSets = 0;
            for (int i = 1; i <= P; i++) {
                if (i == parent[i]) {
                    nSets++;
                }
                trees[i].clear();
            }

            System.out.println(nSets);
            if (Q > 0) {
                System.out.println();
            }
        }
    }
}
"""

