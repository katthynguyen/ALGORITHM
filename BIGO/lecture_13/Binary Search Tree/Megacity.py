# python 3
import math
 
def solve():
    numLocation, totalPeople = map(int, input().split())
    location = dict()
    for i in range(numLocation):
        x, y, people = map(int, input().split())
        r = x * x + y * y
        if r in location:
            location[r] += people
        else:
            location[r] = people
    radius = []
    for r in location:
        radius.append(r)
    radius.sort()
    for r in radius:
        totalPeople += location[r]
        if totalPeople >= 1000000:
            print(math.sqrt(r))
            return
    print("-1")
     
solve()
# C++
"""
#include <iostream>
#include <iomanip>
#include <cmath>
#include <map>
using namespace std;
 
int main() {
    int numLocation, totalPeople, people;
    double x, y;
    cin >> numLocation >> totalPeople;
    map<double, int> location;
    for (int i = 0; i < numLocation; ++ i) {
        cin >> x >> y;
        cin >> people;
        /*
        Tính bán kính của đường tròn, do tâm thành phố là (0, 0) 
        nên để tính bán kính thì chỉ cần công thức bên dưới là đủ 
        thay cho công thức sqrt((x1-x0)*(x1-x0) + (y1-y0)*(y1-y0))
        */
        double r = x * x + y * y;
        if (location.find(r) != location.end()) 
            location[r] += people;
        else
            location[r] = people;
    }
    for (map<double, int>::iterator it = location.begin(); it != location.end(); ++it) {
        totalPeople += it->second;
        if (totalPeople >= 1000000) {
            cout << fixed << setprecision(6) << sqrt(it->first) << endl;
            return 0;
        }
    }
    cout << "-1" << endl;
    return 0;
}
"""
# JAVA
"""
import java.util.*;
 
public class Main {
    public static void main(String[] args) {
        Scanner in= new Scanner(System.in);
        int numLocation, totalPeople, people;
        double x, y;
        numLocation = in.nextInt();
        totalPeople = in.nextInt();
        Map<Double, Integer> location = new TreeMap<>();
        for (int i = 0; i < numLocation; ++ i) {
            x = in.nextDouble();
            y = in.nextDouble();
            people = in.nextInt();
            double r = x * x + y * y;
            if (location.containsKey(r)) 
                location.put(r, location.get(r) + people);
            else
                location.put(r, people);
        }
        for (Double r : location.keySet()) {
            totalPeople += location.get(r);
            if (totalPeople >= 1000000) {
                System.out.printf("%.6f\n", Math.sqrt(r));
                return;
            }
        }
        System.out.print("-1\n");
    }
}
"""

