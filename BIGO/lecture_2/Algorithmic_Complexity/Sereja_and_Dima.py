#  python3
n = int(input())
cards = list(map(int, input().split()))
res = [0, 0]
player = 0
i, j = 0, n - 1
 
while i <= j:
    if cards[i] > cards[j]:
        res[player] += cards[i]
        i += 1
    else:
        res[player] += cards[j]
        j -= 1
     
    player = 1 - player
 
print(res[0], res[1])


#  C++
"""
#include <iostream>
#include <vector>
using namespace std;
 
int main() {
    int n;
    cin >> n;
    vector<int> cards(n);
 
    for (int i = 0; i < n; i++) {
        cin >> cards[i];
    }
 
    int res[2] = {0};
    int player = 0;
    int i = 0, j = n - 1;
 
    while (i <= j) {
        if (cards[i] > cards[j]) {
            res[player] += cards[i];
            i++;
        }
        else {
            res[player] += cards[j];
            j--;
        }
 
        player = 1 - player;
    }
 
    cout << res[0] << " " << res[1];
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
        ArrayList<Integer> cards = new ArrayList<>();
        int n = sc.nextInt();
 
        for (int i = 0; i < n; i++) {
            cards.add(sc.nextInt());
        }
 
        int[] res = {0, 0};
        int player = 0;
        int i = 0, j = n - 1;
 
        while (i <= j) {
            if (cards.get(i) > cards.get(j)) {
                res[player] += cards.get(i);
                i++;
            }
            else {
                res[player] += cards.get(j);
                j--;
            }
 
            player = 1 - player;
        }
 
        System.out.print(res[0] + " " + res[1]);
    }
}
"""