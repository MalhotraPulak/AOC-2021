#include <fstream>
#include <iostream>
#include <vector>

int main() {
  std::ifstream fin;
  fin.open("input.txt");
  std::vector<int> nums;
  int current;
  while (fin >> current) {
    nums.push_back(current);
  }

  int prev = -1;
  int ans = 0;
  for (int i = 0; i < nums.size() - 2; i++) {
    int sum = nums[i] + nums[i + 1] + nums[i + 2];
    if (prev != -1 && sum > prev) {
      ans++;
    }
    prev = sum;
  }

  std::cout << ans << std::endl;
}
