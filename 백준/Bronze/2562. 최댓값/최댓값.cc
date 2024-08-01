#include <iostream>

using namespace std;

int main() {
  int m, idx, temp;
  m = 1;
  for (int i = 0; i < 9; i++) {
    cin >> temp;
    if (temp > m) {
      m = temp;
      idx = i + 1;
    }
  }

  cout << m << '\n' << idx;

  return 0;
}