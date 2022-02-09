# python 3
message = input()
newspaper = input()
a = dict([ (i, 0) for i in range(52) ])
b = dict([ (i, 0) for i in range(52) ])
for ch in message:
    id = ord(ch) - 65
    if (ch > 'Z'):
        id = ord(ch) - 97 + 26
    if not id in a:
        a[id] = 1
    else:
        a[id] += 1
for ch in newspaper:
    id = ord(ch) - 65
    if (ch > 'Z'):
        id = ord(ch) - 97 + 26
    if not id in b:
        b[id] = 1
    else:
        b[id] += 1
yay = 0
whoops = 0
for i in range(52):
    tmp = min(a[i], b[i])
    yay += tmp
    a[i] -= tmp
    b[i] -= tmp
for i in range(26):
    whoops += min(a[i], b[i+26]) + min(a[i+26], b[i])
print("%d %d" % (yay, whoops))
# C++
"""
#include <iostream>
#include <map>
#include <algorithm>
using namespace std;

int main() {
    string message, newspaper;
    map<int, int> a, b;
    int n, m, yay = 0, whoops = 0;
    cin >> message >> newspaper;
    
    for (int i = 0; message[i] != 0; i++) {
        int id = message[i] - 'A';
        if (message[i] > 'Z')
            id = message[i] - 'a' + 26;
        a[id]++;
    }
    for (int i = 0; newspaper[i] != 0; i++) {
        int id = newspaper[i] - 'A';
        if (newspaper[i] > 'Z')
            id = newspaper[i] - 'a' + 26;
        b[id]++;
    }
    
    for (int i = 0; i < 52; i++) {
        int tmp = min(a[i], b[i]);
        yay += tmp;
        a[i] -= tmp; b[i] -= tmp;
    }
    for (int i = 0; i < 26; i++) {
        whoops += min(a[i], b[i+26]) + min(a[i+26], b[i]);
    }
    cout << yay << " " << whoops;
    return 0;
}
"""
# JAVA
"""
import java.util.*;
import java.lang.*;
import java.io.*;

public class Main
{
    public static void main (String[] args) throws java.lang.Exception
    {
        Scanner in = new Scanner(System.in);
        String message, newspaper;
        Map<Integer, Integer> a = new HashMap<Integer, Integer>();
        Map<Integer, Integer> b = new HashMap<Integer, Integer>();
        int yay = 0, whoops = 0;
        message = in.nextLine();
        newspaper = in.nextLine();
        
        for (int i = 0; i < 52; i++) {
            a.put(i, 0);
            b.put(i, 0);
        }
        for (int i = 0; i < message.length(); i++) {
            int id = message.charAt(i) - 'A';
            if (message.charAt(i) > 'Z')
        	    id = message.charAt(i) - 'a' + 26;
            a.put(id, a.get(id) + 1);
        }
        for (int i = 0; i < newspaper.length(); i++) {
            int id = newspaper.charAt(i) - 'A';
            if (newspaper.charAt(i) > 'Z')
        	    id = newspaper.charAt(i) - 'a' + 26;
            b.put(id, b.get(id) + 1);
        }
    
        for (int i = 0; i < 52; i++) {
            int tmp = Math.min(a.get(i), b.get(i));
            yay += tmp;
            a.put(i, a.get(i) - tmp);
            b.put(i, b.get(i) - tmp);
        }
        for (int i = 0; i < 26; i++) {
            whoops += Math.min(a.get(i), b.get(i+26)) + Math.min(a.get(i+26), b.get(i));
        }
        System.out.printf("%d %d", yay, whoops);
    }
}
"""

