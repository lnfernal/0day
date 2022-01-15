;
; Boot sector
;
[org 0x7C00]	; Offset 

; Print "Hello, World"
mov bx, hello_world
call print
call print_newline

; Print "Goodbye, World"
mov bx, goodbye_world
call print
call print_newline

; Print "DedSec"
mov bx, ded_sec
call print
call print_newline

; Print hexnumbers
mov bx, alphabet_hex
call print_hex
call print_newline

hello_world:
	db 'Hello, World', 0
goodbye_world:
	db 'Goodbye, World', 0
ded_sec:
	db 'DedSec', 0
alphabet_hex:
	db '\x41\x42\x43\x44', 0

; Infinite jump
jmp $

%include "boot_sect_print.asm"

; Padding and magic number
times 510-($-$$) db 0
dw 0xaa55
