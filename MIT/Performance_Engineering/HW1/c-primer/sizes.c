// Copyright (c) 2012 MIT License by 6.172 Staff

#define OUTPUT "size of %s : %zu bytes \n"

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main() {

  // Composite types have sizes too.
  typedef struct {
    int id;
    int year;
  } student;

  // Please print the sizes of the following types:
  // int, short, long, char, float, double, unsigned int, long long
  // uint8_t, uint16_t, uint32_t, and uint64_t, uint_fast8_t,
  // uint_fast16_t, uintmax_t, intmax_t, __int128, and student

  // Here's how to show the size of one type. See if you can define a macro
  // to avoid copy pasting this code.
  printf("size of %s : %zu bytes \n", "int", sizeof(int));
  printf(OUTPUT,"short",sizeof(short));
  printf(OUTPUT,"long",sizeof(long));
  printf(OUTPUT,"char",sizeof(char));
  printf(OUTPUT,"float",sizeof(float));
  printf(OUTPUT,"double",sizeof(double));
  printf(OUTPUT,"unsigned int",sizeof(unsigned int));
  printf(OUTPUT,"long long",sizeof(long long));
  printf(OUTPUT,"uint8_t",sizeof(uint8_t));
  printf(OUTPUT,"uint16_t",sizeof(uint16_t));
  printf(OUTPUT,"uint32_t",sizeof(uint32_t));
  printf(OUTPUT,"uint64_t",sizeof(uint64_t));
  printf(OUTPUT,"uint_fast8_t",sizeof(uint_fast8_t));
  printf(OUTPUT,"uint_fast16_t",sizeof(uint_fast16_t));
  printf(OUTPUT,"uintmax_t",sizeof(uintmax_t));
  printf(OUTPUT,"__int128",sizeof(__int128));
  printf(OUTPUT,"student",sizeof(student));
  // e.g. PRINT_SIZE("int", int);
  //      PRINT_SIZE("short", short);

  // Alternatively, you can use stringification
  // (https://gcc.gnu.org/onlinedocs/cpp/Stringification.html) so that
  // you can write
  // e.g. PRINT_SIZE(int);
  //      PRINT_SIZE(short);

  student you;
  you.id = 12345;
  you.year = 4;


  // Array declaration. Use your macro to print the size of this.
  int x[5];
  printf(OUTPUT,"x",sizeof(x));

  // You can just use your macro here instead: PRINT_SIZE("student", you);
  printf("size of %s : %zu bytes \n", "student", sizeof(you));

  return 0;
}
