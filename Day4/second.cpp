#include <iostream>
#include <set>
#include <fstream>
#include <vector>
#include <sstream>


void mark(int a, std::vector <std::vector<int>> &mat){
    for(int i = 0; i < 5; i++) {
      for (int j = 0; j < 5; j++){
        if (mat[i][j] == a) {
          mat[i][j] = -1;
        }
      }
    }
}

bool check(std::vector <std::vector<int>> &mat){
    for(int i = 0; i < 5; i++) {
      int count = 0;
      for (int j = 0; j < 5; j++){
        if (mat[i][j] == -1) {
          count++;
        }
      }
      if (count == 5){
        return true;
      }
    }

    for(int i = 0; i < 5; i++) {
      int count = 0;
      for (int j = 0; j < 5; j++){
        if (mat[j][i] == -1) {
          count++;
        }
      }
      if (count == 5){
        return true;
      }

    }
    return false;
}

int get_unmarked(std::vector <std::vector<int>> &mat){
  int sum = 0;
  for(int i = 0; i < 5; i++) {
      for (int j = 0; j < 5; j++){
        if (mat[i][j] != -1) {
          sum += mat[i][j];
        }
      }
    }
  return sum;

}



int main(){
  std::ifstream fin;
  fin.open("input.txt");
  std::vector <int> nums;

  int bits = 0;
  std::string num_called;
  fin >> num_called;
  std::cout << num_called << std::endl;
  std::vector <std::vector <std::vector<int>>> mats;
  std::cerr << "Here";

  while(fin.peek() != EOF) {
    std::vector <std::vector <int>> mat (5, std::vector <int>(5, 0));
    for (int i = 0; i < 5; i++) {
      for (int j = 0; j < 5; j++) {
        fin >> mat[i][j];
      }
    }
    mats.push_back(mat);
  }

  std::vector<int> vect;

  std::stringstream ss(num_called);

  std::cerr << "Here2" << std::endl;
  
  for (int i; ss >> i;) {
      vect.push_back(i);    
      if (ss.peek() == ',')
          ss.ignore();
  }

  std::cerr << "Here3" << std::endl;
  std::set <int> won; 
  for (int x: vect){
    //std::cout << x << std::endl;
    for(int i = 0; i < mats.size(); i++){
      auto &mat = mats[i]; 
      mark(x, mat);

      if (won.find(i) == won.end() && check(mat)){
        won.insert(i);
        int s = get_unmarked(mat);
        std::cout << s * x << std::endl;
      }
    } 
  }
 
}
