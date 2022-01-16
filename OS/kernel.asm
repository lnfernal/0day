mov ah, 0x0e	; tty mode

mov bp, 0x8000	; Address far away from boot sector (0x7c00)
mov sp, bp

push 0x41 	; A
push 0x42	; B
push 0x43	; C

; recover our characters using 'pop'
; can only pop full words
pop cx
mov al, cl
int 0x10

pop bx
mov al, bl,
int 0x10

pop bx
mov al, bl
int 0x10

; Infinite loop (e9 fd ff)
jmp $ ; Jump to the current address

; Fill with 510 zeros minus the size of the previous code
times 510-($-$$) db 0
; Magic number
dw 0xaa55
