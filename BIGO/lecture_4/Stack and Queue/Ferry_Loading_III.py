# python3
import queue
 
class Car:
    def __init__(self, _id, _arriveTime):
        self.id = _id
        self.arriveTime = _arriveTime
 
Q = int(input())
 
for _ in range(Q):
    qSide = [[] , []]
    qSide[0] = queue.Queue()
    qSide[1] = queue.Queue()
    res = [0] * 10005
     
    n, t, m = map(int, input().split())
     
    for i in range(m):
        arrived, atBank = input().split()
         
        if atBank == "left":
            qSide[0].put(Car(i, int(arrived)))
        else:
            qSide[1].put(Car(i, int(arrived)))
     
    curTime, curSide = 0, 0
    waiting = (not qSide[0].empty()) + (not qSide[1].empty())
     
    while waiting:
        if waiting == 1:
            nextTime = qSide[1].queue[0].arriveTime if qSide[0].empty() else qSide[0].queue[0].arriveTime
        else:
            nextTime = min(qSide[0].queue[0].arriveTime, qSide[1].queue[0].arriveTime)
         
        curTime = max(curTime, nextTime)
        carried = 0
         
        while not qSide[curSide].empty():
            car = qSide[curSide].queue[0]
            if car.arriveTime <= curTime and carried < n:
                res[car.id] = curTime + t
                carried += 1
                qSide[curSide].get()
            else:
                break
         
        curTime += t
        curSide = 1 - curSide
        waiting = (not qSide[0].empty()) + (not qSide[1].empty())
     
    for i in range(m):
        print(res[i])
     
    if _ < Q - 1:
        print()
# C++
"""
#include <iostream>
#include <queue>
#define MAX 10000 + 5
using namespace std;
 
struct Car {
    int id, arriveTime;
};
 
int main() {
    int n, t, m, Q;
    int res[MAX];
    cin >> Q;
     
    while (Q--) {
        queue<Car> qSide[2];
        int arrived;
        string atBank;
         
        cin >> n >> t >> m;
         
        for (int i = 1; i <= m; i++) {
            cin >> arrived >> atBank;
             
            if (atBank == "left") {
                qSide[0].push((Car) {i, arrived});
            }
            else {
                qSide[1].push((Car) {i, arrived});
            }
        }
         
        int curSide = 0, curTime = 0, nextTime;
        int waiting = !qSide[0].empty() + !qSide[1].empty();
         
        while (waiting) {
            if (waiting == 1) {
                nextTime = (qSide[0].empty() ? qSide[1].front().arriveTime : qSide[0].front().arriveTime);
            }
            else {
                nextTime = min(qSide[0].front().arriveTime, qSide[1].front().arriveTime);
            }
             
            curTime = max(curTime, nextTime);
            int carried = 0;
             
            while (!qSide[curSide].empty()) {
                Car car = qSide[curSide].front();
                if (car.arriveTime <= curTime && carried < n) {
                    res[car.id] = curTime + t;
                    carried++;
                    qSide[curSide].pop();
                }
                else {
                    break;
                }
            }
             
            curTime += t;
            curSide = 1 - curSide;
            waiting = !qSide[0].empty() + !qSide[1].empty();
        }
         
        for (int i = 1; i <= m; i++) {
            cout << res[i] << endl;
        }
         
        if (Q) {
            cout << endl;
        }
    }
    return 0;
}
"""
# JAVA
"""
 import java.util.Scanner;
import java.util.LinkedList;
import java.util.Queue;
 
public class Main {
    static final int MAX = 10000 + 5;
    static class Car {
        int id, arriveTime;
         
        public Car(int _id, int _arriveTime) {
            this.id = _id;
            this.arriveTime = _arriveTime;
        }
    }
     
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int Q = sc.nextInt();
        int res[] = new int[MAX];
         
        while (Q-- > 0) {
            Queue<Car> qSide[] = new Queue[2];
            qSide[0] = new LinkedList<>();
            qSide[1] = new LinkedList<>();
             
            int n = sc.nextInt();
            int t = sc.nextInt();
            int m = sc.nextInt();
             
            for (int i = 1; i <= m; i++) {
                int arrived = sc.nextInt();
                String atBank = sc.next();
                 
                if (atBank.equals("left")) {
                    qSide[0].add(new Car(i, arrived));
                }
                else {
                    qSide[1].add(new Car(i, arrived));
                }
            }
             
            int curSide = 0, curTime = 0, nextTime;
            int waiting = (!qSide[0].isEmpty() ? 1 : 0) + (!qSide[1].isEmpty() ? 1 : 0);
             
            while (waiting > 0) {
                if (waiting == 1) {
                    nextTime = (qSide[0].isEmpty() ? qSide[1].peek().arriveTime : qSide[0].peek().arriveTime);
                }
                else {
                    nextTime = Math.min(qSide[0].peek().arriveTime, qSide[1].peek().arriveTime);
                }
                 
                curTime = Math.max(curTime, nextTime);
                int carried = 0;
                 
                while (!qSide[curSide].isEmpty()) {
                    Car car = qSide[curSide].peek();
                    if (car.arriveTime <= curTime && carried < n) {
                        res[car.id] = curTime + t;
                        carried++;
                        qSide[curSide].remove();
                    }
                    else {
                        break;
                    }
                }
                 
                curTime += t;
                curSide = 1 - curSide;
                waiting = (!qSide[0].isEmpty() ? 1 : 0) + (!qSide[1].isEmpty() ? 1 : 0);
            }
             
            for (int i = 1; i <= m; i++) {
                System.out.println(res[i]);
            }
                 
            if (Q > 0) {
                System.out.println();
            }
        }
    }
}
""" 