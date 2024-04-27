from consolemenu import ConsoleMenu
from consolemenu.items import FunctionItem
import compiler
import loader
import utils

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

    # 0 to n
    item_dec2bin = FunctionItem("Перевести десяткові в бінарні", utils.dec_to_bin_list)

    menu.append_item(item_compile)
    menu.append_item(item_load)
    menu.append_item(item_dec2bin)

    menu.screen.println("Розробив ст. Стафеєв Андрій")
    menu.screen.println("https://github.com/Ansandr/debot")

    menu.show()
