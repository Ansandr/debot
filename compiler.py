import utils
import itertools

instructions_dict = {
    "LOAD":     "0000",
    "STORE":    "0001",
    "ADD":      "0010",
    "SUB":      "0011",
    "AND":      "0100",
    "OR":       "0101",
    "XOR":      "0110",
    "NOT":      "0111 00",
    "INPUT":    "0111 01",
    "OUTPUT":   "0111 10",
    "HALT":     "0111 11",
    "JNZ":      "1000",
    "JZ":       "1001",
    "JP":       "1010",
    "JM":       "1011",
    "JNC":      "1100",
    "JC":       "1101",
    "JMP":      "1110",
    "LSL":      "1111 000",
    "LSR":      "1111 001",
    "ASL":      "1111 010",
    "ASR":      "1111 011",
    "ROL":      "1111 100",
    "ROR":      "1111 101",
    "RCL":      "1111 110",
    "RCR":      "1111 111",
}

def translateAssembler(program):
    instructions = []
    for row in program:
        instructions.append(translateRow(row))
    return instructions

def translateRow(row):
    split = row.split(' ')
    
    command = split[0]
    ins_cmd = command_to_bin(command)

    adress = 0
    if (len(split) == 2):
        adress = int(split[1])
        ins_adr = str(utils.dec_to_bin(adress))

        len_zeros = 16 - len(ins_cmd) - len(ins_adr)
        
        zeros = '0'*len_zeros
        ins = ins_cmd + zeros + ins_adr
    elif (len(split) == 1):
        len_zeros = 16 - len(ins_cmd)
        
        zeros = '0'*len_zeros
        ins = ins_cmd + zeros
        
    # add space
    return ' '.join([ins[i:i+4] for i in range(0, len(ins), 4)])

def command_to_bin(instr):
    return instructions_dict.get(instr).replace(' ', '')

def compile():
    # Створення файлу

    try:
        print("Зчитування файлу програму")
        assembler_program = utils.readFile("assembler.txt")
    except IOError:
        utils.create_file("assembler.txt")
        return
    
    if not assembler_program:
        print("Файл програми в асемблері пустий")
        return
    
    print("Запис машиного коду в файл program.txt")
    utils.writeFile("program.txt", translateAssembler(assembler_program))

    print("Компіляція завершена")
