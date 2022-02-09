# python 3
import string
import sys
sys.setrecursionlimit(10000000)

class TrieNode:
    def __init__(self):
        self.count_leaf = 0
        self.child = dict()

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        cur = self.root
        for c in word:
            if c not in cur.child:
                cur.child[c] = TrieNode()
            cur = cur.child[c]
        cur.count_leaf += 1

def suffix_traversal(root, level, start_with):
    cnt = 1
    for c in root.child:
        if level > 0:
            start_with[c] += 1
        cnt += suffix_traversal(root.child[c], level + 1, start_with)
        
    return cnt

def prefix_traversal(root, level, suffix_state_count, start_with):
    res = 0
    if level > 0:
        res = suffix_state_count
    for c in root.child:
        if level > 0:
            res -= start_with[c]
        res += prefix_traversal(root.child[c], level + 1, suffix_state_count, start_with)
    
    return res


if __name__ == '__main__':
    while True:
        p, s = map(int, input().split())
        if p == s == 0:
            break

        suffix_trie = Trie()
        prefix_trie = Trie()

        for i in range(p):
            prefix_trie.add_word(input())

        for i in range(s):
            suffix_trie.add_word(input()[::-1])

        start_with = {c: 0 for c in string.ascii_lowercase}
        suffix_state_count = suffix_traversal(suffix_trie.root, 0, start_with) - 1
        print(prefix_traversal(prefix_trie.root, 0, suffix_state_count, start_with))
# C++
"""
#include <iostream>
#include <string>
#include <cstdio>
#include <algorithm>
using namespace std;

const int MAX = 26;

struct node{
	struct node *child[MAX];
	int countLeaf;
};

struct node *newNode(){
	struct node *newNode = new struct node;
	newNode->countLeaf = 0;
	for (int i = 0; i < MAX; i++)
		newNode->child[i] = NULL;
	return newNode;
}

void addword(struct node *root, string s){
	int ch;
	struct node *temp = root;
	for (int i = 0; i < s.size(); i++){
		ch = s[i] - 'a';
		if (temp->child[ch] == NULL)
			temp->child[ch] = newNode();
		temp = temp->child[ch];
	}
	temp->countLeaf++;
}

long long startWith[26];
long long suffixStateCount;

void suffixTraversal(node* pNode, int level){
	suffixStateCount++;
	for (int i = 0; i < 26; i++){
		if (!pNode->child[i])
			continue;
		if (level > 0) startWith[i]++;
		suffixTraversal(pNode->child[i], level + 1);
	}
}

long long prefixTraversal(node* pNode, int level){
	long long result = 0;
	if (level > 0) result += suffixStateCount;
	for (int i = 0; i < 26; i++){
		if (!pNode->child[i])
			continue;
		if (level > 0)
			result -= startWith[i];
		result += prefixTraversal(pNode->child[i], level+1);
	}
	return result;
}

void clearTree(node *pNode)
{
	for (int i = 0; i < MAX; i++)
	{
		if (pNode->child[i])
		{
			clearTree(pNode->child[i]);
			delete pNode->child[i];
		}
	}
}

int main(){
	// freopen("test.in", "rt", stdin);
	ios::sync_with_stdio(false);

	node *suffixTrie, *prefixTrie;
	int p, s;
	string str;

	while (1){
		cin >> p >> s;
		if (!p && !s)
			break;

		suffixTrie = newNode();
		prefixTrie = newNode();
		for (int i = 0; i < 26; i++)
			startWith[i] = 0;
		suffixStateCount = 0;

		for (int i = 0; i < p; i++){
			cin >> str;
			addword(prefixTrie, str);
		}
		for (int i = 0; i < s; i++){
			cin >> str;
			reverse(str.begin(), str.end());
			addword(suffixTrie, str);
		}
		suffixTraversal(suffixTrie, 0);
		suffixStateCount--;
		cout << prefixTraversal(prefixTrie, 0) << "\n";
	}

	return 0;
}
"""
# JAVA
"""
import java.util.*;
import java.io.*;


class Main
{ 
    static PrintWriter out;
    static final int MAX =26;
    static int suffixStateCount = 0;
    static int startWith[] = new int[MAX];    
    
    
    public static class node{

        public node() {
        }
        public node[] child = new node[MAX];
        public int countLeaf;
    }
    
    public static class Trie{

        public Trie() {
            root = NewNode();
        }
        public node root;
        
        public node NewNode(){
            node newNode = new node();
            newNode.countLeaf = 0;
            for(int i = 0 ; i < MAX;i++){
                newNode.child[i] = null;
            }
            return newNode;
        }
        
        public void AddWord(String s){
            int ch;
            node temp = root;
            for(int i = 0 ; i < s.length(); i++){
                ch = s.charAt(i) - 'a';
                if(temp.child[ch] == null)
                    temp.child[ch] = NewNode();
                temp = temp.child[ch];
            }
            temp.countLeaf++;
        }
        
    }
    
    public static void suffixTraversal(node pNode, int level){
        suffixStateCount++;
        for (int i = 0; i < 26; i++){
            if (pNode.child[i]==null)
                    continue;
            if (level > 0) startWith[i]++;
            suffixTraversal(pNode.child[i], level + 1);
        }
    }
    
    
    static long prefixTraversal(node pNode, int level) {
        long result = 0;
        if (level > 0) result += suffixStateCount;
        for (int i = 0; i < 26; i++) {
            if (pNode.child[i] == null)
                continue;
            if (level > 0)
                result -= startWith[i];
            result += prefixTraversal(pNode.child[i], level + 1);
        }
        return result;
    }

    public static void main(String[] args) {
        MyScanner in = new MyScanner();
        out = new PrintWriter(new BufferedOutputStream(System.out), true);
        int p = 0 ,s = 0;
        String str;
        while(true){
            p = in.nextInt();
            s = in.nextInt();
            if(p==0 && s ==0){
                break;
            }
            Trie suffixTrie = new Trie();
            Trie prefixTrie = new Trie();
            
            for(int i = 0 ; i < 26 ;i++){
                startWith[i] = 0;
            }
            
            suffixStateCount = 0;
            
            for(int i = 0 ; i < p ; i++){
                str = in.next();
                prefixTrie.AddWord(str);
            }
            
            for(int i = 0 ;i < s;i++){
                str = in.next();
                String reverse = new StringBuffer(str).reverse().toString();
                suffixTrie.AddWord(reverse);
            }
            
            suffixTraversal(suffixTrie.root, 0);
            suffixStateCount--;
            long ans = prefixTraversal(prefixTrie.root, 0);
            out.println(ans);
        }
    }
    
    public static class MyScanner {
        BufferedReader br;
        StringTokenizer st;

        public MyScanner() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }
        String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                        st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                        e.printStackTrace();
                }
            }
            return st.nextToken();
        }
        int nextInt() {
                return Integer.parseInt(next());
        }
        long nextLong() {
                return Long.parseLong(next());
        }
        double nextDouble() {
                return Double.parseDouble(next());
        }
        String nextLine() {
            String str = "";
            try {
                str = br.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }
    }
}
"""

