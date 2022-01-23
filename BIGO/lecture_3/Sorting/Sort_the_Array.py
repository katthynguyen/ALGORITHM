#  python3
n = int(input())
a = list(map(int, input().split()))
sorted_a = sorted(a)
l = r = 0

for i in range(n):
    if a[i] != sorted_a[i]:
        l = i
        break

for i in range(len(a) - 1, -1, -1):
    if a[i] != sorted_a[i]:
        r = i
        break

i, j = l, r
while i < j:
    a[i], a[j] = a[j], a[i]
    i += 1
    j -= 1

if a != sorted_a:
    print('no') 
    exit()

print('yes')
print('{} {}'.format(l + 1, r + 1))

#  C++
"""
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> a(n), sorted_a(n);

    for (int i = 0; i < n; i++) {
        cin >> a[i];
        sorted_a[i] = a[i];
    }

    sort(sorted_a.begin(), sorted_a.end());
    int l = 0, r = 0;

    for (int i = 0; i < n; i++) {
        if (a[i] != sorted_a[i]) {
            l = i;
            break;
        }
    }

    for (int i = n - 1; i >= 0; i--) {
        if (a[i] != sorted_a[i]) {
            r = i;
            break;
        }
    }

    for (int i = l, j = r; i < j; i++, j--) {
        swap(a[i], a[j]);
    }

    if (a != sorted_a) {
        cout << "no";
        return 0;
    }

    cout << "yes" << endl;
    cout << l + 1 << " " << r + 1;
    return 0;
}
"""

#  JAVA
"""
import java.util.Scanner;
import java.util.Arrays;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] a = new int[n], sorted_a = new int[n];

        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
            sorted_a[i] = a[i];
        }

        Arrays.sort(sorted_a);
        int l = 0, r = 0;

        for (int i = 0; i < n; i++) {
            if (a[i] != sorted_a[i]) {
                l = i;
                break;
            }
        }

        for (int i = n - 1; i >= 0; i--) {
            if (a[i] != sorted_a[i]) {
                r = i;
                break;
            }
        }

        for (int i = l, j = r; i < j; i++, j--) {
            int temp = a[i];
            a[i] = a[j];
            a[j] = temp;
        }

        if (!Arrays.equals(a, sorted_a)) {
            System.out.print("no");
            return;
        }

        System.out.println("yes");
        System.out.print((l + 1) + " " + (r + 1));
    }
}
"""