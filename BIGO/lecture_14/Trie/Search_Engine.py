# python 3
class Node:
    def __init__(self):
        self.child = dict()
        self.maxValue = -1

def addWord(root, s, value):
    tmp = root
    for c in s:
        if c not in tmp.child:
            tmp.child[c] = Node()
        tmp = tmp.child[c]
        tmp.maxValue = max(tmp.maxValue, value)

def getHeighestMatching(root, s):
    tmp = root
    for c in s:
        if c not in tmp.child:
            return -1
        tmp = tmp.child[c]
    return tmp.maxValue

n, q = map(int, input().strip().split())
root = Node()

for _ in range(n):
    line = input().strip().split()
    addWord(root, line[0], int(line[1]))

for _ in range(q):
    s = input().strip()
    print(getHeighestMatching(root, s))
# C++
"""
#include <bits/stdc++.h>
#define ALPHABET_SIZE 26
using namespace std;

struct Node {
    struct Node *child[ALPHABET_SIZE];
    int maxValue;
};

struct Node *newNode() {
    struct Node *pNode = new struct Node;
    pNode->maxValue = -1;

    for (int i = 0; i < ALPHABET_SIZE; i++) {
        pNode->child[i] = nullptr;
    }
    
    return pNode;
}

void addWord(struct Node *root, string s, int value) {
    struct Node *tmp = root;
    
    for (char &c : s) {
        int pos = c - 'a';
        if (!tmp->child[pos]) {
            tmp->child[pos] = newNode();
        }
        
        tmp = tmp->child[pos];
        tmp->maxValue = max(tmp->maxValue, value);
    }
}

int getHighestMatching(struct Node *root, string s) {
    struct Node *tmp = root;

    for (char &c : s) {
        int pos = c - 'a';
        if (!tmp->child[pos]) {
            return -1;
        }
        tmp = tmp->child[pos];
    }
    
    return tmp->maxValue;
}

int main() {
    int n, q, value;
    string s;
    cin >> n >> q;
    struct Node *root = newNode();

    for (int i = 0; i < n; i++) {
        cin >> s >> value;
        addWord(root, s, value);
    }

    for (int i = 0; i < q; i++) {
        cin >> s;
        cout << getHighestMatching(root, s) << endl;
    }

    return 0;
}
"""
# JAVA
"""
import java.util.*;

public class Main {
    static final int ALPHABET_SIZE = 26;
    
    static class Node {
        Node[] child = new Node[ALPHABET_SIZE];
        int maxValue;
    
        Node() {
            maxValue = -1;
            for (int i = 0; i < ALPHABET_SIZE; i++) {
                child[i] = null;
            }
        }
    }
    
    static void addWord(Node root, String s, int value) {
        Node tmp = root;
    
        for (char c : s.toCharArray()) {
            int pos = c - 'a';
            if (tmp.child[pos] == null) {
                tmp.child[pos] = new Node();
            }
    
            tmp = tmp.child[pos];
            tmp.maxValue = Math.max(tmp.maxValue, value);
        }
    }
    
    static int getHighestMatching(Node root, String s) {
        Node tmp = root;
    
        for (char c : s.toCharArray()) {
            int pos = c - 'a';
            if (tmp.child[pos] == null) {
                return -1;
            }
            tmp = tmp.child[pos];
        }
    
        return tmp.maxValue;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int q = sc.nextInt();
        Node root = new Node();

        for (int i = 0; i < n; i++) {
            String s = sc.next();
            int value = sc.nextInt();
            addWord(root, s, value);
        }

        for (int i = 0; i < q; i++) {
            String s = sc.next();
            System.out.println(getHighestMatching(root, s));
        }
    }
}
"""

