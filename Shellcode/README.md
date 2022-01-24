# Writing Shellcode

## Introduction
Shellcode is machine code which spawns a shell. Typically NULL bytes (\x00) represent the end of reading. Thus, shellcode should not have any NULL bytes. Not all shellcode spawn shells but rather, run some small program.

## Process
Write the C code you want to turn into shellcode:
```C
#include <stdlib.h>
int main() {
	exit(0);
}
```
Compile:
```bash
gcc -m32 -static exit.c -o exit
```
Disassemble 
```bash
gdb -q exit
disassmeble main
	0x08049cf5 <+0>:     lea    ecx,[esp+0x4]
	0x08049cf9 <+4>:     and    esp,0xfffffff0
	0x08049cfc <+7>:     push   DWORD PTR [ecx-0x4]
	0x08049cff <+10>:    push   ebp
	0x08049d00 <+11>:    mov    ebp,esp
	0x08049d02 <+13>:    push   ebx
	0x08049d03 <+14>:    push   ecx
	0x08049d04 <+15>:    call   0x8049d1a <__x86.get_pc_thunk.ax>
	0x08049d09 <+20>:    add    eax,0x992f7
	0x08049d0e <+25>:    sub    esp,0xc
	0x08049d11 <+28>:    push   0x0
	0x08049d13 <+30>:    mov    ebx,eax
	0x08049d15 <+32>:    call   0x8050320 <exit>

disass 0x8050320
	0x08050320 <+0>:     call   0x8049d1a <__x86.get_pc_thunk.ax>
	0x08050325 <+5>:     add    eax,0x92cdb
	0x0805032a <+10>:    sub    esp,0xc
	0x0805032d <+13>:    push   0x1
	0x0805032f <+15>:    push   0x1
	0x08050331 <+17>:    lea    eax,[eax+0x6c]
	0x08050337 <+23>:    push   eax
	0x08050338 <+24>:    push   DWORD PTR [esp+0x1c]
	0x0805033c <+28>:    call   0x8050050 <__run_exit_handlers>

disass 0x8050050
   0x08050289 <+569>:   sub    esp,0xc
   0x0805028c <+572>:   push   DWORD PTR [esp+0x4c]
   0x08050290 <+576>:   mov    ebx,DWORD PTR [esp+0x20]
   0x08050294 <+580>:   call   0x806db23 <_exit>
   0x08050299 <+585>:   mov    eax,esi

disass 0x806db23
   0x0806db23 <+0>:     mov    ebx,DWORD PTR [esp+0x4]
   0x0806db27 <+4>:     mov    eax,0xfc
   0x0806db2c <+9>:     call   DWORD PTR gs:0x10
   0x0806db33 <+16>:    mov    eax,0x1
   0x0806db38 <+21>:    int    0x80
   0x0806db3a <+23>:    hlt
```
<ul>
	<li>Main calls exit</li>
	<li>exit calls __run_exit_handlers</li>
	<li>__run_exit_handlers calls __run_exit_handlers</li>
	<li>__run_exit_handlers call _exit</li>
	<li>Disassemble _exit</li>
</ul>

The <b>gs:0x10</b> is one of four ways to perform a system call, namely:
1. int 0x80
2. sysenter (i586)
3. call gs:0x10
4. syscall (amd64)

Shellcode should be as simple and compact as possible. Most vulnerabilities often only allow a small number of injected bytes. It therefore lacks error-handling and will crash easily. 
We must also lookup the calling convention for certain libc methods. I used <a href="https://chromium.googlesource.com/chromiumos/docs/+/master/constants/syscalls.md#x86-32_bit">Chromium</a>. In this example, when calling sys_exit, eax=1 and ebx=error_code (in my case 0). So the simplest code for exit(0).
```nasm
; exit.asm

global main

section .text

main:
	mov ebx, 0 		; int error_code
	mov eax, 1      ; set eax=1
	int 0x10 		; syscall
```
Then compile:
```bash
nasm -f elf32 exit.asm
gcc -m32 exit.o -o exit_shellcode
```
Then show the contents using objdump
```bash
objdump -d exit_shellcode

00001190 <main>:
    1190:	bb 00 00 00 00       	mov    $0x0,%ebx
    1195:	b8 01 00 00 00       	mov    $0x1,%eax
    119a:	cd 80                	int    $0x80
    119c:	66 90                	xchg   %ax,%ax
    119e:	66 90                	xchg   %ax,%ax
```
Fill the C code which will execute our shellcode:
```C
char shellcode[] = "\xbb\x00\x00\x00\x00\xb8\x01\x00\x00\x00\xcd\x80";

int main(int argc, char ** argv) {
        int (*ret)();
        ret = (int(*)())shellcode;
        (int)(*ret)();
    	exit(0);
}
```
Compile and run:
```bash
gcc -m32 -z execstack -fno-stack-protector -no-pie exit.c -o exit
```

So, the five steps to shellcode:
1. Write high-level code
2. Compile and disassemble
3. Analyze and assembly
4. Clean up assembly, remove NULL
5. Extract commands and create shellcode

## Spawning a shell
Two ways to create a new process in Linux: Replace a running process, using execve(). Copy a running process to create a new one, uses fork() and execve() together.<br>
First, using exeve().
```C
#include <unistd.h>

int main() {
  char * shell[2];
  shell[0] = "/bin/sh";
  shell[1] = NULL;
  execve(shell[0], shell, NULL);
}
```
Compile:<br>
```bash
gcc -m32 -static execve.c -o execve
```