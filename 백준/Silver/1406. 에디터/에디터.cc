// 1406
#include <bits/stdc++.h>
using namespace std;

int main() {
  string s = ""; // 시작 문자
  int m;
  stack<char> left;  // 왼쪽 스택
  stack<char> right; // 오른쪽 스택

  cin >> s;
  cin >> m;

  // 문자열 스택 초기화
  for (int a = 0; a < (int)s.size(); a++) {
    left.push(s[a]);
  }
  // 탐색 시작
  char order, c;
  for (int i = 0; i < m; i++) {
    cin >> order;
    if (order == 'L') {
      if (!left.empty()) {
        right.push(left.top());
        left.pop();
      }
    } else if (order == 'D') {
      if (!right.empty()) {
        left.push(right.top());
        right.pop();
      }
    } else if (order == 'B') {
      if (!left.empty())
        left.pop();
    } else {
      cin >> c;
      left.push(c);
    }
  }

  // 스택 안의 문자들 합치기
  // 1. 왼쪽 스택 문자들 전부 오른쪽으로 이동
  while (!left.empty()) {
    right.push(left.top());
    left.pop();
  }
  // 2. 오른쪽 스택에서 출력
  while (!right.empty()) {
    cout << right.top();
    right.pop();
  }
}