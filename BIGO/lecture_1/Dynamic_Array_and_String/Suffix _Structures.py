# Python3
def getChar(x):
    return chr(x + ord('a'))

s = input()
t = input()

need_tree = array = automaton = False

for i in range(26):
    t_count = t.count(getChar(i))
    s_count = s.count(getChar(i))

    if t_count > s_count:
        need_tree = True
    elif t_count < s_count:
        automaton = True

index_found, match = 0, -1

for i in range(len(t)):
    index_found = s.find(t[i], match + 1)
    if index_found > match:
        match = index_found
    else:
        array = True
        break

if need_tree:
    print("need tree")
elif automaton and array:
    print("both")
elif automaton:
    print("automaton")
else:
    print("array")


# C++
"""
#include <iostream>
#include <string>
using namespace std;

int main() {
    int sCount[26] = {0}, tCount[26] = {0};
    string s, t;
    bool need_tree = false, array = false, automaton = false;

    cin >> s >> t;

    for (int i = 0; i < s.size(); i++) {
        sCount[s[i] - 'a']++;
    }

    for (int i = 0; i < t.size(); i++) {
        tCount[t[i] - 'a']++;
    }

    for (int i = 0; i < 26; i++) {
        if (tCount[i] > sCount[i]) {
            need_tree = true;
        }
        else if (tCount[i] < sCount[i]) {
            automaton = true;
        }
    }

    int index_found = 0, match = -1;

    for (int i = 0; i < t.size(); i++) {
        index_found = s.find_first_of(t[i], match + 1);
        
        if (index_found > match) {
            match = index_found;
        }
        else {
            array = true;
            break;
        }
    }

    if (need_tree) {
        cout << "need tree";
    }
    else if (automaton && array) {
        cout << "both";
    }
    else if (automaton) {
        cout << "automaton";
    }
    else {
        cout << "array";
    }

    return 0;
}
"""

# JAVA
"""
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        String t = sc.next();
        
        boolean need_tree = false, array = false, automaton = false;
        int[] sCount = new int[26];
        int[] tCount = new int[26];

        for (int i = 0; i < s.length(); i++) {
            sCount[s.charAt(i) - 'a']++;
        }

        for (int i = 0; i < t.length(); i++) {
            tCount[t.charAt(i) - 'a']++;
        }

        for (int i = 0; i < 26; i++) {
            if (tCount[i] > sCount[i]) {
                need_tree = true;
            }
            else if (tCount[i] < sCount[i]) {
                automaton = true;
            }
        }

        int index_found = 0, match = -1;

        for (int i = 0; i < t.length(); i++) {
            index_found = s.indexOf(t.charAt(i), match + 1);

            if (index_found > match) {
                match = index_found;
            }
            else {
                array = true;
                break;
            }
        }

        if (need_tree) {
            System.out.print("need tree");
        }
        else if (automaton && array) {
            System.out.print("both");
        }
        else if (automaton) {
            System.out.print("automaton");
        }
        else {
            System.out.print("array");
        }
    }
}
"""