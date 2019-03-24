#include<iostream>
using namespace std;
int main()
{
    char s[3];
    cin >> s[0] >> s[1] >> s[2];

    int cnt = 0;
    for (int i = 0; i < 3; i++) {
        if (s[i] == '1') {
            cnt++;
        }
    }
    cout << cnt << endl;
    return 0;
}