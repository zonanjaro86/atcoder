#include <bits/stdc++.h>
using namespace std;

#define REP(i, n) for(int i = 0; i < (int)(n); i++)
#define UNIQUE(v) v.erase( unique(v.begin(), v.end()), v.end() );

int main()
{
    int n, y;
    cin >> n >> y;

    REP(i, n+1) {
        REP(j, n-i+1) {
            int k = n-i-j;
            int money = 10000 * i + 5000 * j + 1000 * k;
            if (money == y) {
                cout << i << ' ' << j << ' ' << k << endl;
                return 0;
            }
        }
    }
    cout << "-1 -1 -1" << endl;

    return 0;
}