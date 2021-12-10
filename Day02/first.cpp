#include <fstream>
#include <iostream>

int main() {
  std::ifstream fin;
  fin.open("input.txt");
  int depth = 0;
  int h = 0;
  std::string instr;
  int val;
  while (fin >> instr) {
    fin >> val;
    switch (instr[0]) {
    case 'u':
      depth -= val;
      break;
    case 'd':
      depth += val;
      break;
    case 'f':
      h += val;
      break;
    }
  }
  std::cout << h * depth << std::endl;
}
