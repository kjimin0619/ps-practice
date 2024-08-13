// 10828
#include <bits/stdc++.h>
using namespace std;

int main() {
  int n;
  cin >> n;
  stack<int> s = {};

  for (int i = 0; i < n; i++) {
    string c;
    cin >> c;
    // stack 
    if (c == "pop") {
      if (s.size() != 0) {
        cout << s.top() << '\n';
        s.pop();
      } else {
        cout << -1 << '\n';
      }
    } else if (c == "size") {
      cout << s.size() << '\n';
    } else if (c == "empty") {
      cout << s.empty() << '\n';
    } else if (c == "top") {
      if (s.size()) {
        cout << s.top() << '\n';
      } else {
        cout << -1 << '\n';
      }
    } else {
      // push
      int temp = 0;
      cin >> temp;
      s.push(temp);
    }
  }
}