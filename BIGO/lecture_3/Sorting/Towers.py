# python3
n = int(input())
bars = list(map(int, input().split()))
bars.sort()

n_towers = max_height = cur_height = 1

for i in range(1, n):
    if bars[i] == bars[i - 1]:
        cur_height += 1
        max_height = max(max_height, cur_height)
    else:
        n_towers += 1
        cur_height = 1

print(max_height, n_towers)

#  C++

"""
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> bars(n);

    for (int i = 0; i < n; i++) {
        cin >> bars[i];
    }

    sort(bars.begin(), bars.end());
    int n_towers = 1, max_height = 1, cur_height = 1;

    for (int i = 1; i < n; i++) {
        if (bars[i] == bars[i - 1]) {
            cur_height++;
            max_height = max(max_height, cur_height);
        }
        else {
            n_towers++;
            cur_height = 1;
        }
    }

    cout << max_height << " " << n_towers;
    return 0;
}
"""

#  JAVA
"""
import java.util.Scanner;
import java.lang.Math;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] bars = new int[n];

        for (int i = 0; i < n; i++) {
            bars[i] = sc.nextInt();
        }

        Arrays.sort(bars);
        int n_towers = 1, max_height = 1, cur_height = 1;

        for (int i = 1; i < n; i++) {
            if (bars[i] == bars[i - 1]) {
                cur_height++;
                max_height = Math.max(max_height, cur_height);
            }
            else {
                n_towers++;
                cur_height = 1;
            }
        }

        System.out.print(max_height + " " + n_towers);
    }
}
"""