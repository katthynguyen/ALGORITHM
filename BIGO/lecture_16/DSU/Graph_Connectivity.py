# python 3
import sys

def getroot(lab, u):
    if lab[u] == -1:
        return u
    lab[u] = getroot(lab, lab[u])
    return lab[u]

def union(lab, cou, a, b):
    if cou[a] > cou[b]:
        cou[a] += cou[b]
        lab[b] = a
    else:
        cou[b] += cou[a]
        lab[a] = b

def convert_number(x):
    return ord(x) - ord('A')

def solve():
    inf = sys.stdin
    input = []
    for line in inf:
        input.append(line)
    len_input = len(input)
    k = 0
    testcase = int(input[k])
    k+=1
    for t in range(testcase):
        k+=1
        x = list(input[k])[0]
        k+=1
        n = convert_number(x) + 1
        lab = [-1 for i in range(n)]
        cou = [1 for i in range(n)]
        while k < len_input and input[k] != '\n':
            temp = list(input[k])
            u = convert_number(temp[0])
            v = convert_number(temp[1])
            k+=1
            u = getroot(lab, u)
            v = getroot(lab, v)
            if u != v:
                union(lab, cou, u, v)
        ans = lab.count(-1)
        if t == testcase - 1:
            print(ans)
        else:
            print("{}\n".format(ans))

solve()
# C++
"""
#include <bits/stdc++.h> 

using namespace std;

int parent[26];

int test , n , u , v , ans; 
char c;
string s;

void init(int u) {
    parent[u] = u;
}

int findSet(int u) {
    while (u != parent[u]) u = parent[u]; 

    return u; 
}

int unionSet(int u , int v){
    int up = findSet(u); int vp = findSet(v); 

    parent[vp] = up; 
}

int main() {
    scanf("%d\n\n" , &test); 
    
    for(int t = 1; t <= test; t++) {
        getline(cin,s);
        n = s[0] - 'A' + 1; 
        
        ans = n; 
        for (int i = 0; i < n; i++) init(i); 
        
        while(1) {
            if (!getline(cin , s) || s.empty()) break; 
            
            u = s[0] - 'A'; v = s[1] - 'A'; 
            
            int up = findSet(u); int vp = findSet(v); 

            if (up != vp) {
                ans--; 
                unionSet(u , v); 
            }
        }
        
        if (t != 1) printf("\n"); 
        printf("%d\n" , ans); 
    }
    
    return 0;
}
"""
# JAVA
"""
import java.io.*;
import java.util.*;

class DSU {
    Integer[] parent;
    public DSU(int size) {
        parent = new Integer[size];
        for (int i = 0; i < size; i++)
            parent[i] = i;
    }
    public int find(int u) {
        while (u != parent[u])
            u = parent[u];
        return u;
    }
    public void union(int u, int v) {
        u = find(u);
        v = find(v);
        parent[v] = u;
    }
}
class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int T = Integer.parseInt(sc.nextLine());
        sc.nextLine();
        while (T-- > 0) {
            int n = sc.nextLine().charAt(0) - 'A' + 1;
            DSU dsu = new DSU(n);
            int ans = n;
            while (sc.hasNextLine()) {
                String s = sc.nextLine();
                if (s.isEmpty())
                    break;
                int u = dsu.find(s.charAt(0) - 'A');
                int v = dsu.find(s.charAt(1) - 'A');
                if (u != v) {
                    ans--;
                    dsu.union(u, v);
                }
            }
            System.out.println(ans);
            if (T > 0)
                System.out.println();
        }
    }
}
"""

