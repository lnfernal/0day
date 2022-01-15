;
; Simple printing functions
;

; Prints all characters in string up to NULL byte
print:
	pusha		; Push all registers onto the stack
	mov ah, 0x0E	; Set TTY mode
	start_print:

	mov al, [bx]	; BX contains string information
	cmp al, 0x00	; If NULL byte
	je end_print	; 	Break
	int 0x10
	inc bx		; Increment to next character
	jmp start_print	; Jump back to start

	end_print:
	popa		; Pop all registers off the stack
	ret

; Print newline
print_newline:
	pusha
	mov ah, 0x0E	; Set TTY mode
	mov al, 0x0A	; \n character
	int 0x10
	mov al, 0x0D	; \r character
	int 0x10
	popa
	ret

; Print hexadecimal values
print_hex:
	pusha
	mov cl, 0x00	; Set the counter to 0
	
	start_hex:
	mov al, [bx]	; Move character into al
	cmp al, 0x00	; If NULL byte
	je end_hex	; 	Jump to end of routine
	int 0x10	; print
	inc cl		; Increment cl
	cmp cl, 0x5	; If cl is not equal to 5
	je start_hex	;	Jump to end_hex
	inc bx		; Increment to next character
	jmp start_hex	; Jump to start of printing routine
	
	end_hex:
	popa
	ret

