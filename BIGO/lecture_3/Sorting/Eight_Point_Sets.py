#  python3 
fre_x = [False] * (10 ** 6 + 5)
fre_y = [False] * (10 ** 6 + 5)
unique_x = []
unique_y = []
points = []

for _ in range(8):
    x, y = map(int, input().split())
    points.append((x, y))

    if not fre_x[x]:
        fre_x[x] = True
        unique_x.append(x)
    
    if not fre_y[y]:
        fre_y[y] = True
        unique_y.append(y)

if len(unique_x) != 3 or len(unique_y) != 3:
    print('ugly')
    exit()

unique_x.sort()
unique_y.sort()
points.sort()
index = 0

for i in range(3):
    for j in range(3):
        if i == j == 1:
            continue
        if unique_x[i] == points[index][0] and unique_y[j] == points[index][1]:
            index += 1
        else:
            print('ugly')
            exit()

print('respectable')
#  C++

"""
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
const int MAX = 1e6 + 5;

struct Point {
    int x, y;
    bool operator<(const Point& another) {
        return (x < another.x || (x == another.x && y < another.y));
    }
};

bool fre_x[MAX], fre_y[MAX];

int main() {
    int x, y;
    vector<int> unique_x, unique_y;
    vector<Point> points;

    for (int i = 0; i < 8; i++) {
        cin >> x >> y;
        points.push_back({x, y});

        if (!fre_x[x]) {
            fre_x[x] = true;
            unique_x.push_back(x);
        }

        if (!fre_y[y]) {
            fre_y[y] = true;
            unique_y.push_back(y);
        }
    }

    if (unique_x.size() != 3 || unique_y.size() != 3) {
        cout << "ugly";
        return 0;
    }

    sort(unique_x.begin(), unique_x.end());
    sort(unique_y.begin(), unique_y.end());
    sort(points.begin(), points.end());
    int index = 0;

    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (i == j && i == 1) {
                continue;
            }
            if (unique_x[i] == points[index].x && unique_y[j] == points[index].y) {
                index++;
            }
            else {
                cout << "ugly";
                return 0;
            }
        }
    }

    cout << "respectable";
    return 0;
}
"""

#  JAVA

"""
import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;

public class Main {
    static final int MAX = (int)1e6 + 5;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<Point> points = new ArrayList<>();
        ArrayList<Integer> unique_x = new ArrayList<>(), unique_y = new ArrayList<>();
        boolean[] fre_x = new boolean[MAX], fre_y = new boolean[MAX]; 

        for (int i = 0; i < 8; i++) {
            int x = sc.nextInt(), y = sc.nextInt();
            points.add(new Point(x, y));

            if (!fre_x[x]) {
                fre_x[x] = true;
                unique_x.add(x);
            }

            if (!fre_y[y]) {
                fre_y[y] = true;
                unique_y.add(y);
            }
        }

        if (unique_x.size() != 3 || unique_y.size() != 3) {
            System.out.print("ugly");
            return;
        }

        Collections.sort(unique_x);
        Collections.sort(unique_y);
        Collections.sort(points);
        int index = 0;

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (i == j && i == 1) {
                    continue;
                }

                int x = points.get(index).x;
                int y = points.get(index).y;
                if (unique_x.get(i) == x && unique_y.get(j) == y) {
                    index++;
                }
                else {
                    System.out.print("ugly");
                    return;
                }
            }
        }

        System.out.print("respectable");
    }
}

class Point implements Comparable<Point> {
    Integer x, y;

    public Point(int _x, int _y) {
        this.x = _x;
        this.y = _y;
    }
    
    @Override
    public int compareTo(Point another) {
        if (this.x.equals(another.x)) {
            return this.y.compareTo(another.y);
        }
        return this.x.compareTo(another.x);
    }
}
"""