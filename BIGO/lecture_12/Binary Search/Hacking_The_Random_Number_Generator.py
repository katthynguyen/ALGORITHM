# python 3
import sys
class Scanner:
    def __init__(self, istream):
        self.tokenizer = Scanner.__tokenizer__(istream)
    def __tokenizer__(istream):
        for line in istream:
                for token in line.strip().split():
                        yield token
    def next(self):
        return self.tokenizer.__next__()

def BS_search(a, l, r, value):
    while l <= r:
        mid = int( (l + r) / 2 )
        if a[mid] == value:
            return True
        if a[mid] > value:
            r = mid - 1
        else:
            l = mid + 1
    return False

def solve():
    sc = Scanner(sys.stdin)
    n = int(sc.next())
    k = int(sc.next())
    a = []
    for i in range(n):
        x = int(sc.next())
        a.append(x)
    a.sort()
    ans = 0
    j = 0
    for i in range(n):
        while j < i and  a[i] - a[j] > k:
            j += 1
        if a[i] - a[j] == k:
            ans += 1
    print(ans)

solve()
# C++

"""
#include <bits/stdc++.h>
using namespace std;

const int MAX = 1e5 + 10;

int main() {
    ios::sync_with_stdio(false);

    int n, k;
    vector<int> a;

    cin >> n >> k;
    a.resize(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    sort(a.begin(), a.end());
    long long count = 0;
    vector<int>::iterator it;
    for (int i = 0; i < n; i++) {
        it = lower_bound(a.begin(), a.end(), a[i] + k);
        if (it != a.end() && *it == a[i] + k) {
            count++;
        }        
    }
    cout << count;
    return 0;
}
"""


# JAVA
"""
/*
Dùng scanner hay BufferedReader để đọc dữ liệu bị TLE
Dùng arraylist hay array đều được
*/
import java.io.*;
import java.util.*;
 
class Main {
  
    public static int BS_search(int a[], int left, int right, int x) {
        while (left <= right)
        {
            int mid = (left + right) / 2;
 
            if (x == a[mid])
                return mid;
            else if (x < a[mid])
                right = mid - 1;
            else if (x > a[mid])
                left = mid + 1;
        }
        return -1;
    }
  
    public static void main(String[] args) throws IOException {
        Reader in = new Reader();
        PrintWriter out = new PrintWriter(System.out);
        int n, k, count = 0;
        
        n = in.nextInt();
        k = in.nextInt();
        int a[] = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = in.nextInt();
        }
        
        Arrays.sort(a);
        for (int i = 0; i < n; i++) {
            if (BS_search(a, i + 1, n - 1, a[i] + k) != -1)
                count++;
        }
        out.printf("%d\n", count);
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