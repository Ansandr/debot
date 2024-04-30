from numpy import var
import utils

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

def getMarksDict(program):
    marks_dict = {}
    i = 0
    readProgram = False
    for line in program:
        line = line.replace('\t', ' ') 
        parts = line.split(' ')

        if line.startswith("Program"):
            readProgram = True
            continue

        if readProgram:
            if len(parts) == 3:
                mark = parts[0]
                marks_dict[mark] = i
            i = i+1
        
    return marks_dict

def getVariablesDict(program):
    variables_dict = {}
    readVar = False
    for line in program:
        parts = line.split()

        if line.startswith("Var"):
            readVar = True
            continue

        if line.startswith("Program"):
            readVar = False
            break
        
        if len(parts) == 2 and readVar:
            variable_name = parts[0]
            variable_value = int(parts[1])
            variables_dict[variable_name] = variable_value

    return variables_dict

def translateAssembler(program):

    variables = getVariablesDict(program)
    marks = getMarksDict(program)

    dict = variables | marks

    instruction_list = []

    readProgram = False
    for line in program:
        if line.startswith("Program"):
            readProgram = True
            continue
        
        if not readProgram:
            continue

        line = line.replace('\t', ' ')
        parts = line.split(' ')

        hasAdress = True
        if len(parts) == 1:
            instruction = parts[0]
            hasAdress = False
        elif len(parts) == 2:
            instruction = parts[0]
            address = parts[1]
        elif len(parts) == 3:
            instruction = parts[1]
            address = parts[2]

        if hasAdress:

            address = replaceVariable(address, dict)
            
            if address is None:
                print(parts[1] + " is not declared")
                return []

            instruction_list.append(instruction + ' ' + str(address))
            continue

        instruction_list.append(instruction)
        pass

    utils.writeFile("instructions.txt", instruction_list)

    compliied_program = []
    for line in instruction_list:
        ins = translateRow(line)
        compliied_program.append(ins)
    return compliied_program
                
def replaceVariable(variable, dict):
    if isinstance(variable, int):
        return variable
    return dict.get(variable)

def translateRow(row):
    parts = row.split(' ')
    
    command = parts[0]
    ins_cmd = command_to_bin(command)
    ins_cmd = ins_cmd.replace(' ', '')

    adress = 0
    if (len(parts) == 2):
        adress = int(parts[1])
        ins_adr = str(utils.dec_to_bin(adress))

        len_zeros = 16 - len(ins_cmd) - len(ins_adr)
        
        zeros = '0'*len_zeros
        ins = ins_cmd + zeros + ins_adr
    elif (len(parts) == 1):
        len_zeros = 16 - len(ins_cmd)
        
        zeros = '0'*len_zeros
        ins = ins_cmd + zeros
        
    # add space
    return ' '.join([ins[i:i+4] for i in range(0, len(ins), 4)])

def command_to_bin(instr):
    return instructions_dict.get(instr)

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
    open("program.txt", "w").close()
    utils.writeFile("program.txt", translateAssembler(assembler_program))

    print("Компіляція завершена")
