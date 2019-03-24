#include <bits/stdc++.h>
using namespace std;

#define REP(i, n) for(int i = 0; i < (int)(n); i++)
#define UNIQUE(v) v.erase( unique(v.begin(), v.end()), v.end() );

int main()
{
    int n;
    cin >> n;
    vector<int> d(n);
    REP(i,n) cin >> d[i];

    sort(d.begin(), d.end());
    UNIQUE(d);

    cout << d.size() << endl;

    return 0;
}