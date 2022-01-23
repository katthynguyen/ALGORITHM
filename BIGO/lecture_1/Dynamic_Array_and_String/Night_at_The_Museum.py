# PYTHON 3
wheel = input()
 
pointer = 'a'
count = 0
 
for c in wheel:
    dist = abs(ord(pointer) - ord(c))
     
    if dist < 13:
        count = count + dist
    else:
        count = count + (26 - dist)
     
    pointer = c
 
print(count)


# C++
"""
#include <iostream>
#include <string>
using namespace std;
 
int main() {
    string wheel;
    cin >> wheel;
 
    char pointer = 'a';
    int dist, count = 0;
 
    for (char &c : wheel) {
        dist = abs(pointer - c);
 
        if (dist < 13) {
            count = count + dist;
        }
        else {
            count = count + (26 - dist);
        }
 
        pointer = c;
    }
 
    cout << count;
    return 0;
}
"""

# JAVA
"""
import java.util.Scanner;
 
public class Main {
    public static void main(String[] agrs) {
        Scanner sc = new Scanner(System.in);
        String wheel = sc.next();
        char pointer = 'a';
        int dist, count = 0;
 
        for (char c : wheel.toCharArray()) {
            dist = Math.abs(pointer - c);
 
            if (dist < 13) {
                count = count + dist;
            }
            else {
                count = count + (26 - dist);
            }
 
            pointer = c;
        }
 
        System.out.print(count);
    }
}
"""
