# python3
from collections import deque
tc = 1
 
while True:
    P, C = map(int, input().split())
    if P == 0 and C == 0:
        break
     
    q = deque()
    for i in range(1, min(P, C) + 1):
        q.append(i)
     
    print('Case {}:'.format(tc))
    tc += 1
 
    for _ in range(C):
        line = input().split()
        cmd = line[0]
 
        if cmd == 'N':
            print(q[0])
            q.append(q.popleft())
        else:
            x = int(line[1])
            n = len(q)
            q.append(x)
            for i in range(n):
                temp = q.popleft()
                if temp != x:
                    q.append(temp)
#  C++

"""
#include <iostream>
#include <queue>
#include <math.h>
using namespace std;
 
int main() {
    int P, C, x, temp, tc = 1;
    char cmd;
    queue<int> q;
 
    while (true) {
        cin >> P >> C;
        if (P == 0 && C == 0) {
            break;
        }
 
        for (int i = 1; i <= min(P, C); i++) {
            q.push(i);
        }
 
        cout << "Case " << tc++ << ":" << endl;
 
        for (int i = 0; i < C; i++) {
            cin >> cmd;
 
            if (cmd == 'N') {
                temp = q.front();
                cout << temp << endl;
                q.pop();
                q.push(temp);
            }
            else {
                cin >> x;
                int n = q.size();
                q.push(x);
                 
                for (int j = 0; j < n; j++) {
                    temp = q.front();
                    q.pop();
                    if (temp != x) {
                        q.push(temp);
                    }
                }
            }
        }
 
        while (!q.empty()) {
            q.pop();
        }
    }
    return 0;
}
"""
#  JAVA
"""
import java.util.Scanner;
import java.util.Queue;
import java.util.LinkedList;
 
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int P, C, n, x, temp, tc = 1;
        char cmd;
        Queue<Integer> q = new LinkedList<Integer>();
 
        while (true) {
            P = sc.nextInt();
            C = sc.nextInt(); 
             
            if (P == 0 && C == 0) {
                break;
            }
 
            for (int i = 1; i <= Math.min(P, C); i++) {
                q.add(i);
            }
 
            System.out.format("Case %d:\n", tc++);
             
            for (int i = 0; i < C; i++) {
                cmd = sc.next().charAt(0);
                 
                if (cmd == 'N') {
                    System.out.println(q.peek());
                    q.add(q.poll());
                }
                else {
                    x = sc.nextInt();
                    n = q.size();
                    q.add(x);
 
                    for (int j = 0; j < n; j++) {
                        temp = q.poll();
                        if (temp != x) {
                            q.add(temp);
                        }
                    }
                }
            }
 
            while (!q.isEmpty()) {
                q.remove();
            }
        }
    }
}
"""