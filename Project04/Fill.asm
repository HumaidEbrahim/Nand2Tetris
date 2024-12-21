// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, the
// program clears the screen, i.e. writes "white" in every pixel.

(INPUT)
    // set addr to screen address
    @SCREEN
    D=A
    @addr
    M=D
    @KBD
    D=M
    // keyboard press
    @BLACK 
    D;JGT
    // not pressed
    @CLEAR
    D;JEQ

(BLACK)
    @addr
    A=M
    M=-1
    @addr
    M=M+1
    // loop till last pixel
    @24575
    D=M
    @BLACK
    D;JEQ

   @INPUT
   0;JMP
  

(CLEAR)
    @addr
    A=M
    M=0
    @addr
    M=M+1
    @24575
    D=M
    @CLEAR
    D;JLT

   @INPUT
   0;JMP