# python3
atom = []
mass = lambda c : 1 if c == 'H' else 12 if c == 'C' else 16
 
for c in input().strip():
    if c.isalpha():
        atom.append(mass(c))
    elif c.isnumeric():
        mol = atom[-1] * int(c)
        atom.pop()
        atom.append(mol)
    elif c == '(':
        atom.append(-1)
    elif c == ')':
        w = 0
        while atom[-1] != -1:
            w += atom[-1]
            atom.pop()
        atom.pop()
        atom.append(w)
 
print(sum(atom))
# C++
"""
#include <iostream>
#include <stack>
#include <string>
using namespace std;
 
int mass(char c) {
    return c == 'H' ? 1 : (c == 'C' ? 12 : 16);
}
 
int main() {
    string s;
    cin >> s;
 
    stack<int> atom;
    int w, mol;
 
    for (char c : s) {
        if (isalpha(c)) {
            atom.push(mass(c));
        }
        else if (isdigit(c)) {
            mol = atom.top() * (c - '0');
            atom.pop();
            atom.push(mol);
        }
        else if (c == '(') {
            atom.push(-1);
        }
        else if (c == ')') {
            w = 0;
            while (atom.top() != -1) {
                w += atom.top();
                atom.pop();
            }
            atom.pop();
            atom.push(w);
        }
    }
     
    int sum = 0;
    while (!atom.empty()) {
        sum += atom.top();
        atom.pop();
    }
 
    cout << sum;
    return 0;
}
"""

#  JAVA

"""
import java.util.Scanner;
import java.util.Stack;
import java.lang.Character;
 
public class Main {
    public static int mass(char c) {
        return c == 'H' ? 1 : (c == 'C' ? 12 : 16);
    }
 
    public static void main(String[] agrs) {
        Scanner sc = new Scanner(System.in);
        String s;
        s = sc.next();
 
        Stack<Integer> atom = new Stack<>();
        int w, mol;
 
        for (char c : s.toCharArray()) {
            if (Character.isLetter(c)) {
                atom.add(mass(c));
            }
            else if (Character.isDigit(c)) {
                mol = atom.peek() * (c - '0');
                atom.pop();
                atom.add(mol);
            }
            else if (c == '(') {
                atom.add(-1);
            }
            else if (c == ')') {
                w = 0;
                while (atom.peek() != -1) {
                    w += atom.peek();
                    atom.pop();
                }
                atom.pop();
                atom.add(w);
            }
        }
 
        int sum = 0;
        while (!atom.isEmpty()) {
            sum += atom.peek();
            atom.pop();
        }
 
        System.out.print(sum);
    }
}
"""