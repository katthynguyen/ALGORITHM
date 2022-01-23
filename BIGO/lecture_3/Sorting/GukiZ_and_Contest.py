# Python3 
n = int(input())
ratings = list(map(int, input().split()))
sorted_ratings = sorted(ratings, reverse=True)
ranked = [0] * 2005

for i in range(n):
    rating = sorted_ratings[i]
    if not ranked[rating]:
        ranked[rating] = i + 1

for rating in ratings:
    print(ranked[rating], end=' ')
# C++
"""
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
const int MAX = 2005;

int ranked[MAX];

int main() {
    int n, rating;
    cin >> n;
    vector<int> ratings(n), sorted_ratings(n);

    for (int i = 0; i < n; i++) {
        cin >> rating;
        ratings[i] = sorted_ratings[i] = rating;
    }

    sort(sorted_ratings.begin(), sorted_ratings.end(), greater<int>());

    for (int i = 0; i < n; i++) {
        rating = sorted_ratings[i];
        
        if (!ranked[rating]) {
            ranked[rating] = i + 1;
        }
    }

    for (int& rating : ratings) {
        cout << ranked[rating] << " ";
    }

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
        int n = sc.nextInt();
        ArrayList<Integer> ratings = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            ratings.add(sc.nextInt());
        }

        ArrayList<Integer> sorted_ratings = new ArrayList<>(ratings);
        Collections.sort(sorted_ratings, Collections.reverseOrder());
        int[] ranked = new int[2005];

        for (int i = 0; i < n; i++) {
            int rating = sorted_ratings.get(i);
            if (ranked[rating] == 0) {
                ranked[rating] = i + 1;
            }
        }

        for (int rating : ratings) {
            System.out.print(ranked[rating] + " ");
        }
    }
}
"""