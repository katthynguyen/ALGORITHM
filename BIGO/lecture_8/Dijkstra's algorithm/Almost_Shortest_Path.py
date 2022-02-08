# python 3
from heapq import heappush, heappop
INF = 10 ** 9
MAX = 505

def Dijkstra(s, dist, graph):
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

while True:
	N, M = map(int, input().split())
	
	if N == 0 and M == 0:
		break
	
	graph = [[] for _ in range(N)]
	graphS = [[] for _ in range(N)]
	graphD = [[] for _ in range(N)]
	dist = [INF] * N
	distS = [INF] * N
	distD = [INF] * N
		
	S, D = map(int, input().split())
	
	for i in range(M):
		u, v, w = map(int, input().split())
		graphS[u].append((w, v))
		graphD[v].append((w, u))
	
	Dijkstra(S, distS, graphS)
	Dijkstra(D, distD, graphD)
	shortestPath = distS[D]
	
	for u in range(N):
		for w, v in graphS[u]:
			if distS[u] + w + distD[v] != shortestPath:
				graph[u].append((w, v))
	
	Dijkstra(S, dist, graph)
	print(dist[D] if dist[D] != INF else -1)
# C++

"""
#include <bits/stdc++.h>
#define MAX 505
using namespace std;
const int INF = 1e9 + 7;

vector<pair<int, int>> graph[MAX], graphS[MAX], graphD[MAX];
int dist[MAX], distS[MAX], distD[MAX];

void Dijkstra(int s, int dist[], vector<pair<int, int>> (&graph)[MAX]) {
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
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	
	int N, M, S, D, u, v, w;
	
	while (true) {
		cin >> N >> M;
		
		if (N == 0 && M == 0) {
			break;
		}
		
		for (int i = 0; i < N; i++) {
			graph[i].clear();
			graphS[i].clear();
			graphD[i].clear();
			dist[i] = INF;
			distS[i] = INF;
			distD[i] = INF;
		}
		
		cin >> S >> D;
		
		for (int i = 0; i < M; i++) {
			cin >> u >> v >> w;
			graphS[u].push_back(make_pair(w, v));
			graphD[v].push_back(make_pair(w, u));
		}
		
		Dijkstra(S, distS, graphS);
		Dijkstra(D, distD, graphD);
		int shortestPath = distS[D];
		
		for (int u = 0; u < N; u++) {
			for (pair<int, int> &neighbor : graphS[u]) {
				int v = neighbor.second;
				int w = neighbor.first;
				
				if (distS[u] + w + distD[v] != shortestPath) {
					graph[u].push_back(neighbor);
				}
			}
		}
		
		Dijkstra(S, dist, graph);
		cout << (dist[D] != INF ? dist[D] : -1) << endl;
	}
	return 0;
}
"""

# JAVA
"""
import java.util.*;

public class Main {
	static final int MAX = 505;
	static final int INF = (int)1e9 + 7;
	
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
	static ArrayList<Node> graphS[] = new ArrayList[MAX];
	static ArrayList<Node> graphD[] = new ArrayList[MAX];
	static int[] dist = new int[MAX];
	static int[] distS = new int[MAX];
	static int[] distD = new int[MAX];
	
	public static void Dijkstra(int s, int[] dist, ArrayList<Node> graph[]) {
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
	}
	
	public static void main(String[] agrs) {
		Scanner sc = new Scanner(System.in);
		
		while (true) {
			int N = sc.nextInt();
			int M = sc.nextInt();
			
			if (N == 0 && M == 0) {
				break;
			}
			
			for (int i = 0; i < N; i++) {
				graph[i] = new ArrayList<Node>();
				graphS[i] = new ArrayList<Node>();
				graphD[i] = new ArrayList<Node>();
				dist[i] = INF;
				distS[i] = INF;
				distD[i] = INF;
			}
			
			int S = sc.nextInt();
			int D = sc.nextInt();
			
			for (int i = 0; i < M; i++) {
				int u = sc.nextInt();
				int v = sc.nextInt();
				int w = sc.nextInt();
				graphS[u].add(new Node(v, w));
				graphD[v].add(new Node(u, w));
			}
			
			Dijkstra(S, distS, graphS);
			Dijkstra(D, distD, graphD);
			int shortestPath = distS[D];
			
			for (int u = 0; u < N; u++) {
				for (Node neighbor : graphS[u]) {
					int v = neighbor.id;
					int w = neighbor.weight;
					
					if (distS[u] + w + distD[v] != shortestPath) {
						graph[u].add(neighbor);
					}
				}
			}
			
			Dijkstra(S, dist, graph);
			System.out.println(dist[D] != INF ? dist[D] : -1);
		}
	}
}
"""