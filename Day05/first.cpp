#include <fstream>
#include <iostream>
#include <map>
#include <vector>

int main() {
  std::ifstream fin;
  fin.open("input.txt");

  std::map<std::pair<int, int>, int> m;
  for(int k = 0; k <  500; k++) {
    int x1, y1, x2, y2;
    char comma;
    fin >> x1;
    fin >> comma;
    assert(comma == ',' && "first comma");
    fin >> y1;
    fin >> comma;
    // assert(comma == '-' && "-");
    fin >> comma;
    // assert(comma == '>' && ">");
    fin >> x2;
    fin >> comma;
    assert(comma == ',' && "second comma");
    fin >> y2;
    // std::cout << x1 << y1 << " " << x2 << y2 << std::endl;  

    if (x1 != x2 && y1 != y2)
      continue;
     
    int x_min = std::min(x1, x2);
    int x_max = std::max(x1, x2);
    int y_min = std::min(y1, y2);
    int y_max = std::max(y1, y2);

    std::cout << x1 << ":"<< y1 << " " << x2 << ":" << y2 << std::endl;
    if (x1 == x2) {
      for (int i = y_min; i <= y_max; i++) {
        m[{x1, i}] += 1;
      } 
    } else {
      for (int i = x_min; i <= x_max; i++) {
        m[{i, y1}] += 1;
      } 
    }

    //std::cout << "done" << x1 << " " << y1 << std::endl;
  }
  int ans = 0;
  for (auto &[k, v]: m){
    if (v >= 2) {
      ans++;
    }
  }
  std::cout << ans << std::endl;
}
