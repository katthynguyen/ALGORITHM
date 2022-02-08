# python 3

import queue
s = []
q = queue.Queue()
pq = queue.PriorityQueue()
 
while True:
    try:
        n = int(input())
    except EOFError:
        break
 
    s.clear()
    q.queue.clear()
    pq.queue.clear()    
    isStack = isQueue = isPQ = True
     
    for _ in range(n):
        type, x = map(int, input().split())
        if type == 1:
            s.append(x)
            q.put(x)
            pq.put(-x)
        else:
            if len(s) == 0:
                isStack = isQueue = isPQ = False
            else:
                if x != s.pop():
                    isStack = False
                if x != q.get():
                    isQueue = False
                if x != -pq.get():
                    isPQ = False
 
    if isStack + isQueue + isPQ == 0:
        print("impossible")
    elif isStack + isQueue + isPQ > 1:
        print("not sure")
    elif isStack:
        print("stack")
    elif isQueue:
        print("queue")
    else:
        print("priority queue")
# C++

"""
#include <bits/stdc++.h>
using namespace std;
 
int main() {
    int n, type, x;
    stack<int> s;
    queue<int> q;
    priority_queue<int> pq;
    bool isStack, isQueue, isPQ;
 
    while (cin >> n) {
        while (!s.empty()) s.pop();
        while (!q.empty()) q.pop();
        while (!pq.empty()) pq.pop();
        isStack = isQueue = isPQ = true;
 
        for (int i = 0; i < n; i++) {
            cin >> type >> x;
 
            if (type == 1) {
                s.push(x);
                q.push(x);
                pq.push(x);
            }
            else {
                if (s.empty()) {
                    isStack = isQueue = isPQ = false;
                    continue;
                }
                 
                if (s.top() != x) {
                    isStack = false;
                }
                if (q.front() != x) {
                    isQueue = false;
                }
                if (pq.top() != x) {
                    isPQ = false;
                }
 
                s.pop(); q.pop(); pq.pop();
            }
        }
         
        if (isStack + isQueue + isPQ == 0) {
            cout << "impossible" << endl;
        }
        else if (isStack + isQueue + isPQ > 1) {
            cout << "not sure" << endl;
        }
        else if (isStack) {
            cout << "stack" << endl;
        }
        else if (isQueue) {
            cout << "queue" << endl;
        }
        else {
            cout << "priority queue" << endl;
        }
    }
    return 0;
}
"""

# JAVA

"""
import java.util.*;
 
public class Main {
    static int isStack, isQueue, isPQ;
    static Stack<Integer> s = new Stack<>();
    static Queue<Integer> q = new LinkedList<>();
    static PriorityQueue<Integer> pq = new PriorityQueue<>();
    public static void main(String[] agrs) {
        Scanner sc = new Scanner(System.in);
 
        while (sc.hasNext()) {
            int n = sc.nextInt();
            s.clear();
            q.clear();
            pq.clear();
            isStack = isQueue = isPQ = 1;
 
            for (int i = 0; i < n; i++) {
                int type = sc.nextInt();
                int x = sc.nextInt();
 
                if (type == 1) {
                    s.add(x);
                    q.add(x);
                    pq.add(-x);
                }
                else {
                    if (s.empty()) {
                        isStack = isQueue = isPQ = 0;
                        continue;
                    }
 
                    if (s.pop() != x) {
                        isStack = 0;
                    }
                    if (q.poll() != x) {
                        isQueue = 0;
                    }
                    if (pq.poll() != -x) {
                        isPQ = 0;
                    }
                }
            }
 
            if (isStack + isQueue + isPQ == 0) {
                System.out.println("impossible");
            }
            else if (isStack + isQueue + isPQ > 1) {
                System.out.println("not sure");
            }
            else if (isStack == 1) {
                System.out.println("stack");
            }
            else if (isQueue == 1) {
                System.out.println("queue");
            }
            else {
                System.out.println("priority queue");
            }
        }
    }
}
"""