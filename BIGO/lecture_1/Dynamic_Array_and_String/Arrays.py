# Python 3
na, nb = map(int, input().split()) 
k, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
 
print('YES' if a[k - 1] < b[nb - m] else 'NO')
# C++
"""
#include <iostream>
#include <vector>
using namespace std; 
 
int main() {
    int na, nb, k, m;
    cin >> na >> nb;
    cin >> k >> m;
    vector<int> a(na), b(nb);
     
    for (int i = 0; i < na; i++) {
        cin >> a[i];
    }
    for (int i = 0; i < nb; i++) {
        cin >> b[i];
    }
 
    cout << (a[k - 1] < b[nb - m] ? "YES" : "NO");
 
    return 0;
}
"""

# JAVA
"""
import java.util.Scanner;
import java.util.ArrayList;
 
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int na = sc.nextInt();
        int nb = sc.nextInt();
        int k = sc.nextInt();
        int m = sc.nextInt();
 
        ArrayList<Integer> a = new ArrayList<>(), b = new ArrayList<>();
         
        for (int i = 0; i < na; i++) 
            a.add(sc.nextInt());
             
        for (int i = 0; i < nb; i++)
            b.add(sc.nextInt());
         
        System.out.print(a.get(k - 1) < b.get(nb - m) ? "YES" : "NO");
    } 
}
"""
