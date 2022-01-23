# Python3
n, m, x, y = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
v = []
i = j = 0

while i < n and j < m:
   if a[i] - x <= b[j] <= a[i] + y:
      v.append((i + 1, j + 1))
      i += 1
      j += 1
   elif a[i] + y < b[j]:
      i += 1
   elif a[i] - x > b[j]:
      j += 1

print(len(v))
for vest in v:
    print(vest[0], vest[1])

# c++

"""
#include <iostream>
#include <vector>
using namespace std;

struct Vest {
	int u, v;
};

int main() {
	int n, m, x, y;
	cin >> n >> m >> x >> y;
	vector<int> a(n), b(m);

	for (int i = 0; i < n; i++) {
		cin >> a[i];
	}
	
	for (int i = 0; i < m; i++) {
		cin >> b[i];
	}

	vector<Vest> v;
   int i = 0, j = 0;
   
   while (i < n && j < m) {
      if (a[i] - x <= b[j] & b[j] <= a[i] + y) {
         v.push_back({i + 1, j + 1});
         i++;
         j++;
      }
      else if (a[i] + y < b[j]) {
         i++;
      }
      else if (a[i] - x > b[j]) {
         j++;
      }
   }

	cout << v.size() << endl;
	for (Vest &vest : v) {
		cout << vest.u << " " << vest.v << endl;
	}

	return 0;
}
"""

#  Java
"""
import java.util.Scanner;
import java.util.ArrayList;

public class Main {
   static class Vest {
      int u, v;

      public Vest(int x , int y) {
         u = x;
         v = y; 
      }
   }

   public static void main (String[] args) {
      Scanner sc = new Scanner(System.in); 
      int n = sc.nextInt(); 
      int m = sc.nextInt(); 
      int x = sc.nextInt(); 
      int y = sc.nextInt(); 

      ArrayList<Integer> a = new ArrayList<>(), b = new ArrayList<>();

      for (int i = 0; i < n; i++) {
         a.add(sc.nextInt());
      }

      for (int i = 0; i < m; i++) {
         b.add(sc.nextInt()); 
      }

      ArrayList<Vest> v = new ArrayList<>();  

      int i = 0, j = 0;
      while (i < n && j < m) {
         if (a.get(i) - x <= b.get(j) && b.get(j) <= a.get(i) + y) {
            v.add(new Vest(i + 1, j + 1));
            i++;
            j++;
         }
         else if (a.get(i) + y < b.get(j)) {
            i++;
         }
         else if (a.get(i) - x > b.get(j)) {
            j++;
         }
      }

      System.out.println(v.size()); 

      for (Vest vest : v) {
         System.out.println(vest.u + " " + vest.v);
      }
   }
}
"""