# python 3
import sys
sys.setrecursionlimit(100000)
MAX = 10000

def findSet(u):
    if parent[u] != u:
        parent[u] = findSet(parent[u])
    return parent[u]

def unionSet(u, v):
    up = findSet(u)
    vp = findSet(v)
    parent[vp] = up

n = int(input())
parent = [i for i in range(MAX * 2)]
while True:
    c, x, y = map(int, input().split())
    if c == x == y == 0:
        break
    if c == 1:
        if findSet(x) == findSet(y + MAX):
            print(-1)
            continue
        unionSet(x, y)
        unionSet(x + MAX, y + MAX)
    if c == 2:
        if findSet(x) == findSet(y):
            print(-1)
            continue
        unionSet(x, y + MAX)
        unionSet(x + MAX, y)
    if c == 3:
        if findSet(x) == findSet(y):
            print(1)
        else:
            print(0)
    if c == 4:
        if findSet(x) == findSet(y + MAX):
            print(1)
        else:
            print(0)
# C++
"""
#include <iostream>
#define MAX 10000
using namespace std;
int parent[MAX * 2];

int findSet(int u) {
	while (u != parent[u]) {
		u = parent[u];
	}
	return u;
}

void unionSet(int u, int v) {
	int up = findSet(u);
	int vp = findSet(v);                                                                                                                                                                                       
	parent[vp] = up;
}

int main() {
	int n, c, x, y;
	cin >> n;
	for (int i = 0; i < MAX * 2; i++)
		parent[i] = i;
	while (true) {
		cin >> c >> x >> y;
		if (c == 0 && x == 0 && y == 0) {
			break;
		}
		if (c == 1) {
			if (findSet(x) == findSet(y + MAX)) {
				cout << -1 << endl;
				continue;
			}
			unionSet(x, y);
			unionSet(x + MAX, y + MAX);
		}
		else if (c == 2) {
			if (findSet(x) == findSet(y)) {
				cout << -1 << endl;
				continue;
			}
			unionSet(x, y + MAX);
			unionSet(x + MAX, y);
		}
		else if (c == 3) {
			cout << (findSet(x) == findSet(y)) << endl;
		}
		else if (c == 4) {
			cout << (findSet(x) == findSet(y + MAX)) << endl;
		}
	}
	return 0;
}
"""
# JAVA
"""
import java.util.Scanner;
import java.util.Map;
import java.util.TreeSet;


class DSU{
  int[] parent;
  int n;
  public DSU(int x){
    n = x;
    parent = new int[x];
    for (int i=0;i< n;i++) {
      parent[i]=i;
    }
  }
  public int find(int u){
    if (parent[u]!=u) parent[u]=find(parent[u]);
    return parent[u];
  }
  public void union(int u ,int v){
    int i = find(u);
    int j = find(v);
    if (i!=j) {
      parent[j]=i;
    }
  }
}
class Main {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int MAX = 10000;
    int n,c,x,y;  
    n = sc.nextInt();
    DSU dsu = new DSU(20002);
    while (true) {
      c = sc.nextInt();
      x = sc.nextInt();
      y = sc.nextInt();

      if (c == 0 && x == 0 && y == 0) {
        break;
      }
      if (c == 1) {
        if (dsu.find(x) == dsu.find(y + MAX)) {
          System.out.println(-1);
          continue;
        }
      
      dsu.union(x, y);
      dsu.union(x + MAX, y + MAX);
      }
      else if (c == 2) {
        if (dsu.find(x) == dsu.find(y)) {
          System.out.println(-1);
          continue;
        }
        dsu.union(x, y + MAX);
        dsu.union(x + MAX, y);
      }
      else if (c == 3) {
        if(dsu.find(x) == dsu.find(y)){
          System.out.println(1);
        }
        else
          System.out.println(0);
      }
      else if (c == 4) {
        if(dsu.find(x) == dsu.find(y+MAX)){
          System.out.println(1);
        }
        else
          System.out.println(0);
      }
    }
  }
}
"""

