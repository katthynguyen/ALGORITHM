# EX_1
"""
                    Fashion in Bertland
According to rules of the Berland fashion, 
a jacket should be fastened by all the buttons except only one, 
but not necessarily it should be the last one. 
Also if the jacket has only one button, it should be fastened, 
so the jacket will not swinging open.
You are given a jacket with N buttons. Determine if it is fastened in a right way.
"""

def checkJacket(v, n):
    if n == 1:
        if v[0] == 1:
            return True
        else:
            return False
    count = 0
    for i in range(n):
        if v[i] == 0:
            count += 1
    if count == 1:
        return True
    else:
        return False
 
 
n = int(input())
v = list(map(int, input().split()))
 
if checkJacket(v, n):
    print("YES")
else:
    print("NO")


# C++
"""
#include <iostream>  
#include <vector>  
using namespace std;
 
bool checkJacket(vector<int>& v, int n) {
    if (n == 1) {
        if (v[0] == 1)
            return true;
        else
            return false;
    }
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (v[i] == 0) {
            count++;
        }
    }
    if (count == 1)
        return true;
    else
        return false;
}
 
int main() {
    int n, value;
    cin >> n;
    vector<int> v;
    for (int i = 0; i < n; i++) {
        cin >> value;
        v.push_back(value);
    }
    bool result = checkJacket(v, n);
    if (result == true)
        cout << "YES";
    else
        cout << "NO";
    return 0;
}
"""


# JAVA
"""
import java.util.ArrayList;
import java.util.Scanner;
 
public class Main {
    private static boolean checkJacket(ArrayList<Integer> v, int n) {
        if (n == 1) {
            if (v.get(0) == 1)
                return true;
            else
                return false;
        }
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (v.get(i) == 0) {
                count++;
            }
        }
        if (count == 1)
            return true;
        else
            return false;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int value;
        ArrayList<Integer> v = new ArrayList<>();
 
        for (int i = 0; i < n; i++) {
            value = sc.nextInt();
            v.add(value);
        }
 
        boolean result = checkJacket(v, n);
        if (result == true)
            System.out.println("YES");
        else
            System.out.println("NO");
    }
}
"""