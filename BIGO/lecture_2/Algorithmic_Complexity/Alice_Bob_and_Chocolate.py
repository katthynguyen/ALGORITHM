# python 3
n = int(input())
chocolate = list(map(int, input().split()))
t_alice = t_bob = 0
i, j = 0, n - 1

while i <= j:
    if t_alice + chocolate[i] <= t_bob + chocolate[j]:
        t_alice += chocolate[i]
        i += 1
    else:
        t_bob += chocolate[j]
        j -= 1

print(i, n - i)


#  C++
"""
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> chocolate(n);

    for (int i = 0; i < n; i++) {
        cin >> chocolate[i];
    }

    int t_alice = 0, t_bob = 0;
    int i = 0, j = n - 1;

    while (i <= j) {
        if (t_alice + chocolate[i] <= t_bob + chocolate[j]) {
            t_alice += chocolate[i];
            i++;
        }
        else {
            t_bob += chocolate[j];
            j--;
        }
    }

    cout << i << " " << n - i;
    return 0;
}
"""

#  JAVA
"""
import java.util.Scanner;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<Integer> chocolate = new ArrayList<>();
        int n = sc.nextInt();

        for (int i = 0; i < n; i++) {
            chocolate.add(sc.nextInt());
        }

        int t_alice = 0, t_bob = 0;
        int i = 0, j = n - 1;

        while (i <= j) {
            if (t_alice + chocolate.get(i) <= t_bob + chocolate.get(j)) {
                t_alice += chocolate.get(i);
                i++;
            }
            else {
                t_bob += chocolate.get(j);
                j--;
            }
        }

        System.out.print(i + " " + (n - i));
    }
}
"""