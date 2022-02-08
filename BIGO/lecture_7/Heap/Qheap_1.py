# python 3
import queue

q = int(input())
pq = queue.PriorityQueue()
pqRemove = queue.PriorityQueue()

for i in range(q):
    line = input()

    if line[0] == '1':
        value = int(line.split()[1])
        pq.put(value)
    elif line[0] == '2':
        value = int(line.split()[1])
        pqRemove.put(value)
    else:
        while not pqRemove.empty() and pq.queue[0] == pqRemove.queue[0]:
            pq.get()
            pqRemove.get()

        print(pq.queue[0])
# C++
"""
#include <iostream>
#include <queue>
#include <functional>
using namespace std;

int main() {
    priority_queue<int, vector<int>, greater<int>> pq, pqRemove;
    int Q;
    cin >> Q;

    int type, value;

    for (int k = 0; k < Q; k++) {
        cin >> type;

        if (type == 1) {
            cin >> value;
            pq.push(value);
        }
        else if (type == 2) {
            cin >> value;
            pqRemove.push(value);
        }
        else {
            while (!pqRemove.empty() && pq.top() == pqRemove.top()) {
                pq.pop();
                pqRemove.pop();
            }

            cout << pq.top() << endl;
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
        int Q = sc.nextInt();
        PriorityQueue<Integer> pq = new PriorityQueue<>(), pqRemove = new PriorityQueue<>();

        int type, value;

        for (int k = 0; k < Q; k++) {
            type = sc.nextInt();

            if (type == 1) {
                value = sc.nextInt();
                pq.add(value);
            }
            else if (type == 2) {
                value = sc.nextInt();
                pqRemove.add(value);
            }
            else {
                while (!pqRemove.isEmpty() && (int)pq.peek() == (int)pqRemove.peek()) {
                    pq.remove();
                    pqRemove.remove();
                }

                System.out.println(pq.peek());
            }
        }
    }
}
"""