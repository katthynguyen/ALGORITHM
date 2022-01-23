#  python 3
n, k = map(int, input().split())
a = list(map(int, input().split()))
fre = [0] * (10 ** 5 + 5)
unique = 0
j = 0
 
for i in range(n):
    if fre[a[i]] == 0:
        unique += 1
     
    fre[a[i]] += 1
 
    while unique == k:
        fre[a[j]] -= 1
 
        if fre[a[j]] == 0:
            print(j + 1, i + 1)
            exit()
         
        j += 1
 
print('-1 -1')

#  c++
"""
#include <iostream>
#include <vector>
using namespace std;
const int MAX = 1e5 + 5;
 
int fre[MAX];
 
int main() {
    int n, k;
    cin >> n >> k;
    vector<int> a(n + 1);
 
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
     
    int unique = 0;
    int j = 0;
 
    for (int i = 0; i < n; i++) {
        if (fre[a[i]] == 0) {
            unique++;
        }
 
        fre[a[i]]++;
             
        while (unique == k) {
            fre[a[j]]--;
 
            if (fre[a[j]] == 0) {
                cout << j + 1 << " " << i + 1;
                return 0;
            }
 
            j++;
        }
 
    }
     
    cout << "-1 -1";
    return 0;
}
"""

#  java
"""
import java.util.Scanner;
import java.util.ArrayList;
 
public class Main {
    static final int MAX = (int)1e5 + 5;
    static int fre[] = new int[MAX];
     
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        ArrayList<Integer> a = new ArrayList<>();
         
        for (int i = 0; i < n; i++) {
            a.add(sc.nextInt());
        }
         
        int unique = 0;
        int j = 0;
 
        for (int i = 0; i < n; i++) {
            if (fre[a.get(i)] == 0) {
                unique++;
            }
 
            fre[a.get(i)]++;
             
            while (unique == k) {
                fre[a.get(j)]--;
 
                if (fre[a.get(j)] == 0) {
                    System.out.printf("%d %d", j + 1, i + 1); 
                    return;
                }
 
                j++;
            }
        }
 
        System.out.print("-1 -1");
    }
}
"""