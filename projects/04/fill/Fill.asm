// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

@0 // position
M=0

(checkKeyboard)
	@KBD
	D=M

	@paint
	D;JNE

	@dePaint
	D;JEQ

(paint)
	@0
	D=M

	@8192
	D=D-A

	@cancel
	D;JGE

	@8192
	D=D+A


	@0
	D=M

	@SCREEN
	A=A+D

	M=-1

	@0
	M=M+1

	@checkKeyboard
	0;JMP

(cancel)
	@8192
	D=D+A
	
	@checkKeyboard
	0;JMP

(dePaint)
	@0
	D=M-1

	@checkKeyboard
	D;JLE

	@0
	M=M-1
	D=M

	@SCREEN
	A=A+D

	M=0

	@checkKeyboard
	0;JMP

(end)
	@end
	0;JMP