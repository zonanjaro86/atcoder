#include<iostream>

using namespace std;
int main()
{
    int a, b, c, x;
    cin >> a >> b >> c >> x;

    // 500 * a, 100 * b, 50 * c

    int cnt = 0;
    for (int i = 0; i <= a; i++) {
        for (int j = 0; j <= b; j++ ) {
            int sum = 500 * i + 100 * j;
            int k = (x - sum) / 50;
            if (k >= 0 && k <= c) {
                cnt++;
            }
        }
    }
    cout << cnt << endl;

    return 0;
}