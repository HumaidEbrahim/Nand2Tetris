// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
// The algorithm is based on repetitive addition.

// RAM[2] = 0
@R2
M=0

// set R1 = n
@R1
D=M
@END
D;JEQ
@n 
M=D

// R2 = R0 + R2
(LOOP)
@R0
D=M

@R2
MD=D+M

// decrement n
@n 
D=M
MD=D-1
@LOOP
D;JGT

(END)
@END
0;JMP