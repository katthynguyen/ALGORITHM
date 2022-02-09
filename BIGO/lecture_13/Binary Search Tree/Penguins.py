# python 3
def solve():
    n = int(input())
    S = dict()
    for i in range(n):
        name = input()
        if name in S:
            S[name] = S[name] + 1
        else:
            S[name] = 1
    ans = ""
    max = 0
    for item in S:
        if S[item] > max:
            max = S[item]
            ans = item
    print (ans)
 
solve()
# C++
"""
#include <bits/stdc++.h> 
  
using namespace std; 
  
int n; 
map <string , int> mymap; 
string s; 
  
int main () {
    cin >> n; 
  
    cin.ignore(); 
  
    while (n--) {
        getline(cin , s); 
        mymap[s]++; 
    }
  
    string res; 
    int maxi = -1; 
  
    for (map <string , int> :: iterator it = mymap.begin(); it != mymap.end(); it++) 
        if (maxi < it->second) {
            maxi = it->second; 
            res = it->first; 
        }
  
    cout << res; 
    return 0; 
}
"""
# JAVA
"""
import java.io.File;
import java.io.IOException;
import java.util.*;
 
public class Penguins {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        Map<String, Integer> penguins = new TreeMap<>();
        int n = Integer.parseInt(sc.nextLine());
        while (n-- > 0) {
            String name = sc.nextLine();
            if (penguins.containsKey(name))
                penguins.put(name, penguins.get(name) + 1);
            else
                penguins.put(name, 1);
        }
        String kind = "";
        int maxCount = 0;
        for (String name : penguins.keySet())
            if (maxCount < penguins.get(name)) {
                kind = name;
                maxCount = penguins.get(name);
            }
        System.out.println(kind);
    }
}
"""

