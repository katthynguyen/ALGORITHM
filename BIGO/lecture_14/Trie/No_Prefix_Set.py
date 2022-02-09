# python 3
class Node:
    def __init__(self):
        self.child = dict()
        self.countWord = 0

def addWord(root, s):
    temp = root
    for ch in list(s):
        if ch not in temp.child:
            temp.child[ch] = Node()
        temp = temp.child[ch]
        if temp.countWord > 0:
            return False
    temp.countWord += 1
    return len(temp.child) == 0

n = int(input())
root = Node()
nonVulnerable = True
for i in range(n):
    s = input()
    if not addWord(root, s):
        print('BAD SET')
        print(s)
        exit()
print('GOOD SET')
# C++
"""
#include <iostream>
#include <string>
using namespace std;
#define MAX 26

struct Node {
    Node* child[MAX];
    bool countWord;
};

Node *newNode() {
    Node *node = new Node;
    node->countWord = 0;
    for (int i = 0; i < MAX; i++)
        node->child[i] = NULL;
    return node;
}

bool addWord(Node* root, string s) {
    Node* temp = root;
    for (int i = 0; i < s.length(); i++) {
        int ch = s[i] - 'a';
        if (temp->child[ch] == NULL) {
            temp->child[ch] = newNode();
        }
        temp = temp->child[ch];
        if (temp->countWord > 0) // có 1 từ là tiền tố của từ đang thêm vào trie
            return false; 
    }
    temp->countWord++;
    for (int i = 0; i < MAX; i++) {
        if (temp->child[i] != NULL) // từ vừa thêm vào trie là tiền tố của 1 từ khác
            return false;
    }
    return true;
}

int main() {
    int n;
    string s;
    cin >> n;
    Node* root = newNode();
    bool nonVulnerable = true;
    while (n--){
        cin >> s;
        if (!addWord(root, s)){
            cout << "BAD SET\n";
            cout << s << "\n";
            return 0;
        }
    }
    cout << "GOOD SET";
    return 0;
}
"""
# JAVA
"""
import java.util.*;
import java.io.*;
 
class Node {
    public Node[] child;
    public int countWord;
    public Node() {
        child = new Node[26];
        this.countWord = 0;
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
        for (int i = 0; i < s.length(); i++) {
            int ch = s.charAt(i) - 'a'; 
            if (temp.child[ch] == null) {
                temp.child[ch] = new Node();
            }
            temp = temp.child[ch];
            if (temp.countWord > 0) // có 1 từ là tiền tố của từ đang thêm vào trie
                return false;
        }
        temp.countWord += 1;
        for (int i = 0; i < MAX; i++) {
            if (temp.child[i] != null) // từ vừa thêm vào trie là tiền tố của 1 từ khác
                return false;
        }
        return true;
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
            if (!trie.addWord(s)){
                System.out.print("BAD SET\n");
                System.out.print(s);
                return;
            }
        }
        System.out.print("GOOD SET");
    } 
}
"""

