#include <iostream>
#include <fstream>


int main(){
  std::ifstream fin;
  fin.open("input.txt");
  int depth = 0;
  int h = 0;
  int aim = 0;
  std::string instr;
  int val;
  while(fin >> instr){
    fin >> val;
    switch (instr[0]){
      case 'u': 
        aim -= val;
        break;
      case 'd':
        aim += val;
        break;
      case 'f':
        h += val;
        depth += val * aim;
        break;
    }
  }
  std::cout << h * depth<< std::endl;
}
