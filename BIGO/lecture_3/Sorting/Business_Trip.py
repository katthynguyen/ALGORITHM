#  python3
k = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
n_months = 0

for height in a:
    if k <= 0:
        break
    
    n_months += 1
    k -= height

print(n_months if k <= 0 else -1)
#  C++

"""
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int k;
    cin >> k;
    vector<int> a(12);

    for (int i = 0; i < 12; i++) {
        cin >> a[i];
    }

    sort(a.begin(), a.end(), greater<int>());
    int n_months = 0;

    for (int height : a) {
        if (k <= 0) {
            break;
        }

        n_months++;
        k -= height;
    }

    cout << (k <= 0 ? n_months : -1);
    return 0;
}
"""

#  JAVA
"""
import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int k = sc.nextInt();
        ArrayList<Integer> a = new ArrayList<>();

        for (int i = 0; i < 12; i++) {
            a.add(sc.nextInt());
        }

        Collections.sort(a, Collections.reverseOrder());
        int n_months = 0;
        
        for (int height : a) {
            if (k <= 0) {
                break;
            }

            n_months++;
            k -= height;
        }

        System.out.print(k <= 0 ? n_months : -1);
    }
}
"""