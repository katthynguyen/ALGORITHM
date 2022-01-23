#  python 3
n, x = map(int, input().split())
c = list(map(int, input().split()))
c.sort()
min_time = 0

for chapters in c:
    min_time += chapters * x
    if x > 1:
        x -= 1
        
print(min_time)

#  C++
"""
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int n, x;
	cin >> n >> x;
	vector<int> c(n);
	
	for (int i = 0; i < n; i++) {
		cin >> c[i];
	}
	
	sort(c.begin(), c.end());
	
	long long min_time = 0;
	
	for (int chapters : c) {
		min_time += 1LL * chapters * x;
		if (x > 1) {
			x--;
		}
	}
	
	cout << min_time;
	return 0;
}
"""

#  JAVA
"""
import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int x = sc.nextInt();
		ArrayList<Integer> c = new ArrayList<>();
		for (int i = 0; i < n; i++) {
			c.add(sc.nextInt());
		}
		
		Collections.sort(c);
		
		long min_time = 0;
		
		for (int chapters : c) {
			min_time += 1L * chapters * x;
			if (x > 1) {
				x--;
			}
		}
		
		System.out.print(min_time);
	}
}
"""
