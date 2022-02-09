# python 3
class Node:
   def __init__(self):
      self.end_word = False
      self.child = dict()

def addWord(root, s):
   temp = root
   s_prefix_other = False
   other_prefix_s = True
   
   for ch in s:
      if ch not in temp.child:
         temp.child[ch] = Node()
         other_prefix_s = False
      
      temp = temp.child[ch]
      if temp.end_word:
         s_prefix_other = True
   
   temp.end_word = True
   return s_prefix_other or other_prefix_s

t = int(input())
for tc in range(t):
   n = int(input())
   root = Node()
   is_inconsistent = False

   for _ in range(n):
      if not is_inconsistent:
         is_inconsistent = addWord(root, input())
      else:
         input()

   print('Case {}: {}'.format(tc + 1, 'NO' if is_inconsistent else 'YES'))
# C++
"""
#include <iostream>
#include <vector>
using namespace std;
const int MAX = 10;

struct Node {
   Node* child[MAX];
   bool end_word;
};

Node *newNode() {
   Node *new_node = new Node;
   new_node->end_word = false;
   for (int i = 0; i < MAX; i++) {
      new_node->child[i] = nullptr;
   }
   return new_node;
}

bool addWord(Node* root, const string& s) {
   Node* temp = root;
   bool s_prefix_other = false;
   bool other_prefix_s = true;

   for (int i = 0; i < s.size(); i++) {
      int ch = s[i] - '0';

      if (temp->child[ch] == nullptr) {
         temp->child[ch] = newNode();
         other_prefix_s = false;
      }

      temp = temp->child[ch];
      if (temp->end_word) {
         s_prefix_other = true;
      }
   }

   temp->end_word = true;
   return (s_prefix_other || other_prefix_s);
}
      
int main() {
   int t, n, tc;
   string s;
   cin >> t;

   for (tc = 1; tc <= t; tc++) {
      cin >> n;
      Node* root = newNode();
      bool is_inconsistent = false;

      for (int i = 0; i < n; i++) {
         cin >> s;
         if (!is_inconsistent) {
            is_inconsistent = addWord(root, s);
         }
      }

      cout << "Case " << tc << ": " << (is_inconsistent ? "NO" : "YES") << endl;
   }
   return 0;
}
"""
# JAVA
"""
import java.io.*;
import java.util.*;
import java.lang.*;

class Node {
    static final int MAX = 10;
    public Node[] child;
    public boolean isLeaf;
    public Node() {
        child = new Node[MAX];
        isLeaf = false;
    }
}
class Trie {
    Node root;
    public Trie() {
        root = new Node();
    }
    public boolean add(String s) {
        Node p = root;
        boolean flag = false;
        for (int i = 0; i < s.length(); i++) {
            int c = s.charAt(i) - '0';
            if (p.child[c] == null) {
                p.child[c] = new Node();
                flag = true;
            }
            p = p.child[c];
            if (p.isLeaf) {
                flag = false;
                break;
            }
        }
        p.isLeaf = true;
        return flag;
    }
}

class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int T = Integer.parseInt(sc.nextLine());
        for (int t = 1; t <= T; t++) {
            System.out.print("Case " + t + ": ");
            Trie trie = new Trie();
            int n = Integer.parseInt(sc.nextLine());
            boolean flag = true;
            while (n-- > 0) {
                String s = sc.nextLine();
                if (flag && !trie.add(s)) 
                    flag = false;
            }
            if (flag)
                System.out.println("YES");
            else
                System.out.println("NO");
        }
        System.exit(0);
    }
}
"""

