#  python3
import queue
n, b = map(int, input().split())
q = queue.Queue()
processing = 0
 
for _ in range(n):
    t, d = map(int, input().split())
 
    while q.qsize() != 0 and t >= q.queue[0]:
        q.get()
 
    if q.qsize() <= b:
        processing = max(t, processing) + d
        q.put(processing)
        print(processing, end=' ')
    else:
        print(-1, end=' ')
#  C++

"""
#include <iostream>
#include <queue>
using namespace std;
 
int main() {
    int n, b;
    long long t, d, processing = 0;
    queue<long long> q;
     
    cin >> n >> b;
 
    for (int i = 0; i < n; i++) {
        cin >> t >> d;
 
        while (!q.empty() && q.front() <= t) {
            q.pop();
        }
 
        if (q.size() <= b) {
            processing = max(processing, t) + d;
            cout << processing << " ";
            q.push(processing);
        }
        else {
            cout << -1 << " ";
        }
    }
    return 0;
}
"""

#  JAVA
"""
import java.util.Scanner;
import java.util.LinkedList;
import java.util.Queue;
 
public class Main {
    public static void main(String[] agrs) {
        Scanner sc = new Scanner(System.in);
        int t, d;
        int n = sc.nextInt(), b = sc.nextInt();
        Queue<Long> q = new LinkedList<>();
        long processing = 0;
 
        for (int i = 0; i < n; i++) {
            t = sc.nextInt();
            d = sc.nextInt();
 
            while (!q.isEmpty() && q.peek() <= t) {
                q.remove();
            }
 
            if (q.size() <= b) {
                processing = Math.max(processing, t) + d;
                System.out.format("%d ", processing);
                q.add(processing);
            }
            else {
                System.out.print("-1 ");
            }
        }
    }
}
"""