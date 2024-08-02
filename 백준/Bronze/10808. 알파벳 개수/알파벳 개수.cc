// 10808
#include <iostream>
using namespace std;

int main() {
  string s;
  cin >> s;

  int count[26] = {0}; // 초기화 0

  for (auto temp : s) {
    count[temp - 'a']++;
  }

  for (auto cnt : count) {
    cout << cnt << ' ';
  }

  return 0;
}