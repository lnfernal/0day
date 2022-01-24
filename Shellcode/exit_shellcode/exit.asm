; exit.asm
global main
section .text

main:
  xor ebx, ebx  ; int error code
  mov al, 1     ; set eax=1
  int 0x80      ; syscall
