#  Python3
def transform(expression):
    s = []
    for symbol in expression:
        if symbol.isalpha():
            print(symbol, end='')
        elif symbol == ')':
            print(s.pop(), end='')
        elif symbol != '(':
            s.append(symbol)
    print()
 
t = int(input())
for i in range(t):
    expression = input()
    transform(expression)
# C++
"""
#include <iostream>
#include <stack>
#include <string>
using namespace std;
 
void transform(string expression) {
    stack<char> s;
     
    for (char symbol : expression) {
        if (isalpha(symbol)) {
            cout << symbol;
        }
        else if (symbol == ')') {
            cout << s.top();
            s.pop();
        }
        else if (symbol != '(') {
            s.push(symbol);
        }
    }
    cout << endl;
}
 
int main() {
    int t;
    string expression;
 
    cin >> t;
    for (int i = 0; i < t; i++) {
        cin >> expression;
        transform(expression);
    }
    return 0;
}
"""

#  JAVA

"""
import java.util.Scanner;
import java.util.Stack;
 
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        Stack<Character> s = new Stack<>();
 
        for (int i = 0; i < t; i++) {
            char[] expression = sc.next().toCharArray();
            for (Character symbol : expression) {
                if (Character.isLetter(symbol)) {
                    System.out.print(symbol);
                }
                else if (symbol.equals(')')) {
                    System.out.print(s.pop());
                }
                else if (!symbol.equals('(')) {
                    s.add(symbol);
                }
            }
            System.out.println();
        }
    }
}

"""