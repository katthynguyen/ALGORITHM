# python 3
class Node:
    def __init__(self):
        self.child = dict()
        self.isLeaf = False

def addWord(root, s):
    flag = False
    temp = root
    for ch in list(s):
        if ch not in temp.child:
            flag = True
            temp.child[ch] = Node()
        temp = temp.child[ch]
        if temp.isLeaf:
            return False
    temp.isLeaf = True
    return flag

n = int(input())
root = Node()
nonVulnerable = True
for i in range(n):
    s = input()
    nonVulnerable &= addWord(root, s)
print(("non " if nonVulnerable else "") + "vulnerable")
# C++
"""
#include <iostream>
#include <string>
using namespace std;
#define MAX 26

struct Node {
    Node* child[MAX];
    bool isLeaf;
};

Node *newNode() {
    Node *node = new Node;
    node->isLeaf = false;
    for (int i = 0; i < MAX; i++)
        node->child[i] = NULL;
    return node;
}

bool addWord(Node* root, string s) {
    Node* temp = root;
    bool flag = false;
    for (int i = 0; i < s.length(); i++) {
        int ch = s[i] - 'a';
        if (temp->child[ch] == NULL) {
            flag = true;
            temp->child[ch] = newNode();
        }
        temp = temp->child[ch];
        if (temp->isLeaf)
            return false;
    }
    temp->isLeaf = true;
    return flag;
}

int main() {
    int n;
    string s;
    cin >> n;
    Node* root = newNode();
    bool nonVulnerable = true;
    while (n--) {
        cin >> s;
        nonVulnerable &= addWord(root, s);
    }
    if (nonVulnerable)
        cout << "non vulnerable";
    else
        cout << "vulnerable";
    return 0;
}
"""
# JAVA
"""
import java.util.*;
import java.io.*;
 
class Node {
    public Node[] child;
    public boolean isLeaf;
    public Node() {
        child = new Node[26];
        this.isLeaf = false;
    }
}

class Trie {
    public static final int MAX = 26;
    private Node root;
    public Trie() {
        root = new Node();
    }
    
    public boolean addWord(String s) {
        Node temp = root;
        boolean flag = false;
        for (int i = 0; i < s.length(); i++) {
            int ch = s.charAt(i) - 'a'; 
            if (temp.child[ch] == null) {
                flag = true;
                temp.child[ch] = new Node();
            }
            temp = temp.child[ch];
            if (temp.isLeaf == true)
                return false;
        }
        temp.isLeaf = true;
        return flag;
    } 
} 

class Main {
    public static void main(String[] args)  {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        in.nextLine();
        Trie trie = new Trie();
        boolean nonVulnerable = true;
        while (n-- > 0) {
            String s = in.nextLine();
            nonVulnerable &= trie.addWord(s);
        }
        if (nonVulnerable)
            System.out.print("non vulnerable");
        else
            System.out.print("vulnerable");
    } 
}
"""

