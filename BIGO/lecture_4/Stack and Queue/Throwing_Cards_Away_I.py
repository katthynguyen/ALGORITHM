# python3
import queue
deck = queue.Queue()
 
while True:
    n = int(input())
    if n == 0:
        break
 
    for i in range(1, n + 1):
        deck.put(i)
 
    discarded_cards = []
      
    while deck.qsize() >= 2:
        discarded_cards.append(deck.get())
        deck.put(deck.get())
     
    print('Discarded cards: ' if discarded_cards else 'Discarded cards:', end='')
    print(*discarded_cards, sep=', ')
    print('Remaining card: {}'.format(deck.get()))
# C++

"""
#include <iostream>
#include <vector>
#include <queue>
using namespace std;
 
int main() {
    int n;
    queue<int> deck;
    vector<int> discarded_cards;
 
    while (true) {
        cin >> n;
        if (n == 0) {
            break;
        }
 
        for (int i = 1; i <= n; i++) {
            deck.push(i);
        }
 
        while (deck.size() >= 2) {
            discarded_cards.push_back(deck.front());
            deck.pop();
            deck.push(deck.front());
            deck.pop();
        }
 
        cout << "Discarded cards:";
        for (int i = 0; i < n - 1; i++) {
            if (i != 0) {
                cout << ",";
            }   
            cout << " " << discarded_cards[i];
        }
        cout << endl;
        cout << "Remaining card: " << deck.front() << endl;
         
        deck.pop();
        discarded_cards.clear();
    }
    return 0;
}
"""

#  JAVA 

"""
import java.util.Scanner;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
 
public class Main {
    public static void main(String[] agrs) {
        Scanner sc = new Scanner(System.in);
        Queue<Integer> deck = new LinkedList<>();
        ArrayList<Integer> discarded_cards = new ArrayList<>();
         
        while (true) {
            int n = sc.nextInt();
            if (n == 0) {
                break;
            }
 
            for (int i = 1; i <= n; i++) {
                deck.add(i);
            }
 
            while (deck.size() >= 2) {
                discarded_cards.add(deck.poll());
                deck.add(deck.poll());
            }
 
            System.out.print("Discarded cards:");
            for (int i = 0; i < n - 1; i++) {
                if (i != 0) {
                    System.out.print(",");
                }
                System.out.format(" %d", discarded_cards.get(i));
            }
            System.out.println();
            System.out.format("Remaining card: %d\n", deck.poll());
 
            discarded_cards.clear();
        }
    }
}
"""