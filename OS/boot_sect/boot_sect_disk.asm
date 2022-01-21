;
; Read disk sectors
;
; AH = 0x02
; AL = Number of sectors to read (1 - 128, dec...)
; CH = Tracks/cylinder number (0 - 1023, dec...)
; CL = Sector number (1 - 17, dec...)
; DH = Head number (0 - 15 dec...)
; DL = Drive number (0=A:, 1=2nd floppy, 80h=drive 0, 81h=drive 1)
;
; On return
; AH = Status
; AL = Number of sectors read
; CF = 0 if successful
;    = 1 if failure

disk_load:
	pusha
	push dx
	mov ah, 0x02
