#include <bits/stdc++.h>
using namespace std;

// #include <algorithm> // std::equal
// #include <iterator>  // std::rbegin, std::rend
// ends_with("abc", "bc") == true
bool ends_with(const std::string& s, const std::string& suffix) {
   if (s.size() < suffix.size()) return false;
   return std::equal(std::rbegin(suffix), std::rend(suffix), std::rbegin(s));
}