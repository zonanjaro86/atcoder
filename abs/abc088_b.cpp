#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for(int i = 0; i < (int)(n); i++)

int main()
{
    int n;
    cin >> n;
    int a[n];
    rep(i, n) {
        cin >> a[i];
    }

    sort(a, a+n, greater<int>());

    int sum_a = 0, sum_b = 0;
    rep(i, n) {
        if (i % 2 == 0) {
            sum_a += a[i];
        } else {
            sum_b += a[i];
        }
    }

    cout << sum_a - sum_b << endl;

    return 0;
}