#include<iostream>
using namespace std;
int main()
{
    int n;
    cin >> n;

    int a[n];
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    int cnt = 0;
    bool isEven = true;
    while(isEven) {
        for (int i = 0; i < n; i++) {
            if (a[i] % 2 == 0) {
                a[i] /= 2;
            } else {
                isEven = false;
                break;
            }
        }
        if (isEven) {
            cnt++;
        }
    }
    cout << cnt << endl;

    return 0;
}