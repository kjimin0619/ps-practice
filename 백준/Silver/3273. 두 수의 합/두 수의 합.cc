#include <algorithm>
#include <bits/stdc++.h>
#include <iostream>

using namespace std;

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);

  int n, x;
  int nums[100001] = {0};
  cin >> n;
  for (int i = 0; i < n; i++)
    cin >> nums[i];
  cin >> x;

  sort(nums, nums + n);
  int count = 0;
  int st = 0;
  int end = n - 1;
  while (st < end) {
    if (nums[st] + nums[end] == x) {
      count++;
      st++;
      end--;
    } else if (nums[st] + nums[end] > x) {
      end--;
    } else {
      st++;
    }
  }
  cout << count;
}
