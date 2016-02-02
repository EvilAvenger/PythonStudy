#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Имитация текста

Прочитайте файл, указанный в командной строке.
Используйте str.split() (без аргументов) для получения всех слов в файле.
Вместо того, чтобы читать файл построчно, проще считать
его в одну гигантскую строку и применить к нему split() один раз.

Создайте "имитационный" словарь, который связывает каждое слово
со списком всех слов, которые непосредственно следуют за этим словом в файле.
Список слов может быть в любом порядке и должен включать дубликаты. 

Так, например, для текста "Привет, мир! Привет, Вселенная!" мы получим такой
имитационный словарь:
{'': ['Привет,'], 'Привет,': ['мир!', 'Вселенная!'], 'мир!': ['Привет,']}
Будем считать, в качестве ключа для первого слова в файле используется пустая строка.

С помощью имитационного словаря довольно просто генерировать случайные тексты, 
имитирующие оригинальный. Возьмите слово, посмотрите какие слова могут за ним, 
выберите одно из них наугад, выведите его и используйте это слово 
в следующей итерации.

Используйте пустую строку в качестве ключа для первого слова.
Если вы когда-нибудь застрянете на слове, которого нет в словаре,
вернетесь к пустой строке, чтобы продолжать генерацию текста.

Примечание: стандартный python-модуль random включает в себя метод 
random.choice(list), который выбирает случайный элемент из непустого списка.

"""

import random
import sys
import codecs

PARSE_EXPRESSION = "!><?#-:.,;«»“="


def mimic_dict(filename):
    """Возвращает имитационный словарь, сопоставляющий каждое слово 
    со списом слов, которые непосредственно следуют за ним в тексте"""
    wordDic = {}
    lines = []
    file = open(filename, 'r', encoding="utf-8")
    try:
        lines = [word for word in file.read().split()]
        wordDic[""] = set([lines[0]])
        prevWord = ""
        for word in lines:
            if prevWord == "":
                prevWord = word.lower().strip(PARSE_EXPRESSION)
            else:
                if prevWord in wordDic:
                    wordDic[prevWord].add(word)
                else:
                    wordDic[prevWord] = {word}
                prevWord = word.lower().strip(PARSE_EXPRESSION)

    finally:
        file.close()
    return wordDic


def print_mimic(mimic_dict, word, i, sentence):
    """Принимает в качестве аргументов имитационный словарь и начальное слово,
    выводит 200 случайных слов."""
    sentence = ' '.join((sentence, word))
    while i <= 200:
        i += 1
        word = word.lower().strip(PARSE_EXPRESSION)
        if word in mimic_dict:
            myList = mimic_dict[word]
        else:
            myList = mimic_dict[""]

        randomWord = random.choice(list(myList))
        return print_mimic(mimic_dict, randomWord, i, sentence)
    return sentence


def main():
    if len(sys.argv) != 2:
        print('usage: ./mimic.py file-to-read')
        sys.exit(1)

    d = mimic_dict(sys.argv[1])
    sentence = print_mimic(d, random.choice(list(d.keys())), 0, "")
    print(sentence.strip())

if __name__ == '__main__':
    main()
