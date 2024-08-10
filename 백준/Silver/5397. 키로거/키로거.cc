// 5397
#include <bits/stdc++.h>
using namespace std;

int main() {
  int tc;
  cin >> tc; // 테스트케이스 개수

  for (int z = 0; z < tc; z++) {
    list<char> passwords = {};
    auto ptr = passwords.begin();

    string s;
    cin >> s;

    for (auto c : s) {
      if (c == '<') {
        if (ptr != passwords.begin())
          ptr--;
      } else if (c == '>') {
        if (ptr != passwords.end())
          ptr++;
      } else if (c == '-') {
        if (ptr != passwords.begin()) {
          ptr--;
          ptr = passwords.erase(ptr);
        }

      } else {
        passwords.insert(ptr, c);
      }
    }
    // 출력
    for (auto c : passwords) {
      cout << c;
    }
    cout << '\n';
  }
}