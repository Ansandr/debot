from directKeys import click
import time
import win32gui
import utils

button_reset = (0,0)
button_data = (0,0)
button_record = (0,0)
button_add1 = (0,0)
bits = []


def getBitCoords(bit_x, bit_y) -> list[tuple[int,int]]:
    bits = []

    x = bit_x
    y = bit_y
    for i in range(1, 17):
        if i % 4 == 0:
            x += 22
        else:
            x += 17
        bits.append((x, y))
    return bits

def load():
    global button_reset, button_data, button_record, button_add1, bits

    wind = win32gui.FindWindow(None, "DeComp v. 0.3.2 beta")
    if wind == 0:
        print("Вікно Decomp не знайдено")
        return

    wind_rect = win32gui.GetWindowRect(wind)

    print("Читання файлу program.txt")
    try:
        program = utils.readFile("program.txt")
    except IOError:
        utils.create_file("program.txt")
        return
    
    if not program:
        print("Файл програми в машиних кодах пустий")
        return

    # (left, top, right, bottom)
    x_main = wind_rect[0]
    y_main = wind_rect[1]

    bit15_x_pos = x_main + 479
    bit_y_pos = y_main + 431

    button_reset = (x_main + 627, 
                    y_main + 478)
    
    button_data = (x_main + 493, 
                    y_main + 319)
    
    button_record = (x_main + 491, 
                    y_main + 134)

    button_add1 = (x_main + 611, 
                    y_main + 134)
    
    bits = getBitCoords(bit15_x_pos, bit_y_pos)


    writeProgram(program)

def writeProgram(program):
    for row in program:
        clickButton(button_reset)
        writeRow(row)
        clickButton(button_data)
        clickButton(button_record)
        clickButton(button_add1)


def writeRow(row):
    row = row.replace(' ', '')
    i = 0
    for char in row:
        if char == '1':
            clickButton(bits[i])
        i = i + 1


def clickButton(t):
    click(t[0], t[1])