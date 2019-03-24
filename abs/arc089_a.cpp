#include <bits/stdc++.h>
using namespace std;

#define REP(i, n) for(int i = 0; i < (int)(n); i++)
#define UNIQUE(v) v.erase( unique(v.begin(), v.end()), v.end() );

int main()
{
    int n;
    cin >> n;
    int t[n+1], x[n+1], y[n+1];
    t[0] = 0;
    x[0] = 0;
    y[0] = 0;
    REP(i, n) {
        cin >> t[i+1] >> x[i+1] >> y[i+1];
    }

    REP(i, n) {
        int time = t[i+1] - t[i];
        int x_len = x[i+1] - x[i];
        int y_len = y[i+1] - y[i];
        int diff = time - x_len - y_len;
        if (diff < 0 || diff % 2 != 0) {
            cout << "No" << endl;
            return 0;
        }
    }
    cout << "Yes" << endl;

    return 0;
}