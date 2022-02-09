# python 3

def BinarySearch(a, left, right, x):
    while left <= right:
        mid = (left + right) // 2
    
        if a[mid] == x:
            return True
        elif a[mid] > x:
            right = mid - 1
        else:
            left = mid + 1
                
    return False

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    cnt = 0
    
    for i in range(n):
        comp = m - a[i]
        if BinarySearch(a, i + 1, n - 1, comp):
            cnt += 1

    print(cnt)

# C++
"""
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool binarySearch(vector<int> &a, int left, int right, int x) {
    while (left <= right) {
        int mid = (left + right) / 2;

        if (a[mid] == x) {
            return true;
        }
        else if (a[mid] > x) {
            right = mid - 1;
        }
        else {
            left = mid + 1;
        }
    }

    return false;
}

int main() {
    int t, n, m, cnt, comp;
    vector<int> a;
    cin >> t;

    for (int k = 0; k < t; k++) {
        cin >> n >> m;
        a.resize(n);

        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }

        sort(a.begin(), a.end());
        cnt = 0;

        for (int i = 0; i < n; i++) {
            comp = m - a[i];
            if (binarySearch(a, i + 1, n - 1, comp)) {
                cnt++;
            }
        }

        cout << cnt << endl;
	}
    return 0;
}
"""

# JAVA
"""
import java.io.*;
import java.util.*;
 
public class Solution {
    public static boolean BinarySearch(int a[], int left, int right, int x) {
        while (left <= right) {
            int mid = (left + right) / 2;
 
            if (a[mid] == x) {
                return true;
            }
            else if (a[mid] > x) {
                right = mid - 1;
            }
            else {
                left = mid + 1;
            }
        }

        return false;
    }
  
    public static void main(String[] args) throws IOException {
        Reader in = new Reader();
        PrintWriter out = new PrintWriter(System.out);
        int n, m, comp, cnt;
        int t = in.nextInt();

        for (int k = 0; k < t; k++) {
            n = in.nextInt();
            m = in.nextInt();
            int a[] = new int[n];

            for (int i = 0; i < n; i++) {
                a[i] = in.nextInt();
            }

            Arrays.sort(a);
            cnt = 0;

            for (int i = 0; i < n; i++) {
                comp = m - a[i];
                if (BinarySearch(a, i + 1, n - 1, comp)) {
                    cnt++;
                }
            }

            out.println(cnt);
        }
        out.close();
        return;
    }
}

class Reader {
    final private int BUFFER_SIZE = 1 << 16;
    private DataInputStream din;
    private byte[] buffer;
    private int bufferPointer, bytesRead;
 
    public Reader() {
        din = new DataInputStream(System.in);
        buffer = new byte[BUFFER_SIZE];
        bufferPointer = bytesRead = 0;
    }
 
    public Reader(String file_name) throws IOException {
        din = new DataInputStream(new FileInputStream(file_name));
        buffer = new byte[BUFFER_SIZE];
        bufferPointer = bytesRead = 0;
    }
 
    public String readLine() throws IOException {
        byte[] buf = new byte[64]; // line length
        int cnt = 0, c;
        while ((c = read()) != -1) {
            if (c == '\n') break;
            buf[cnt++] = (byte) c;
        }
        return new String(buf, 0, cnt);
    }
 
    public int nextInt() throws IOException {
        int number = 0;
        byte c = read();
        while (c <= ' ') c = read();
        boolean IsNegative = (c == '-');
        if (IsNegative) c = read();

        do {
            number = number * 10 + (c - '0');
        }
        while ((c = read()) >= '0' && c <= '9');

        return IsNegative ? -number : number;
    }
 
    public long nextLong() throws IOException {
        long number = 0;
        byte c = read();
        while (c <= ' ') c = read();
        boolean IsNegative = (c == '-');
        if (IsNegative) c = read();
        
        do {
            number = number * 10 + (c - '0');
        }
        while ((c = read()) >= '0' && c <= '9');

        return IsNegative ? -number : number;
    }
 
    public double nextDouble() throws IOException {
        double number = 0, div = 1;
        byte c = read();
        while (c <= ' ') c = read();
        boolean IsNegative = (c == '-');
        if (IsNegative) c = read();
 
        do {
            number = number * 10 + (c - '0');
        }
        while ((c = read()) >= '0' && c <= '9');
 
        if (c == '.') {
            while ((c = read()) >= '0' && c <= '9') {
                number += (c - '0') / (div *= 10);
            }
        }

        return IsNegative ? -number : number;
    }
 
    private void fillBuffer() throws IOException {
        bytesRead = din.read(buffer, bufferPointer = 0, BUFFER_SIZE);
        if (bytesRead == -1) buffer[0] = -1;
    }
 
    private byte read() throws IOException {
        if (bufferPointer == bytesRead) fillBuffer();
        return buffer[bufferPointer++];
    }
 
    public void close() throws IOException {
        if (din == null)
            return;
        din.close();
    }
}
"""