# python 3
import queue
import math

class Scanner:
    def __generator__():
        while True:
            try:
                buff = input().strip().split()
                for x in buff:
                    yield x
            except EOFError:
                exit()
                
    sc = __generator__()
    def next():
        return Scanner.sc.__next__()

class node:
    dist = 0
    index = 0

    def __init__(self, dist, index):
        self.dist = dist
        self.index = index

    def __lt__(self, other):
        return self.dist < other.dist

def prim(graph, src):
    # graph = matrix [n][n]
    n = len(graph)
    dist = [1e9] * n
    visited = [0] * n
    total_cost = 0
    dist[src] = 0
    Q = queue.PriorityQueue()
    Q.put(node(0, src))

    while not Q.empty():
        temp = Q.get()
        u = temp.index
        visited[u] = True
        for v in range(n):
            if not visited[v] and dist[v] > graph[u][v]:
                dist[v] = graph[u][v]
                Q.put(node(dist[v], v))

    for i in range(n):
        total_cost += dist[i]
    return total_cost

def distance(x1, y1, x2, y2):
    square_dis = (x1-x2)**2 + (y1-y2)**2
    return math.sqrt(square_dis)

def solve():
    while True:
        n = int(Scanner.next())
        x = [0] * n
        y = [0] * n
        for i in range(n):
            x[i], y[i] = int(Scanner.next()), int(Scanner.next())
        graph = []
        for i in range(n):
            graph.append([])
            for j in range(n):
                graph[i].append(distance(x[i], y[i], x[j], y[j]))
        m = int(Scanner.next())
        for i in range(m):
            u, v = int(Scanner.next()), int(Scanner.next())
            u-=1
            v-=1
            graph[u][v] = 0
            graph[v][u] = 0
        print("%.2f" % prim(graph, 0))

