#include <bits/stdc++.h>
using namespace std;

int main() {
  int n;
  cin >> n;

  int nums[10] = {0};
  while (n > 0) {
    nums[n % 10]++;
    n = n / 10;
  }
  // 6 & 9
  nums[6] = (nums[6] + nums[9] + 1) / 2;
  nums[9] = (nums[6] + nums[9] + 1) / 2;

  cout << *max_element(nums, nums + 9);
}