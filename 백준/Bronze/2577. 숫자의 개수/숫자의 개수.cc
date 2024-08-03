// 2577
#include <iostream>

using namespace std;

int main() {
  int a, b, c, m;

  cin >> a >> b >> c;

  m = a * b * c;
  int count[10] = {0};
  while (m > 0) {
    count[m % 10]++;
    m = m / 10;
  }
  for (auto i : count)
    cout << i << '\n';
}