n, t = map(int, input().split())
a = list(map(int, input().split()))
 
j = 0
read_books = max_books = 0
 
for i in range(n):
    while t < a[i]:
        t += a[j]
        j += 1
        read_books -= 1
 
    t -= a[i] 
    read_books += 1
    max_books = max(max_books, read_books) 
 
print(max_books)


# C++
"""
#include <iostream>
#include <vector>
using namespace std;
 
int main() {
    int n, t;
    cin >> n >> t;
    vector<int> a(n);
 
    int j = 0, max_book = 0, read_book = 0;
 
    for (int i = 0; i < n; i++) {
        cin >> a[i];
 
        while (t < a[i]) {
            t += a[j];
            j++;
            read_book--;
        }
         
        t -= a[i];
        read_book++;
        max_book = max(max_book, read_book);
    }
 
    cout << max_book;
    return 0;
}
"""

# java
"""
import java.util.Scanner;
import java.util.ArrayList;
 
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int t = sc.nextInt();
        ArrayList<Integer> a = new ArrayList<>();
 
        int j = 0, max_books = 0, read_books = 0; 
         
        for (int i = 0; i < n; i++) { 
            a.add(sc.nextInt());
 
            while (t < a.get(i)) { 
                t += a.get(j);
                j++;
                read_books--;
            }
 
            t -= a.get(i);
            read_books++;
            max_books = Math.max(max_books, read_books);
        }
 
        System.out.print(max_books);
    }
}

"""