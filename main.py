from consolemenu import *
from consolemenu.items import *
import compiler
import loader

if __name__ == "__main__":
    # Create the menu
    menu = ConsoleMenu(
        "Компілятор Decomp", 
        "Програма кодує інструкцій симулятора DeComp та вводить їх у пам'ять симулятора",
        exit_option_text="Вихід",
        clear_screen=False
        )

    # Translate
    item_compile = FunctionItem("Компілювати інструкції", compiler.compile)

    # CODE
    item_load = FunctionItem("Завантажити код", loader.load)

    menu.append_item(item_compile)
    menu.append_item(item_load)

    menu.show()
