# Python 3
n, k = map(int, input().split())
cnt = [0] * 101

for _ in range(n):
    s = input()
    cnt[len(s)] += 1

password = input()
best_time = worst_time = 0

for i in range(len(password)):
    best_time += cnt[i]

worst_time = best_time + cnt[len(password)] - 1

best_time += (best_time // k) * 5
worst_time += (worst_time // k) * 5

print(best_time + 1, worst_time + 1, sep=' ')

# C ++

"""
#include <iostream>
#include <string>
using namespace std;

int main() {
    int n, k;
    int cnt[101] = {0};
    string s, password;
    cin >> n >> k;

    for (int i = 0; i < n; i++) {
        cin >> s;
        cnt[s.size()]++;
    }

    cin >> password;

    int best_time = 0, worst_time = 0;

    for (int i = 0; i < password.size(); i++) {
        best_time += cnt[i];
    }

    worst_time = best_time + cnt[password.size()] - 1;
    
    best_time += (best_time / k) * 5;
    worst_time += (worst_time / k) * 5;

    cout << best_time + 1 << " " << worst_time + 1;
    return 0;
}
"""
#  JAVA

"""
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int[] cnt = new int[101];

        for (int i = 0; i < n; i++) {
            String s = sc.next();
            cnt[s.length()]++;
        }

        String password = sc.next();
        int best_time = 0, worst_time = 0;

        for (int i = 0; i < password.length(); i++) {
            best_time += cnt[i];
        }

        worst_time = best_time + cnt[password.length()] - 1;

        best_time += (best_time / k) * 5;
        worst_time += (worst_time / k) * 5;

        System.out.print((best_time + 1) + " " + (worst_time + 1));
    }
}
"""