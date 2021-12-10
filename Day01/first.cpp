#include <fstream>
#include <iostream>

int main() {
  std::ifstream fin;
  fin.open("input.txt");
  int prev = -1;
  int current = 0;
  int ans = 0;
  while (fin >> current) {
    if (prev != -1 && current > prev) {
      ans++;
    }
    prev = current;
  }
  std::cout << ans << std::endl;
}
