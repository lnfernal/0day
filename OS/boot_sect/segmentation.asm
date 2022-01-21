mov ah, 0x0E	; Set tty mode

mov bx, 0x7C0	; Segmentation is automatic
mov ds, bx	; From now on all memory references will be ds implicitly
mov al, [the_secret]
int 0x10

mov al, [es:the_secret]
int 0x10

mov bx, 0x7C0
mov es, bx
mov al, [es:the_secret]
int 0x10

jmp $

the_secret:
	dw 'X'

times 510-($-$$) db 0
dw 0xaa55
