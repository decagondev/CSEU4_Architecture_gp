import sys
# lets build up our simulator some more
# now we will add the concept of registers
# and an add opcode, using external files for program code

# let's make a simple data driven machine!!!
HALT = 1
PRINT_TOM = 2
PRINT_NUM = 3
SAVE = 4
PRINT_REG = 5
ADD = 6

# lets load a program in to memory
def load_memory(filename):
    pass

# lets make a model of memory to hold our program
# TODO: refactor to load in memory from file eg `memory = [0] * 128`
memory = []

register = [0] * 8

# think about keeping track where we are currently in mem to fetch the next instruction
pc = 0
# are we actually running
running = True
op_size = 0

# Main entrypoint
# TODO: grab any args
# TODO: load the memory
# REPL

# lets make a running loop...
while running:
    # extract a command maybe?
    # FETCH
    command = memory[pc]

    # lets check what command has been fetched
    # DECODE
    if command == HALT:
        # EXECUTE
        running = False
    
    elif command == PRINT_TOM:
        # EXECUTE
        print("Tom")
        op_size = 1

    elif command == PRINT_NUM:
        num = memory[pc + 1]
        print(num)
        op_size = 2

    elif command == SAVE:
        num = memory[pc + 1]
        reg = memory[pc + 2]
        register[reg] = num
        op_size = 3

    elif command == PRINT_REG:
        reg = memory[pc + 1]
        print(register[reg])
        op_size = 2

    # handle ADD opcode
    elif command == ADD:
        reg_a = memory[pc + 1]
        reg_b = memory[pc + 2]
        register[reg_a] += register[reg_b]
        op_size = 3

    
    else:
        print(f"Invalid Instruction: {command}")
        running = False

    # how will we move forward in memory to grab the next command?
    pc += op_size

