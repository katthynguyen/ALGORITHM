#  Python 3
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
 
count = i = 0
 
for j in range(m):
    if i >= n:
        break
 
    if b[j] >= a[i]:
        count += 1
        i += 1
 
print(n - count)
#  C++
"""
#include <iostream>
#include <vector>
using namespace std;
 
int main() {
    int n, m;
    cin >> n >> m;
    vector<int> a(n), b(m);
 
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    for (int i = 0; i < m; i++) {
        cin >> b[i];
    }
 
    int count = 0;
    for (int i = 0, j = 0; i < n && j < m; j++) {
        if (b[j] >= a[i]) {
            count++;
            i++;
        }
    }
 
    cout << n - count;
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
        int n = sc.nextInt();
        int m = sc.nextInt();
        ArrayList<Integer> a = new ArrayList<>(), b = new ArrayList<>();
 
        for (int i = 0; i < n; i++) {
            a.add(sc.nextInt());
        }
        for (int i = 0; i < m; i++) {
            b.add(sc.nextInt());
        }
 
        int count = 0;
        for (int i = 0, j = 0; i < n && j < m; j++) {
            if (b.get(j) >= a.get(i)) {
                count++;
                i++;
            }
        }
 
        System.out.print(n - count);
    }
}
"""
