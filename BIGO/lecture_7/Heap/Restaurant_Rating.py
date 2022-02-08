# python 3
import heapq
top3 = []
rest = []
nreviews = 0

n = int(input())

for _ in range(n):
    line = list(map(int, input().split()))
    type = line[0]
    
    if type == 1:
        x = line[1]
        nreviews += 1

        if len(top3) != 0 and top3[0] < x:
            heapq.heappush(rest, -heapq.heappop(top3))
            heapq.heappush(top3, x)
        else:
            heapq.heappush(rest, -x)

        if nreviews % 3 == 0:
            heapq.heappush(top3, -heapq.heappop(rest))
    else:
        if len(top3) == 0:
            print("No reviews yet")
        else:
            print(top3[0])
# C++
"""
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, x, type, nreviews = 0;
    priority_queue<int, vector<int>, greater<int>> top3;
    priority_queue<int> rest;
    cin >> n;

    while (n--) {
        cin >> type;
    
        if (type == 1) {
            cin >> x;
            nreviews++;
    
            if (!top3.empty() && top3.top() < x) {
                rest.push(top3.top());
                top3.pop();
                top3.push(x);
            }
            else {
                rest.push(x);
            }
    
            if (nreviews % 3 == 0) {
                top3.push(rest.top());
                rest.pop();
            }
        }
        else {
            if (top3.empty()) {
                cout << "No reviews yet" << endl;
            }
            else {
                cout << top3.top() << endl;
            }
        }
    }
    return 0;
}

"""

# JAVA

"""
import java.io.*;
import java.util.*;
 
public class Main {
    public static void main(String[] args) {
        MyScanner in = new MyScanner();
        PrintWriter out = new PrintWriter(System.out);
        PriorityQueue<Integer> top3 = new PriorityQueue<>();
        PriorityQueue<Integer> rest = new PriorityQueue<>();
        int n = in.nextInt();
        int nreviews = 0;
     
        while (n-- > 0) {
            int type = in.nextInt();
            
            if (type == 1) {
                int x = in.nextInt();
                nreviews++;
                
                if (!top3.isEmpty() && top3.peek() < x) {
                    rest.add(-top3.poll()); 
                    top3.add(x);
                }
                else {
                    rest.add(-x); 
                }

                if (nreviews % 3 == 0) {
                    top3.add(-rest.poll()); 
                }
            }
            else {
                if (top3.isEmpty()) {
                    out.println("No reviews yet");
                }
                else {
                    out.println(top3.peek());
                }
            }
        }
        out.close();
    }
    
    public static class MyScanner {
        BufferedReader br;
        StringTokenizer st = null;
        public MyScanner() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }
 
        public MyScanner(InputStream stream) {
            br = new BufferedReader(new InputStreamReader(stream));
        }
 
        boolean hasNext() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    String tmp = br.readLine();
                    if (tmp == null)
                        return false;
                    st = new StringTokenizer(tmp);
                } catch (IOException e) {
                    return false;
                }
            }
            return true;
        }
        String next() {
            if (hasNext())
                return st.nextToken();
            return null;
        }
        int nextInt() {
            return Integer.parseInt(next());
        }
        long nextLong() {
            return Long.parseLong(next());
        }
        double nextDouble() {
            return Double.parseDouble(next());
        }
        String nextLine() {
            String str = "";
            try {
                str = br.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }
    }
}
"""