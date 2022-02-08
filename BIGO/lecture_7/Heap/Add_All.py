# python 3

import queue
pq = queue.PriorityQueue()

while True:
    n = int(input())
    
    if n == 0:
        break

    for x in input().split():
        pq.put(int(x))
    
    ans = 0
    
    while pq.qsize() > 1:
        a = pq.get()
        b = pq.get()
        ans += a + b
        pq.put(a + b)

    print(ans)
    pq.get()

    #  c++

"""
#include <iostream>
#include <queue>
using namespace std;

int main() {
    priority_queue<int, vector<int>, greater<int>> pq;
    int n, x;
    
    while (true) {
        cin >> n;

        if (n == 0) {
            break;
        }

        for (int i = 0; i < n; i++) {
            cin >> x;
            pq.push(x);
        }

        long long ans = 0;

        while (pq.size() > 1) {
            int a = pq.top();
            pq.pop();
            int b = pq.top();
            pq.pop();
            ans += a + b;
            pq.push(a + b);
        }

        cout << ans << endl;
        pq.pop();
    }
    return 0;
}
"""


#  JAVA

"""
import java.util.Scanner;
import java.util.PriorityQueue;

public class Solution {
    public static void main(String[] agrs) {
        Scanner sc = new Scanner(System.in);
        PriorityQueue<Integer> pq = new PriorityQueue<>();

        while (true) {
            int n = sc.nextInt();

            if (n == 0) {
                break;
            }

            for (int i = 0; i < n; i++) {
                int x = sc.nextInt();
                pq.add(x);
            }

            long ans = 0;

            while (pq.size() > 1) {
                int a = pq.poll();
                int b = pq.poll();
                ans += a + b;
                pq.add(a + b);
            }

            System.out.println(ans);
            pq.remove();
        }
    }
}
"""