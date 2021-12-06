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
  std::string nums;
  fin >> nums;
  auto starting = comma_sep(nums);
  std::map<int, int> m;
  for (int x : starting) {
    m[x] += 1;
  }
  int ans = 0;
  for (auto &[k, v] : m) {
    std::vector<int> pop;
    pop.push_back(k);
    for (int i = 1; i <= 80; i++) {

      int size = pop.size();
      for (int i = 0; i < size; i++) {
        if (pop[i] > 0) {
          pop[i] -= 1;
        } else {
          pop[i] = 6;
          pop.push_back(8);
        }
      }
      // std::cout << "After day " << i << std::endl;
      // print_vec(pop);
    }
    ans += pop.size() * v;
  }

  std::cout << ans << std::endl;
}
