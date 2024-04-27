from numpy import var
import utils
import itertools

variables_dict = {}

instructions_list = []

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
    analyzing_program = False
    # var parsing
    for line in program:
        line = line.strip()
        if line.startswith("Var"):
            # parsing variables
            continue
        elif line.startswith("Program"):
            # stop parsing variables
            analyzing_program = True
            continue
        elif line and not analyzing_program:
            parts = line.split()
            if len(parts) == 2:
                variable_name = parts[0]
                variable_value = int(parts[1])
                variables_dict[variable_name] = variable_value
        elif line and analyzing_program: # program
            parts = line.split()
            if len(parts) == 2:
                instruction = parts[0]
                address = parts[1]
                
                address = replaceVariable(address)

                if address == "None":
                    print(parts[1] + " is not declared")
                    exit()

                instructions_list.append(instruction + ' ' + str(address))
            elif len(parts) == 1:
                instruction = parts[0]
                instructions_list.append(instruction)
    compliied_program = []
    for line in instructions_list:
        ins = translateRow(line)
        compliied_program.append(ins)
    return compliied_program

def replaceVariable(variable):
    if isinstance(variable, int):
        return variable
    return variables_dict.get(variable)

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

def readVariables():

    pass

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
