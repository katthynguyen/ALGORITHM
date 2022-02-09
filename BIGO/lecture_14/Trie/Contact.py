# python 3
class TrieNode:
    def __init__(self, c):
        self.count = c
        self.child = dict()
        self.child.clear()

def addContact(root, s):
    for c in list(s):
        if c in root.child:
            root = root.child[c]
        else:
            root.child[c] = TrieNode(0)
            root = root.child[c]
        root.count += 1
        

def countContacts(root, s):
    
    for c in list(s):
        if c in root.child:
            root = root.child[c]
        else:
            return 0
    return root.count

n = int(input())
root = TrieNode(0)
while (n > 0):
    n -= 1
    opt, arg = input().split()
    
    if opt[0] == 'a':
        addContact(root, arg)
    else:
        print(countContacts(root, arg))
# C++
"""
#include <iostream>
#include <string>
#define K 26
using namespace std;
typedef struct Node* ref;
struct Node {
	ref child[K];
	int count;
	Node() {
		for (int i = 0; i < K; i++)
			child[i] = NULL;
		count = 0;
	}
}* root;
void addContact(string& s) {
	ref p = root;
	for (int i = 0; i < s.length(); i++) {
		int c = s[i] - 'a';
		if (!p->child[c])
			p->child[c] = new Node;
		p = p->child[c];
		p->count++;
	}
}
int countContacts(string& s) {
	ref p = root;
	for (int i = 0; i < s.length(); i++) {
		int c = s[i] - 'a';
		if (!p->child[c])
			return 0;
		p = p->child[c];
	}
	return p->count;
}
int main() {
	int n;
	cin >> n;
	root = new Node;
	while (n--) {
		string opt, arg;
		cin >> opt >> arg;
		if (opt[0] == 'a')
			addContact(arg);
		else
			cout << countContacts(arg) << endl;
	}
	delete root;
}
"""
# JAVA
"""
import java.io.*;
import java.util.*;

class Node {
	static final int MAX = 26;
	public Node[] child;
	public int count;
	public Node() {
		child = new Node[MAX];
	}
}
class Trie {
	Node root;
	public Trie() {
		root = new Node();
	}
	public void add(String s) {
		Node p = root;
		for (int i = 0; i < s.length(); i++) {
			int next = s.charAt(i) - 'a';
			if (p.child[next] == null) {
				p.child[next] = new Node();
			}
			p = p.child[next];
			p.count++;
		}
	}
	public int find(String s) {
		Node p = root;
		int res = 0;
		for (int i = 0; i < s.length(); i++) {
			int next = s.charAt(i) - 'a';
			if (p.child[next] == null)
				return 0;
			p = p.child[next];
			res = p.count;
		}
		return res;
	}
}
class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		Trie trie = new Trie();
		while (n > 0) {
			n--;
			String type = sc.next();
			String s = sc.next();
			if (type.equals("add")) 
				trie.add(s);
			else
				System.out.println(trie.find(s));
		}
	}
}
"""

