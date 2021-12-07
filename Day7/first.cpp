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

  for (std::size_t i = 0; i < vect.size(); i++)
    std::cout << vect[i] << std::endl;

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
  
  for(int i = 1; i < nums.size() - 1; i++) {
    int center = nums[i];
    int no_left = i;
    int no_right = total - i - 1;
    int cost_left = no_left * center - cost_pre[i - 1];
    int cost_right = cost_suff[i + 1] - no_right * center;
    ans = std::min(ans, cost_left + cost_right); 
  }

  std::cout << ans << std::endl;


}
