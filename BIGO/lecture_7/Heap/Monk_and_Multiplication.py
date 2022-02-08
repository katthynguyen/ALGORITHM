# python 3
import queue

n = int(input())
a = list(map(int, input().split()))
pq = queue.PriorityQueue()

for i in range(n):
	pq.put(-a[i])

	if i < 2:
		print(-1)
	else:
		first = -pq.get()
		second = -pq.get()
		third = -pq.get()

		print(first * second * third)

		pq.put(-first)
		pq.put(-second)
		pq.put(-third)

# C++

"""
#include <iostream>
#include <queue>
using namespace std;

int main() {
    int x, n;
    priority_queue<int> pq;
    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> x;
        pq.push(x);

        if (i < 2) {
            cout << -1 << endl;
        }
        else {
            int first = pq.top();
            pq.pop();
            int second = pq.top();
            pq.pop();
            int third = pq.top();
            pq.pop();

            cout << 1LL * first * second * third << endl;

            pq.push(first);
            pq.push(second);
            pq.push(third);
        }
    }
    return 0;
}   
"""

# JAVA
"""
import java.util.Scanner;
import java.util.PriorityQueue;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x, n = sc.nextInt();
        PriorityQueue<Integer> pq = new PriorityQueue<>();

        for (int i = 0; i < n; i++) {
            x = sc.nextInt();
            pq.add(-x);

            if (i < 2) {
                System.out.println(-1);
            }
            else {
                int first = -pq.poll();
                int second = -pq.poll();
                int third = -pq.poll();

                System.out.println(1L * first * second * third);

                pq.add(-first);
                pq.add(-second);
                pq.add(-third);
            }
        }
    }
}
"""