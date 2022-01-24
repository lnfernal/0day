char shellcode[] = "\xcc\xdb"
                   "\xb0\x01"
                   "\xcd\x80";

/*
 * 31 db        xor ebx,ebx
 * b0 01        mov al,0x1
 * cd 80        int 0x80
*/

int main() {
  int (*func)();
  func = (int (*)()) shellcode;
  (int)(*func)();
}
