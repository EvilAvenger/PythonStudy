#!/usr/bin/python3

# Строки

# Заполните код преведенных ниже функций. Функция main() уже настроена
# для вызова функций с несколькими различными параметрами,
# и выводит 'OK' в случае, если вызов функции корректен.
# Начальный код каждой функции содержит 'return'
# и является просто заготовкой для вашего кода.


# A. Пончики
# Дано количество пончиков (целое число);
# Нужно вернуть строку следующего вида:
# 'Количество пончиков: <count>', где <count> это количество,
# переданное в функцию как параметр.
# Однако, если количество 10 и более - нужно использовать слово
# 'много', вместо текущего количества.
# Таким образом, donuts(5) вернет 'Количество пончиков: 5'
# а donuts(23) - 'Количество пончиков: много'
def donuts(count):
    template = 'Количество пончиков: {0}'
    if count >= 10:
        str = template.format('много')
    else:
        str = template.format(count)
    return str


# B. Оба конца
# Дана строка s.
# Верните строку, состоящую из первых 2
# и последних 2 символов исходной строки.
# Таким образом, из строки 'spring' получится 'spng'.
# Однако, если длина строки меньше, чем 2 -
# верните просто пустую строчку.
def both_ends(s):
    temp = ""
    if len(s) >= 2:
        temp = "".join((s[0:2], s[-2:]))
    return temp


# C. Кроме первого
# Дана строка s.
# Верните строку, в которой все вхождения ее первого символа
# заменены на '*', за исключением самого этого первого символа.
# Т.е., из 'babble' получится 'ba**le'.
# Предполагается, что длина строки 1 и более.
# Подсказка: s.replace(stra, strb) вернет версию строки,
# в которой все вхождения stra будут заменены на strb.
def fix_start(s):
    s = "".join((s[0], s[1:].replace(s[0], '*')))
    return s


# D. Перемешивание
# Даны строки a и b.
# Верните одну строку, в которой a и b отделены пробелом '<a> <b>',
# и поменяйте местами первые 2 символа каждой строки.
# Т.е.:
#   'mix', 'pod' -> 'pox mid'
#   'dog', 'dinner' -> 'dig donner'
# Предполагается, что строки a и b имеют длину 2 и более символов.
def mix_up(a, b):
    result = "{0}{1} {2}{3}".format(b[0:2], a[2:], a[0:2], b[2:])
    return result


# E. Хорош
# Дана строка.
# Найдите первое вхождение подстрок 'не' и 'плох'.
# Если 'плох' идет после 'не' - замените всю подстроку
# 'не'...'плох' на 'хорош'.
# Верните получившуюся строку
# Т.о., 'Этот ужин не так уж плох!' вернет:
# Этот ужин хорош!
def not_bad(s):
    str1 = "не"
    str2 = "плох"
    str3 = "хорош"
    index = s.find(str1)
    index2 = s.find(str2)
    if index > 0 and index2 > 0 and index2 > index:
        s = "{0}{1}{2}".format(s[0: index], str3, s[index2 + len(str2):])
    return s


# F. Две половины
# Рассмотрим разделение строки на две половины.
# Если длина четная - обе половины имеют одинаковую длину.
# Если длина нечетная — дополнительный символ присоединяется к первой половине.
# Т.е., 'abcde', первая половина 'abc', вторая - 'de'.
# Даны 2 строки, a и b, верните строку вида:
# 1-половина-a + 1-половина-b + 2-половина-a + 2-половина-b
def front_back(a, b):
    result = "{0}{1}{2}{3}".format(
        split_Word(a, False), split_Word(b, False), split_Word(a, True), split_Word(b, True))
    return result


def split_Word(word, revert):
    index = int(len(word) / 2)
    index += len(word) % 2
    result = word[0:index] if not revert else word[index:]
    return result


# Простая функция test() используется в main() для вывода
# сравнения того, что возвращает с функция с тем, что она должна возвращать.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s Получено: %s | Ожидалось: %s' %
          (prefix, repr(got), repr(expected)))


# Вызывает фунции выше с тестовыми параметрами.
def main():
    print('Пончики')
    # Каждая строка вызывает donuts() и сравнивает возвращаемое значение с
    # ожидаемым.
    test(donuts(4), u'Количество пончиков: 4')
    test(donuts(9), 'Количество пончиков: 9')
    test(donuts(10), 'Количество пончиков: много')
    test(donuts(99), 'Количество пончиков: много')

    print()
    print('Оба конца')
    test(both_ends('spring'), 'spng')
    test(both_ends('Hello'), 'Helo')
    test(both_ends('a'), '')
    test(both_ends('xyz'), 'xyyz')

    print()
    print('Кроме первого')
    test(fix_start('babble'), 'ba**le')
    test(fix_start('aardvark'), 'a*rdv*rk')
    test(fix_start('google'), 'goo*le')
    test(fix_start('donut'), 'donut')

    print()
    print('Перемешивание')
    test(mix_up('mix', 'pod'), 'pox mid')
    test(mix_up('dog', 'dinner'), 'dig donner')
    test(mix_up('gnash', 'sport'), 'spash gnort')
    test(mix_up('pezzy', 'firm'), 'fizzy perm')

    print()
    print('Хорош')
    test(not_bad('Этот фильм не так уж плох'), 'Этот фильм хорош')
    test(not_bad('А ужин был не плох!'), 'А ужин был хорош!')
    test(not_bad('Этот чай уже не горячий'), 'Этот чай уже не горячий')
    test(not_bad("Этот плох, но не совсем"), "Этот плох, но не совсем")

    print()
    print('Две половины')
    test(front_back('abcd', 'xy'), 'abxcdy')
    test(front_back('abcde', 'xyz'), 'abcxydez')
    test(front_back('Kitten', 'Donut'), 'KitDontenut')


# Стандартный шаблон для вызова функции main().
if __name__ == '__main__':
    main()
