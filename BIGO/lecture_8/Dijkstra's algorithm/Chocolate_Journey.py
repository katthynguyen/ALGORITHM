# python 3
from heapq import heappush, heappop
INF = 10 ** 9

def Dijkstra(s):
	dist = [INF] * (N + 1)
	pq = [(0, s)]
	dist[s] = 0
	
	while pq:
		w, u = heappop(pq)
		
		if w > dist[u]:
			continue
		
		for weight, v in graph[u]:
			if w + weight < dist[v]:
				dist[v] = w + weight
				heappush(pq, (dist[v], v))
	
	return dist

N, M, k, x = map(int, input().split())
cities = list(map(int, input().split()))
graph = [[] for _ in range(N + 1)]

for _ in range(M):
	u, v, d = map(int, input().split())
	graph[u].append((d, v))
	graph[v].append((d, u))

A, B = map(int, input().split())

distA = Dijkstra(A)
distB = Dijkstra(B)
res = INF

for city in cities:
	if distB[city] <= x:
		res = min(res, distA[city] + distB[city])
	
print(res if res < INF else -1)
# C++

"""
#include <bits/stdc++.h>
#define MAX 100000 + 5
using namespace std;
const int INF = 1e9;

int N, M;
vector<pair<int, int>> graph[MAX];

vector<int> Dijkstra(int s) {
	vector<int> dist(N + 1, INF);
	priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
	pq.push(make_pair(0, s));
	dist[s] = 0;
	
	while (!pq.empty()) {
		pair<int, int> top = pq.top();
		pq.pop();
		
		int u = top.second;
		int w = top.first;
		
		if (w > dist[u]) {
			continue;
		}
		
		for (pair<int, int> &neighbor : graph[u]) {
			if (w + neighbor.first < dist[neighbor.second]) {
				dist[neighbor.second] = w + neighbor.first;
				pq.push(make_pair(dist[neighbor.second], neighbor.second));
			}
		}
	}
	
	return dist;
}
	
int main() {
	int A, B, k, x, u, v, d;
	
	cin >> N >> M >> k >> x;
	vector<int> cities(k);
	
	for (int i = 0; i < k; i++) {
		cin >> cities[i];
	}
	
	for (int i = 0; i < M; i++) {
		cin >> u >> v >> d;
		graph[u].push_back(make_pair(d, v));
		graph[v].push_back(make_pair(d, u));
	}
	
	cin >> A >> B;
	
	vector<int> distA = Dijkstra(A);
	vector<int> distB = Dijkstra(B);
	int res = INF;
	
	for (int &city : cities) {
		if (distB[city] <= x) {
			res = min(res, distA[city] + distB[city]);
		}
	}
	
	cout << (res < INF ? res : -1);
	return 0;
}
"""

# JAVA
"""
import java.util.*;

public class Main {
	static final int MAX = 100000 + 5;
	static final int INF = (int)1e9;
	static int N, M;
	
	static class Node implements Comparable<Node> {
		int id, weight;
		
		public Node(int _id, int _weight) {
			this.id = _id;
			this.weight = _weight;
		}
		
		@Override
		public int compareTo(Node other) {
			return this.weight - other.weight;
		}
	}
	
	static ArrayList<Node> graph[] = new ArrayList[MAX];
	
	public static int[] Dijkstra(int s) {
		int[] dist = new int[N + 1];
		Arrays.fill(dist, INF);
		
		PriorityQueue<Node> pq = new PriorityQueue<>();
		pq.add(new Node(s, 0));
		dist[s] = 0;
		
		while (!pq.isEmpty()) {
			Node top = pq.poll();
			int u = top.id;
			int w = top.weight;
			
			if (w > dist[u]) {
				continue;
			}
			
			for (Node neighbor : graph[u]) {
				if (w + neighbor.weight < dist[neighbor.id]) {
					dist[neighbor.id] = w + neighbor.weight;
					pq.add(new Node(neighbor.id, dist[neighbor.id]));
				}
			}
		}
		
		return dist;
	}

	public static void main(String[] agrs) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		M = sc.nextInt();
		int k = sc.nextInt();
		int x = sc.nextInt();
		ArrayList<Integer> cities = new ArrayList<>();
		
		for (int i = 0; i < k; i++) {
			cities.add(sc.nextInt());
		}
		
		for (int i = 0; i <= N; i++) {
			graph[i] = new ArrayList<Node>();
		}
		
		for (int i = 0; i < M; i++) {
			int u = sc.nextInt();
			int v = sc.nextInt();
			int d = sc.nextInt();
			graph[u].add(new Node(v, d));
			graph[v].add(new Node(u, d));
		}
		
		int A = sc.nextInt();
		int B = sc.nextInt();
		int[] distA = Dijkstra(A);
		int[] distB = Dijkstra(B);
		int res = INF;
		
		for (int city : cities) {
			if (distB[city] <= x) {
				res = Math.min(res, distA[city] + distB[city]);
			}
		}
		
		System.out.print(res < INF ? res : -1);
	}
}
"""