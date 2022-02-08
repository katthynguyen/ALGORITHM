# python 3
import queue
def solve():
    n = int(input())
    jobs = []
    for i in range(n):
        a, b, d = map(int, input().split())
        jobs.append((d, a, b))
    
    jobs.sort()
    pq = queue.PriorityQueue()
    time = 0
    money = 0
    for d, a, b in jobs:
        time += b
        pq.put((-a, b, d))
        while time > d:
            ta, tb, td = pq.get()
            if tb > time - d:
                tb -= time - d
                money += (time - d) / -ta
                time = d
                pq.put((ta, tb, td))
            else:
                time -= tb
                money += tb / -ta

    print('{:.2f}'.format(money))

T = int(input())
for t in range(T):
    solve()
# C++
"""
#include <bits/stdc++.h>
#define MAX 100005
using namespace std;
 
struct Job {
    int a, b, d;
    bool operator<(const Job &other) const {
        return a < other.a;
    }
};
 
bool wayToSort(const Job &x, const Job &y) {
    return x.d < y.d;
}
 
int main() {
    int t, N;
    cin >> t;
 
    while (t--) {
        cin >> N;
        Job job[MAX];
        priority_queue<Job> pq;
 
        for (int i = 0; i < N; i++) {
            cin >> job[i].a >> job[i].b >> job[i].d;
        }
 
        sort(job, job + N, wayToSort);
        double money = 0;
        int time = 0;
 
        for (int i = 0; i < N; i++) {
            time += job[i].b;
            pq.push(job[i]);
             
            while (time > job[i].d) {
                Job top = pq.top();
                pq.pop();
 
                if (top.b > time - job[i].d) {
                    money += (time - job[i].d) * 1.0 / top.a;
                    top.b -= time - job[i].d;
                    pq.push(top);
                    time = job[i].d;
                }
                else {
                    money += top.b * 1.0 / top.a;
                    time -= top.b;
                    top.b = 0;
                }
            }
        }
 
        cout << fixed << setprecision(2) << money << endl;
         
        while (!pq.empty()) {
            pq.pop();
        }
    }
    return 0;
}
"""
# JAVA
"""
import java.util.*;
import java.io.*;
class Job implements Comparable<Job>{
     
    public int a,b,d;
    public int compareTo(Job j){
        return this.d - j.d;
    }
    Job(){
        a = b = d = 0;
    }
}
class InputReader {
    public BufferedReader reader;
    public StringTokenizer tokenizer;
  
    public InputReader(InputStream stream) {
        reader = new BufferedReader(new InputStreamReader(stream));
        tokenizer = null;
    }
  
    public String next() {
        while (tokenizer == null || !tokenizer.hasMoreTokens()) {
            try {
                tokenizer = new StringTokenizer(reader.readLine());
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        }
        return tokenizer.nextToken();
    }
  
    public int nextInt() {
        return Integer.parseInt(next());
    }
  
    public double nextDouble() {
        return Double.parseDouble(next());
    }
}
class Main {
    static final int MAX = 100005;
    public static void main(String[] args) {
        InputReader sc = new InputReader(System.in);
         
        int t,N;
        t = sc.nextInt();
         
        for(int k = 0 ; k < t; k++)
        {
            PriorityQueue<Job> pq = new PriorityQueue<>(new Comparator<Job>() {
 
                @Override
                public int compare(Job o1, Job o2) {
                    return o2.a - o1.a;
                }
            });
            N = sc.nextInt();
            Job J[] = new Job[MAX];
            for(int i =0; i  < N; i++){
                J[i] = new Job();
                J[i].a = sc.nextInt();
                J[i].b = sc.nextInt();
                J[i].d = sc.nextInt();
            }
            Arrays.sort(J,0,N);
            double sum_min = 0;
            int time = 0 ;
            for(int i = 0; i < N;i++){
                time += J[i].b;
                pq.add(J[i]);
                while (time > J[i].d)
                {
                    Job top = pq.poll();
                    if (top.b > time - J[i].d)
                    {
                        sum_min += (time - J[i].d) * 1.0 / top.a;
                        top.b -= time - J[i].d;
                        pq.add(top);
                        time = J[i].d;
                    }
                    else
                    {
                        sum_min += top.b * 1.0 / top.a;
                        time -= top.b;
                        top.b = 0;
                    }
                }
            }
            System.out.printf("%.2f\n", sum_min);
        }
    }
}
"""