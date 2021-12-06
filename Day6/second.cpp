#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <vector>

#define int long long
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

signed main(signed argc, char *argv[]) {
  std::ifstream fin;
  fin.open(argv[1]);
  std::string nums;
  fin >> nums;
  auto starting = comma_sep(nums);
  std::map<int, int> m;
  for (int x : starting) {
    m[x] += 1;
  }
  for (int i = 1; i <= 256; i++) {
    std::map<int, int> m2;
    for (auto &[k, v] : m) {
      if (k == 0) {
        m2[6] += v;
        m2[8] += v;
      } else {
        m2[k - 1] += v;
      }
    }
    m = m2;
  }
  int ans = 0;
  for (auto &[k, v] : m) {
    ans += v;
  }
  std::cout << ans << std::endl;
}