solve()
# C++
"""
#include <cmath>
#include <stdio.h>
#include <cstdio>
#include <vector>
#include <iostream>
#include <iomanip>
#include <queue>
#include <string>
#include <functional>
using namespace std;
#define MAX 751

const int INF = 1e9;
vector<pair<int, double> > graph[MAX];
vector<double> dist(MAX, INF);
vector<int> path(MAX, -1);
bool visited[MAX];
int N, M;
int x[MAX], y[MAX];

int distance(int i, int j)
{
	return (x[i] - x[j])*(x[i] - x[j]) + (y[i] - y[j])*(y[i] - y[j]);
}

double result() 
{
	double ans = 0;
	for (int i = 0; i<N; i++) 
	{
		ans += sqrt(dist[i]);
		if (ans >= INF) 
		{
			return -1;
		}
	}
	return ans;
}

void prims(int src) 
{
	priority_queue<pair<int, int>, vector<pair<int, int> >, greater<pair<int, int> > > pq;
	pq.push(make_pair(0, src));
	dist[src] = 0;
	while (!pq.empty()) 
	{
		int u = pq.top().second;
		pq.pop();
		visited[u] = true;
		for (int i = 0; i<graph[u].size(); i++) 
		{
			int v = graph[u][i].first;
			int w = graph[u][i].second;
			if (!visited[v] && dist[v] > w) 
			{
				dist[v] = w;
				pq.push(make_pair(w, v));
				path[v] = u;
			}
		}
	}
}

void ResetGraph()
{
	for (int i = 0; i < N; i++)
	{
		graph[i].clear();
		visited[i] = false;
		dist[i] = INF;
		path[i] = -1;
	}
}

int main() 
{
	freopen("INPUT.INP", "rt", stdin);
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	while (cin >> N) 
	{
		for (int i = 0; i<N; i++)
		{
			int a, b;
			cin >> a >> b;
			x[i] = a;
			y[i] = b;
		}
		cin >> M;
		vector<vector<bool> > edges(MAX, vector<bool>(MAX, false));
		for (int i = 0; i<M; i++)
		{
			int a, b;
			cin >> a >> b;
			edges[a - 1][b - 1] = true;
			edges[b - 1][a - 1] = true;
		}
		for (int i = 0; i<N - 1; i++) 
		{
			for (int j = i + 1; j<N; j++)
			{
				if (edges[i][j] == false)
				{
					int w = distance(i, j);
					graph[i].push_back(make_pair(j, w));
					graph[j].push_back(make_pair(i, w));
				}
				else 
				{
					graph[i].push_back(make_pair(j, 0));
					graph[j].push_back(make_pair(i, 0));
				}
			}
		}
		prims(0);
		double r = result();
		printf("%0.2f\n", r);
		ResetGraph();
	}
	return 0;
}
"""
# JAVA
"""
import java.util.PriorityQueue;
import java.util.Scanner;
import java.util.ArrayList;
 
class Node implements Comparable<Node> {
	public Integer id;
	public Integer dist;
	public Node(Integer id, Integer dist) {
	this.id = id;
	this.dist = dist;
	}
	public int compareTo(Node other) {
	return this.dist.compareTo(other.dist);
	}
}
public class Main {
	
	static Scanner sc = new Scanner(System.in);
	static final int MAX = 800;
	static final  int INF = (int) 1e9;
	static ArrayList<ArrayList< Node >> graph = new ArrayList<ArrayList< Node> >();
	static int dist[]= new int[MAX];
	static int path[] = new int[MAX];
	static Boolean visited[] = new Boolean[MAX];
	static int N, M;
	static int x[] = new int[MAX], y[] = new int[MAX];

	static int distance(int i, int j)
	{
		return (x[i] - x[j])*(x[i] - x[j]) + (y[i] - y[j])*(y[i] - y[j]);
	}

	static double result() 
	{
		double ans = 0;
		for (int i = 0; i<N; i++) 
		{
			ans += Math.sqrt(dist[i]);
			if (ans >= INF) 
			{
				return -1;
			}
		}
		return ans;
	}

	static void prims(int src) 
	{
		PriorityQueue<Node > pq = new PriorityQueue<Node>();
		pq.add(new Node(src,0));
		dist[src] = 0;
		while (!pq.isEmpty()) 
		{
			int u = (int) pq.peek().id;
			pq.poll();
			visited[u] = true;
			for (int i = 0; i<graph.get(u).size(); i++) 
			{
				int v = graph.get(u).get(i).id;
				int w = (int) graph.get(u).get(i).dist;
				if (!visited[v] && dist[v] > w) 
				{
					dist[v] = w;
					pq.add(new Node(v, w));
					path[v] = u;
				}
			}
		}
	}

	static void ResetGraph()
	{
		for (int i = 0; i < N; i++)
		{
			graph.get(i).clear();
			visited[i] = false;
			dist[i] = INF;
			path[i] = -1;
		}
	}

	public static void main(String[] args) 
	{
		for (int i=0;i<MAX;i++) graph.add(new ArrayList<Node>());
		N=MAX-1;
		ResetGraph();
		while (sc.hasNext()) 
		{
			N=sc.nextInt();
			for (int i = 0; i<N; i++)
			{
				int a, b;
				a = sc.nextInt();
				b = sc.nextInt();
				x[i] = a;
				y[i] = b;
			}
			M = sc.nextInt();
			boolean edges[][] = new boolean[MAX][MAX];
			for (int i=0;i<N;i++)
				for (int j=0;j<N;j++) edges[i][j]=false;
			
			for (int i = 0; i<M; i++)
			{
				int a, b;
				a= sc.nextInt();
				b= sc.nextInt();
				edges[a - 1][b - 1] = true;
				edges[b - 1][a - 1] = true;
			}
			for (int i = 0; i< N - 1; i++) 
			{
				for (int j = i + 1; j<N; j++)
				{
					if (edges[i][j] == false)
					{
						int w = distance(i, j);
						graph.get(i).add(new Node(j, w));
						graph.get(j).add(new Node(i, w));
					}
					else 
					{
						graph.get(i).add(new Node(j, 0));
						graph.get(j).add(new Node(i, 0));
					}
				}
			}
			prims(0);
			double r = result();
			System.out.printf("%.2f%n", r);
			ResetGraph();
		}
	}
}
"""

