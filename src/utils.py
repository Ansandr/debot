import os

# Create empty file
def create_file(fileName):
    print("Створення файлу " + fileName)
    try:
        with open(fileName, 'w') as f:
            pass
        print("Файл " + fileName + " створений")
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
    except IOError:
        print("Помилка при запису файлу " + fileName)
        raise

def dec_to_bin(x):
    return int(bin(x)[2:])