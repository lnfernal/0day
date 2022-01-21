.globl _start

_start:
	xor %eax, %eax		# Xor anything with itself is 0, so eax = 0
	movb $1, %al		# Move byte 1 into al, eax contains syscall number
	xor %ebx, %ebx		# Set ebx to 0, ebx contains return value
	int $0x80		# Call kernel
