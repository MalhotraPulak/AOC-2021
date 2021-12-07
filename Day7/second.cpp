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

int main(int argc, char *argv[]) {
  std::ifstream fin;
  fin.open(argv[1]);
  std::string str;
  fin >> str;
  auto nums = comma_sep(str);
  sort(nums.begin(), nums.end());
  int total = nums.size(); 
  std::vector <int> cost_pre(total, nums[0]);
  std::vector <int> cost_suff(total, nums[nums.size() - 1]);
  for(int i = 1; i < nums.size(); i++) {
    cost_pre[i] = cost_pre[i - 1] + nums[i]; 
  }
  for(int i = nums.size() - 2; i >= 0; i--) {
    cost_suff[i] = cost_suff[i + 1] + nums[i]; 
  }
  int ans = INT_MAX; 
  
  for(int i = nums[0]; i <= nums[nums.size() - 1]; i++) {
    int center = i;
    int cost = 0;
    for(int j = 0; j < nums.size(); j++){
      int dist = abs(nums[j] - center);
      cost += dist * (dist + 1) / 2;
    }
    ans = std::min(ans, cost);
  }

  std::cout << ans << std::endl;


}
