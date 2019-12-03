import ast
import sys

def adder(opcode, a, b, output):
    opcode[output] = opcode[a] + opcode[b]
    return opcode


def multiplier(opcode, a, b, output):
    opcode[output] = opcode[a] * opcode[b]
    return opcode


if __name__=='__main__':
    test = 0 

    # Inputs
    if test:
        #opcode = [1,0,0,0,99]
        opcode = [2,3,0,3,99]
        #opcode = [2,4,4,5,99,0]
        #opcode = [1,1,1,4,99,5,6,0,99]

    else:
        with open('input.txt', 'r') as f:
            opcode_str = f.readline()

        opcode = list(ast.literal_eval(opcode_str))

    opcode_len = len(opcode)
    i = 0

    # If command line parameters are presented
    if (len(sys.argv)) == 3:
        arg_list = sys.argv
        first = int(arg_list[1])
        second = int(arg_list[2])
        opcode[1] = first
        opcode[2] = second

    # Logic
    while i < opcode_len:
        chunk = opcode[i:i+4]
        print(chunk)

        operand = chunk[0]

        if operand == 1:
            opcode = adder(opcode, chunk[1], chunk[2], chunk[3])
        elif operand == 2:
            opcode = multiplier(opcode, chunk[1], chunk[2], chunk[3])
        elif operand == 99:
            break

        i = i + 4 

    print(opcode)

'''
noun increases the value by 32,000
verb increases the value by 1

The right combination would be 60, 86

initial state + (60 * 32,000) + (86 * 1) = 19,690,720
'''
