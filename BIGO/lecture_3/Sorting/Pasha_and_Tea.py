# python3
n, w = map(int, input().split())
cups = list(map(int, input().split()))
cups.sort()

m = min(cups[0], cups[n] / 2)
total = 3 * m * n
print(min(total, w))
# C++
"""
#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>
using namespace std;

int main() {
	int n, w;
	cin >> n >> w;
	vector<int> cups(n * 2);
	
	for (int i = 0; i < n * 2; i++) {
		cin >> cups[i];
	}
	
	sort(cups.begin(), cups.end());

	double m = min(1.0 * cups[0], 1.0 * cups[n] / 2);
	double total = 3 * m * n;
	cout << setprecision(9) << min(total, 1.0 * w);
	return 0;
}

"""
# JAVA
"""
import java.util.Scanner;
import java.util.ArrayList;
import java.lang.Math;
import java.util.Collections;

public class Main {
	public static void main(String[] agrs) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt(), w = sc.nextInt();
		ArrayList<Integer> cups = new ArrayList<>();
		
		for (int i = 0; i < n * 2; i++) {
			cups.add(sc.nextInt());
		}
		
		Collections.sort(cups);
		
		double m = Math.min(1.0 * cups.get(0), 1.0 * cups.get(n) / 2);
		double max_amount = 3 * m * n;
		System.out.print(Math.min(max_amount, w));
	}
}
"""