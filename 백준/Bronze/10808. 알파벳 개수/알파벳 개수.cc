// 10808
#include <iostream>
using namespace std;

int main() {
  string s;
  cin >> s;

  int count[26] = {0}; // 초기화 0

  for (int i = 0; i < s.size(); i++) {
    count[s[i] - 'a']++;
  }

  for (int i = 0; i < 26; i++) {
    cout << count[i] << ' ';
  }

  return 0;
}