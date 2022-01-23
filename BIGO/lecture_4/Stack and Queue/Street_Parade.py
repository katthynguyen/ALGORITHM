#  Python3
while True:
    n = int(input())
    if n == 0:
        break
    trucks = list(map(int, input().split()))
    side_trucks = []
    ordering = 1
    i = 0
 
    while i < n:
        if trucks[i] == ordering:
            ordering += 1
            i += 1
        elif side_trucks and side_trucks[-1] == ordering:
            ordering += 1
            side_trucks.pop()
        else:
            side_trucks.append(trucks[i])
            i += 1
     
    while side_trucks and side_trucks[-1] == ordering:
        ordering += 1
        side_trucks.pop()
 
    print('yes' if ordering == n + 1 else 'no')

    #  C++

    """
    #include <iostream>
#include <stack>
using namespace std;
const int MAX = 1005;
 
int main() {
    int n;
    int trucks[MAX];
    stack<int> side_trucks;
 
    while (true) {
        cin >> n;
        if (n == 0) {
            break;
        }
     
        for (int i = 0; i < n; i++) {
            cin >> trucks[i];
        }
 
        int ordering = 1;
        int i = 0;
         
        while (i < n) {
            if (trucks[i] == ordering) {
                i++;
                ordering++;
            }
            else if (!side_trucks.empty() && side_trucks.top() == ordering) {
                ordering++;
                side_trucks.pop();
            }
            else {
                side_trucks.push(trucks[i]);
                i++;
            }
        }
 
        while (!side_trucks.empty() && side_trucks.top() == ordering) {
            ordering++;
            side_trucks.pop();
        }
 
        cout << (ordering == n + 1 ? "yes" : "no") << endl;
        while (!side_trucks.empty()) {
            side_trucks.pop();
        }
    }
    return 0;
}
    """

    #  JAVA
    """
    import java.util.Scanner;
import java.util.Stack;
 
public class Main {
    static final int MAX = 1005;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] trucks = new int[MAX];
        Stack<Integer> side_trucks = new Stack<>();
         
        while (true) {
            int n = sc.nextInt();
            if (n == 0) {
                break;
            }
 
            for (int i = 0; i < n; i++) {
                trucks[i] = sc.nextInt();
            }
 
            int ordering = 1;
            int i = 0;
 
            while (i < n) {
                if (trucks[i] == ordering) {
                    ordering++;
                    i++;
                }
                else if (!side_trucks.empty() && side_trucks.peek().equals(ordering)) {
                    ordering++;
                    side_trucks.pop();
                }
                else {
                    side_trucks.push(trucks[i]);
                    i++;
                }
            }
 
            while (!side_trucks.empty() && side_trucks.peek().equals(ordering)) {
                ordering++;
                side_trucks.pop();
            }
 
            System.out.println(ordering == n + 1 ? "yes" : "no");
            side_trucks.clear();
        }
    }
}
    """
