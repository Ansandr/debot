# DeBot

Програма призначення для полегшення роботи з програмаю симуляції навчальної ЕОМ DeComp. Використання програми має на меті допомогти студентам більш ефективно розробляти алгоритми поставлені завданням, не втрачаючи час на ручний набір та кодування інструкцій в двійковий код.

## Взаємодія

Програма має консольне меню з мінімальною кількістью опцій.

### Файли

- `assembler.txt` - містить набір інструкцій асемблеру для подальшого переводу інструкцій DeComp в двійковий код.  
- `program.txt`- містить результат переводу двійкового коду програми. При необхідності вміст цього файлу програма завантажує в пам'ять симулятора DeComp.

### Меню

**1** - Компілювати інструкції з `assembler.txt` в двійковий код та вивести в `program.txt`. Слід впевнетись що файл з асемблером існує і не пустий

**2** - Завантажити код з `program.txt` в пам'ять симулятора. Перед вибором опції впевніться, що файл існує та вікну DeComp нічого не заважає, а Регістр Адреси (РА) виставлено на 0.

### Плани

- Аналіз коду ассемблера на помилки.
- Охопити більше виключних ситуацій.
- Додати функціонал аналізу виконання в _покроковому_ режимі.