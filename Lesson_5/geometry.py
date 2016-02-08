# -*- coding: utf-8 -*-

import turtle
import time
import random


class Polygon(object):
    """docstring for Polygon"""

    def __init__(self, coordinates, color):
        self.coordinates = coordinates
        self.color = color


class Rectangle(Polygon):
    """docstring for Rectangle"""

    def __init__(self, coordinates, width, color):
        super(Rectangle, self).__init__(coordinates, color)
        self.width = width


class Triangle(Polygon):
    """docstring for Triangle"""

    def __init__(self, coordinates, length, color):
        super(Triangle, self).__init__(coordinates, color)
        self.length = length


class Circle(object):
    """docstring for Circle"""

    def __init__(self, coordinates, radius, color):
        super(Circle, self).__init__()
        self.coordinates = coordinates
        self.radius = radius
        self.color = color


class Vector(object):
    """docstring for Vector"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __sub__(self, num):
        self.x *= num
        self.y *= num
        return self


def draw_rect(ttl):
    x = random.randint(-200, 200)  # получаем случайные координаты
    y = random.randint(-200, 200)

    ttl.color('red')  # устанавливаем цвет линии
    ttl.penup()  # убираем "ручку" от холста, чтобы переместить в нужное место
    ttl.setpos(x, y)  # перемещаем на первую вершину
    ttl.pendown()  # опускаем ручку обратно
    ttl.goto(x + 50, y)  # проводим линии для сторон четырёхугольника
    ttl.goto(x + 50, y + 50)
    ttl.goto(x, y + 50)
    ttl.goto(x, y)


def draw_circle(ttl):
    x = random.randint(-200, 200)  # получаем случайные координаты
    y = random.randint(-200, 200)

    ttl.color('violet')  # устанавливаем цвет линии
    ttl.penup()  # убираем "ручку" от холста, чтобы переместить в нужное место
    ttl.setpos(x, y)  # перемещаем в "основание" - это будет самая низкая точка
    ttl.pendown()  # опускаем ручку обратно

    ttl.circle(25)  # рисуем круг радиуса 25


def main():

    # устанавливаем все задержки в 0, чтобы рисовалось мгновенно
    turtle.tracer(0, 0)
    turtle.hideturtle()  # убираем точку посередине

    ttl = turtle.Turtle()  # создаём объект черепашки для рисования
    ttl.hideturtle()  # делаем её невидимой

    while True:
        time.sleep(0.5)  # засыпаем на полсекунды, чтобы увидеть что нарисовали
        ttl.clear()  # очищаем всё нарисованое ранее
        draw_rect(ttl)
        draw_circle(ttl)
        turtle.update()  # т.к. мы сделали turtle.tracer(0, 0) нужно обновить экран, чтобы увидеть нарисованное

if __name__ == '__main__':
    main()
