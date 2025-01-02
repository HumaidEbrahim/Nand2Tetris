compTable = {
    "0": "0101010",
    "1": "0111111",
    "-1": "0111010",
    "D": "0001100",
    "A": "0110000",
    "!D": "0001101",
    "!A": "0110001",
    "-D": "0001111",
    "-A": "0110011",
    "D+1": "0011111",
    "A+1": "0110111",
    "D-1": "0001110",
    "A-1": "0110010",
    "D+A": "0000010",
    "D-A": "0010011",
    "A-D": "0000111",
    "D&A": "0000000",
    "D|A": "0010101",
    "M": "1110000",
    "!M": "1110001",
    "-M": "1110011",
    "M+1": "1110111",
    "M-1": "1110010",
    "D+M": "1000010",
    "D-M": "1010011",
    "M-D": "1000111",
    "D&M": "1000000",
    "D|M": "1010101"
}
destTable = {
    None: "000",  # No destination
    "M": "001",   # Store in memory (RAM[A])
    "D": "010",   # Store in register D
    "MD": "011",  # Store in both M and D
    "A": "100",   # Store in register A
    "AM": "101",  # Store in both A and M
    "AD": "110",  # Store in both A and D
    "AMD": "111"  # Store in A, M, and D
}
jmpTable = {
    None: "000",  # No jump
    "JGT": "001", # Jump if out > 0
    "JEQ": "010", # Jump if out == 0
    "JGE": "011", # Jump if out >= 0
    "JLT": "100", # Jump if out < 0
    "JNE": "101", # Jump if out != 0
    "JLE": "110", # Jump if out <= 0
    "JMP": "111"  # Unconditional jump
}
symbolTable = {
    # Predefined symbols
    "SP": 0,
    "LCL": 1,
    "ARG": 2,
    "THIS": 3,
    "THAT": 4,
    "R0": 0,
    "R1": 1,
    "R2": 2,
    "R3": 3,
    "R4": 4,
    "R5": 5,
    "R6": 6,
    "R7": 7,
    "R8": 8,
    "R9": 9,
    "R10": 10,
    "R11": 11,
    "R12": 12,
    "R13": 13,
    "R14": 14,
    "R15": 15,
    "SCREEN": 16384,
    "KBD": 24576
}

inputFile = input("File: ")

def populateTable(file):
    count = 0
    varSymbol = 16
    with open(file, "r") as file:
        for line in file:
            # Strip whitespace and comments
            line = line.strip()
            if not line or line.startswith('/'):
                continue

            # loop symbol
            if line.startswith('('):
                line = line.removeprefix('(').removesuffix(')')
                if line not in symbolTable:  
                    symbolTable[line] = count
                continue

            count += 1
    
def populateVariables(file):
    varSymbol = 16
    with open(file, "r") as file:
        for line in file:
            # Strip whitespace and comments
            line = line.strip()
            if not line or line.startswith('/'):
                continue

            # variable symbol
            if line.startswith('@') and line[1].isalpha():
                symbol = line[1:]
                if symbol not in symbolTable:
                    symbolTable[symbol] = varSymbol
                    varSymbol += 1

# parse lines
def parser(file):
    # open file
    with open(file, "r") as file:
        for line in file:
            line = line.strip()
            if line and not line.startswith("/") and not line.startswith('(') :
                
                if line.startswith('@'):
                    translator(line,"A")
                else:
                    translator(line,"C")
                            
def translator(cmd,instruc):
    # c instruction
    binary = ""
    dest = "000"
    comp = "000000"
    jmp = "000"
    if(instruc == "C"):
       if '=' in cmd:
         dest,comp = cmd.split('=')
         binary = "111" + compTable.get(comp)  + destTable.get(dest) + jmp
         
       if ';' in cmd:
           comp,jmp = cmd.split(';')
           binary = "111" + compTable.get(comp)  + dest + jmpTable.get(jmp) 
    # a instruction 
    else: 
        cmd = cmd[1:]
        if cmd in symbolTable:
            binary = symbolTable.get(cmd)
        else:
            binary = cmd
        binary = bin(int(binary))[2:].zfill(16) 
        
    # write to file
    global inputFile
    inputFile = inputFile.split('.')[0]    
    with open(inputFile + ".hack","a") as file:
        file.writelines(binary + '\n')

populateTable(inputFile)
populateVariables(inputFile)
parser(inputFile)

