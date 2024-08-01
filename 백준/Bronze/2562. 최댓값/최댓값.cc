#include <algorithm>
#include <iostream>

using namespace std;

int a[9];
int main() {
  for (int i = 0; i < 9; i++)
    cin >> a[i];

  cout << *max_element(a, a + 9) << '\n'; // value
  cout << max_element(a, a + 9) - a + 1;  // index
}