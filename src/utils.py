# Create empty file
def create_file(fileName):
    print("Створення файлу " + fileName)
    try:
        with open(fileName, 'w') as f:
            pass
        print("Файл " + fileName + " створений")
        f.close()
    except IOError:
        print("Помилка створення файлу " + fileName)
        raise


def readFile(fileName) -> list:
    try:
        lines = []
        with open(fileName, 'r') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                
                lines.append(line.strip())
        f.close()
        return lines
    except IOError:
        print("Помилка при зчитуванні файлу " + fileName)
        raise


def writeFile(fileName, programLines):
    try:
        with open(fileName, 'w') as f:
            for line in programLines:
                f.write(line)
                f.write("\n")
            f.close()
    except IOError:
        print("Помилка при запису файлу " + fileName)
        raise


def dec_to_bin(x):
    return int(bin(x)[2:])

def dec_to_bin_list():
    n = int(input("Enter an integer: "))

    create_file("list.txt")
    lines = []
    for dec in range(0, n):
        num = str(dec_to_bin(dec))
        zeros = '0'*(12 - len(num))
        num = zeros + num
        num = ' '.join([num[i:i+4] for i in range(0, len(num), 4)])
        lines.append(num)
    writeFile("list.txt", lines)