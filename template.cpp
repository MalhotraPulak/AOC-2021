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
}
