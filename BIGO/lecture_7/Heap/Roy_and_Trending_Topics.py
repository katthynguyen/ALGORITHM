# python 3
import queue

class Topic:
    def __init__(self, _id, _old_score, _new_score):
        self.id = _id
        self.old_score = _old_score
        self.new_score = _new_score
        self.change = self.new_score - self.old_score
    
    def __lt__(self, other):
        return self.change > other.change or (self.change == other.change and self.id > other.id)

n = int(input())
pq = queue.PriorityQueue()

for _ in range(n):
    id, old_score, post, like, comment, share = map(int, input().split())
    new_score = post * 50 + like * 5 + comment * 10 + share * 20
    pq.put(Topic(id, old_score, new_score))

for i in range(5):
    t = pq.get()
    print(t.id, t.new_score)
#  C++
"""
#include <iostream>
#include <queue>
using namespace std;

struct Topic {
    int id;
    long long old_score, new_score, change;

    Topic(int _id, long long _old_score, long long _new_score) {
        id = _id;
        old_score = _old_score;
        new_score = _new_score;
        change = new_score - old_score;
    }

    bool operator<(const Topic &other) const {
        return change < other.change || (change == other.change && id < other.id);
    }
};

int main() {
    int n;
    cin >> n;
    int id;
    long long old_score, new_score, post, like, comment, share;
    priority_queue<Topic> pq;

    while (n--) {
        cin >> id >> old_score >> post >> like >> comment >> share;
        new_score = post * 50 + like * 5 + comment * 10 + share * 20;
        pq.push(Topic(id, old_score, new_score));
    }

    for (int i = 0; i < 5; i++) {
        Topic t = pq.top();
        pq.pop();
        cout << t.id << " " << t.new_score << endl;
    }
    return 0;
}
"""
# JAVA

"""
import java.util.*;
import java.io.*;

public class Solution {
    static class Topic {
        int id;
        long old_score, new_score, change;

        public Topic(int _id, long _old_score, long _new_score) {
            id = _id;
            old_score = _old_score;
            new_score = _new_score;
            change = new_score - old_score;
        }
    };

    public static void main(String[] agrs) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        PriorityQueue<Topic> pq = new PriorityQueue<>(new Comparator<Topic>() {
            public int compare(Topic a, Topic b) {
                if (a.change < b.change || (a.change == b.change && a.id < b.id)) {
                    return 1;
                }
                else {
                    return -1;
                }
            }
        });

        for (int k = 0; k < n; k++) {
            int id = sc.nextInt();
            long old_score = sc.nextLong();
            long post = sc.nextLong(),          like = sc.nextLong();
            long comment = sc.nextLong(),       share = sc.nextLong();
            long new_score = post * 50 + like * 5 + comment * 10 + share * 20;
            pq.add(new Topic(id, old_score, new_score));
        }

        for (int i = 0; i < 5; i++) {
            Topic t = pq.poll();
            System.out.println(t.id + " " + t.new_score);
        }
    }
}
"""