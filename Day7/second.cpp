#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <vector>

std::vector<int> comma_sep(std::string str) {
  std::vector<int> vect;

  std::stringstream ss(str);

  for (int i; ss >> i;) {
    vect.push_back(i);
    if (ss.peek() == ',')
      ss.ignore();
  }

  return vect;
}

void print_vec(std::vector<int> &v) {
  std::cout << "vector size" << v.size() << std::endl;
  for (int x : v) {
    std::cout << x << " ";
  }
  std::cout << "\n";
}


int get_sum(std::vector <int> &v, int mid) {
  int total = 0;
  for (int x: v) {
      total += abs(x - mid) * (abs(x - mid) + 1) / 2; 
  }
  return total;
}

int main(int argc, char *argv[]) {
  std::ifstream fin;
  fin.open(argv[1]);
  std::string str;
  fin >> str;
  auto nums = comma_sep(str);
  sort(nums.begin(), nums.end());
  int total = nums.size(); 
  int ans = INT_MAX; 
  
  int l = 0, r = nums[nums.size() - 1];

  while (l < r) {
    int mid = (l + r)/2;
    if (get_sum(nums, mid) > get_sum(nums, mid + 1)) {
      l = ans = mid + 1;
    } else {
      r = ans = mid;
    }

  }
  

  std::cout << get_sum(nums, ans) << std::endl;


}
