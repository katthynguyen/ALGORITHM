# python3
T = int(input())
 
for _ in range(T):
    s = input()
    expr = []
    ans = 0
 
    for i in range(len(s)):
        if s[i] == '<':
            expr.append(s[i])
        elif len(expr) == 0:
            break
        else:
            expr.pop()
            ans = i + 1 if len(expr) == 0 else ans
     
    print(ans)
# C++
"""
#include <iostream>
#include <stack>
#include <string>
using namespace std;
 
int main() {
    int T, ans;
    string s;
    cin >> T;
 
    for (int k = 0; k < T; k++) {
        cin >> s;
        stack<char> expr;
        ans = 0;
 
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == '<') {
                expr.push(s[i]);
            }
            else if (expr.empty()) {
                break;
            }
            else {
                expr.pop();
                ans = (expr.empty() ? i + 1 : ans);
            }
        }
 
        cout << ans << endl;
    }
    return 0;
}
"""
# JAVA
"""
import java.util.Scanner;
import java.util.Stack;
 
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
 
        for (int k = 0; k < T; k++) {
            String s = sc.next();
            Stack<Character> expr = new Stack<>();
            int ans = 0;
 
            for (int i = 0; i < s.length(); i++) {
                if (s.charAt(i) == '<') {
                    expr.push(s.charAt(i));
                }
                else if (expr.empty()) {
                    break;
                }
                else {
                    expr.pop();
                    ans = (expr.empty() ? i + 1 : ans);
                }
            }
 
            System.out.println(ans);
        }
    }
}
"""