#include <fstream>
#include <iostream>
#include <vector>

int rating(int to_keep, std::vector<int> nums, int bits) {

  for (int i = 0; i < bits; i++) {
    int j = bits - i - 1;
    int zeros = 0, ones = 0;
    for (int num : nums) {
      if ((num >> j) & 1) {
        ones++;
      } else {
        zeros++;
      }
    }
    int keep = 0;
    if (ones >= zeros) {
      keep = to_keep;
    } else {
      keep = 1 - to_keep;
    }

    std::vector<int> new_nums;

    for (int num : nums) {
      if (((num >> j) & 1) == keep) {
        new_nums.push_back(num);
      }
    }

    if (new_nums.size() == 1) {
      return new_nums[0];
    }

    nums = new_nums;
  }

  return nums[0];
}

int main() {
  std::ifstream fin;
  fin.open("input.txt");
  std::string current;
  std::vector<int> nums;
  int bits = 0;
  while (fin >> current) {
    bits = current.size();
    nums.push_back(stoi(current, nullptr, 2));
  }
  int gamma = 0;
  for (int i = 0; i < bits; i++) {
    int zeros = 0, ones = 0;
    for (int num : nums) {
      if ((num >> i) & 1) {
        ones++;
      } else {
        zeros++;
      }
    }
    if (ones >= zeros) {
      gamma += (1 << i);
    }
  }
  int eps = ((1 << bits) - 1) ^ gamma;
  std::cout << eps << " " << gamma << std::endl;
  std::cout << eps * gamma << std::endl;
}
