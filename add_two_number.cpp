#include <iostream>
using namespace std;

extern "C" int add_numbers(int a, int b) {
    return a + b;
}
