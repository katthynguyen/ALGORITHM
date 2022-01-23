n = int(input())
a = list(map(int, input().split()))
 
fre = [0] * (10 ** 5 + 5)
diff = 0
j = 0
longest_range = 0
 
for i in range(n):
    if fre[a[i]] == 0:
        diff += 1
    fre[a[i]] += 1
 
    while j < n and diff > 2:
        if fre[a[j]] == 1:
            diff -= 1
        fre[a[j]] -= 1
        j += 1
     
    longest_range = max(longest_range, i - j + 1)
 
print(longest_range)

#  C++

"""
#include <iostream>
#include <vector>
using namespace std;
const int MAX = 1e5 + 5;
 
int fre[MAX];
 
int main() {
    int n;
    cin >> n;
    vector<int> a(n);
 
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
 
    int j = 0, diff = 0;
    int longest_range = 0;
 
    for (int i = 0; i < n; i++) {
        if (fre[a[i]] == 0) {
            diff++;
        }
        fre[a[i]]++;
 
        while (j < n && diff > 2) {
            if (fre[a[j]] == 1) {
                diff--;
            }
            fre[a[j]]--;
            j++;
        }
 
        longest_range = max(longest_range, i - j + 1);
    }
 
    cout << longest_range;
    return 0;
}
"""

#  Java
"""
import java.util.Scanner;
import java.util.ArrayList;
import java.lang.Math;
 
public class Main {
    static final int MAX = (int)1e5 + 5;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<Integer> a = new ArrayList<>();
        int n = sc.nextInt();
 
        for (int i = 0; i < n; i++) {
            a.add(sc.nextInt());
        }
 
        int[] fre = new int[MAX];
        int j = 0, diff = 0;
        int longest_range = 0;
        
        for (int i = 0; i < n; i++) {
            if (fre[a.get(i)] == 0) {
                diff++;
            }
            fre[a.get(i)]++;
 
            while (j < n && diff > 2) {
                if (fre[a.get(j)] == 1) {
                    diff--;
                }
                fre[a.get(j)]--;
                j++;
            }
 
            longest_range = Math.max(longest_range, i - j + 1);
        }
 
        System.out.print(longest_range);
    }
}
"""
