# Python
n = int(input())
L, R = [], []
 
for _ in range(n):
    a, b = map(int, input().split())
    L.append(a)
    R.append(b)
 
left, right = min(L), max(R)
 
for i in range(n):
    if left == L[i] and right == R[i]:
        print(i + 1)
        exit()
 
print(-1)
# C++
"""
#include <iostream>
#include <vector>
using namespace std;
const int INF = 1e9 + 5;
 
int main() {
    int n;
    cin >> n;
    vector<int> L(n), R(n);
     
    int left = INF, right = 0;                  // Sentinal values
 
    for (int i = 0; i < n; i++) {
        cin >> L[i] >> R[i];
        left = min(left, L[i]);
        right = max(right, R[i]);
    }
 
    for (int i = 0; i < n; i++) {
        if (left == L[i] && right == R[i]) {
            cout << i + 1;
            return 0;
        }
    }
 
    cout << -1;
    return 0;
}
"""
# JAVA
"""
#include <iostream>
#include <vector>
using namespace std;
const int INF = 1e9 + 5;
 
int main() {
    int n;
    cin >> n;
    vector<int> L(n), R(n);
     
    int left = INF, right = 0;                  // Sentinal values
 
    for (int i = 0; i < n; i++) {
        cin >> L[i] >> R[i];
        left = min(left, L[i]);
        right = max(right, R[i]);
    }
 
    for (int i = 0; i < n; i++) {
        if (left == L[i] && right == R[i]) {
            cout << i + 1;
            return 0;
        }
    }
 
    cout << -1;
    return 0;
}
"""