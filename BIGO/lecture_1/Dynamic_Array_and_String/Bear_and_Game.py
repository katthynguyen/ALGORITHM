# Python
n = int(input())
v = list(map(int, input().split(' ')))
 
t = 0
for i in range(n):
    if t + 15 < v[i]:
        print(t + 15)
        exit()
    else:
        t = v[i]
         
print(min(90, t + 15))

# C++
"""
#include <iostream>
#include <vector>
using namespace std;
 
int main() {
    int n;
    cin >> n;
    vector<int> v(n);
 
    for (int i = 0; i < n; i++) {
        cin >> v[i];
    }
     
    int t = 0;    
    for (int i = 0; i < n; i++) {
        if (t + 15 < v[i]) {
            cout << t + 15;
            return 0;
        }
        else {
            t = v[i];
        }
    }
     
    cout << min(t + 15, 90);
    return 0;
}
"""
# JAVA
"""
import java.util.Scanner;
import java.util.ArrayList;
import java.lang.Math;
 
public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        ArrayList<Integer> a = new ArrayList<>();
 
        for (int i = 0; i < n; i++) {
            a.add(sc.nextInt());
        }
 
        int t = 0;
        for (int i = 0; i < n; i++) {
            if (t + 15 < a.get(i)) {
                System.out.print(t + 15);
                return;
            }
            else {
                t = a.get(i);
            }
        }
 
        System.out.print(Math.min(t + 15, 90));
    }
}
"""