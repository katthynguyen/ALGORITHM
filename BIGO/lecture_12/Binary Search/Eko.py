# python 3
import sys

def inp():
    return map(int, input().split(' '))

def check(a, x):
    sum = 0
    for item in a:
        sum += max(0, item - x)
    return sum

def BS_search(a, l, r, k):
    ans = r
    while l <= r:
        mid = int( (l + r) / 2 )
        if check(a, mid) >= k:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
    return ans

def solve():
    n, k = inp()
    a = list(inp())
    vmin = 0
    vmax = 1e9
    print (BS_search(a, vmin, vmax, k))

solve()
# C++

"""
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<int> trees(n);

    for (int i = 0; i < n; i++) {
        cin >> trees[i];
    }

    int hmin = 0, hmax = 1e9 + 7;
    long long sum;
    int res = 0;

    while (hmin <= hmax) {
        int hmid = (hmin + hmax) / 2;
        
        sum = 0;
        for (int &x : trees) {
            sum += max(0, x - hmid);
        }

        if (sum >= m) {
            res = hmid;
            hmin = hmid + 1;
        }
        else {
            hmax = hmid - 1;
        }
    }

    cout << res;
    return 0;
}   
"""


# JAVA
"""
/*
Dùng scanner hay BufferedReader để đọc dữ liệu bị TLE
*/

import java.io.*;
import java.util.*;
 
class Main {
    static int n;
    static long m;
    static long a[];
    
    public static long check(long val) {
        long sum = 0L;
        for (int i = 0; i < a.length; i++) 
            sum += Math.max(0 , a[i] - val); 
 
        return sum; 
    }
    
    public static long BS_search() {
        long left = 0, right = 1000000010L, ans = right;
        while (left <= right)
        {
            long mid = (left + right) / 2;
            if (check(mid) < m) {
                right = mid - 1;
            }
            else {
                ans = mid;
                left = mid + 1;
            }
        }
        return ans;
    }
    
    public static void main(String[] args) throws IOException {
        Reader in = new Reader();
        PrintWriter out = new PrintWriter(System.out);
        
        n = in.nextInt();
        m = in.nextLong();
        a = new long[n];
        for (int i = 0; i < n; i++) {
            a[i] = in.nextLong();
        }
        
        out.printf("%d\n", BS_search());
        out.close();
        return;
    }
}
 
class Reader
{
    final private int BUFFER_SIZE = 1 << 16;
    private DataInputStream din;
    private byte[] buffer;
    private int bufferPointer, bytesRead;
 
    public Reader()
    {
        din = new DataInputStream(System.in);
        buffer = new byte[BUFFER_SIZE];
        bufferPointer = bytesRead = 0;
    }
 
    public Reader(String file_name) throws IOException
    {
        din = new DataInputStream(new FileInputStream(file_name));
        buffer = new byte[BUFFER_SIZE];
        bufferPointer = bytesRead = 0;
    }
 
    public String readLine() throws IOException
    {
        byte[] buf = new byte[64]; // line length
        int cnt = 0, c;
        while ((c = read()) != -1)
        {
            if (c == '\n')
                break;
            buf[cnt++] = (byte) c;
        }
        return new String(buf, 0, cnt);
    }
 
    public int nextInt() throws IOException
    {
        int ret = 0;
        byte c = read();
        while (c <= ' ')
            c = read();
        boolean neg = (c == '-');
        if (neg)
            c = read();
        do
        {
            ret = ret * 10 + c - '0';
        }  while ((c = read()) >= '0' && c <= '9');
 
        if (neg)
            return -ret;
        return ret;
    }
 
    public long nextLong() throws IOException
    {
        long ret = 0;
        byte c = read();
        while (c <= ' ')
            c = read();
        boolean neg = (c == '-');
        if (neg)
            c = read();
        do {
            ret = ret * 10 + c - '0';
        }
        while ((c = read()) >= '0' && c <= '9');
        if (neg)
            return -ret;
        return ret;
    }
 
    public double nextDouble() throws IOException
    {
        double ret = 0, div = 1;
        byte c = read();
        while (c <= ' ')
            c = read();
        boolean neg = (c == '-');
        if (neg)
            c = read();
 
        do {
            ret = ret * 10 + c - '0';
        }
        while ((c = read()) >= '0' && c <= '9');
 
        if (c == '.')
        {
            while ((c = read()) >= '0' && c <= '9')
            {
                ret += (c - '0') / (div *= 10);
            }
        }
 
        if (neg)
            return -ret;
        return ret;
    }
 
    private void fillBuffer() throws IOException
    {
        bytesRead = din.read(buffer, bufferPointer = 0, BUFFER_SIZE);
        if (bytesRead == -1)
            buffer[0] = -1;
    }
 
    private byte read() throws IOException
    {
        if (bufferPointer == bytesRead)
            fillBuffer();
        return buffer[bufferPointer++];
    }
 
    public void close() throws IOException
    {
        if (din == null)
            return;
        din.close();
    }
}
"""