#include <bits/stdc++.h>
using namespace std;

#define REP(i, n) for(int i = 0; i < (int)(n); i++)
#define UNIQUE(v) v.erase( unique(v.begin(), v.end()), v.end() );

// #include <algorithm> // std::equal
// #include <iterator>  // std::rbegin, std::rend
// ends_with("abc", "bc") == true
bool ends_with(const std::string& s, const std::string& suffix) {
   if (s.size() < suffix.size()) return false;
   return std::equal(std::rbegin(suffix), std::rend(suffix), std::rbegin(s));
}

int main()
{
    string s;
    cin >> s;

    vector<string> slist = {"dream", "dreamer", "erase", "eraser"};

    bool endsWith = true;
    while (endsWith) {
        endsWith = false;
        REP(i, 4) {
            if (ends_with(s, slist[i])) {
                s = s.substr(0, s.size() - slist[i].size());
                endsWith = true;
            }
        }
    }
    if (s.size() > 0) {
        cout << "NO" << endl;
    } else {
        cout << "YES" << endl;
    }

    return 0;
}