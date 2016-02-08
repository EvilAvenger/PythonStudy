#!/usr/bin/python3
import sys
import math
from functools import reduce

__author__ = "Vitaly Bibikov"
__version__ = "0.1"


def __main__():

    wallPapers = Wallpapers(1, 10, 100)
    ceiling = CeilingPaint(2000, 200, 200)
    floor = Laminate(3, 2, 5, 300)

    kitchen = Room(3, 2.4, 5, 2, 2, "Kitchen")
    room1 = Room(3, 2.4, 4, 2, 2)
    room2 = Room(3, 2.4, 3, 2, 2)

    flat = Flat(kitchen, room1, room2)
    flat.estimateTotalComsumption(wallPapers, ceiling, floor)
    return


class ConstructMaterials(object):
    """docstring for ConstructMaterials"""

    def __init__(self, square, pricePerItem):
        self.square = square
        self.pricePerItem = pricePerItem

    def countItemsNeeded(self, surfaceSquare):
        items = math.ceil(surfaceSquare / self.square)
        return items

    def countPrice(self, items):
        price = self.pricePerItem * items
        return price


class Wallpapers(ConstructMaterials):
    """docstring for Wallpapers"""

    def __init__(self, width, length, pricePerItem):
        super(self.__class__, self).__init__(width * length, pricePerItem)
        self.width = width
        self.length = length

    def __str__(self):
        return self.__class__.__name__


class CeilingPaint(ConstructMaterials):
    """docstring for CeilingPaint"""

    def __init__(self, weight, consumption, priceForItem):
        super(self.__class__, self).__init__(
            weight / consumption, priceForItem)
        self.weight = weight
        self.consumption = consumption

    def __str__(self):
        return self.__class__.__name__


class Laminate(ConstructMaterials):
    """docstring for Laminate"""

    def __init__(self, length, width, amount, priceForItem):
        square = length * width * amount
        super(self.__class__, self).__init__(square, priceForItem)
        self.length = length
        self.width = width
        self.amount = amount

    def __str__(self):
        return self.__class__.__name__


class Room(object):

    def __init__(self, width, height, length, windowWidth, doorWidth, name="Room"):
        self.width = width
        self.height = height
        self.length = length
        self.windowWidth = windowWidth
        self.doorWidth = doorWidth
        self.name = name

    def doWallpapering(self, wallPapers):
        square = (2 * (self.width + self.length) -
                  self.windowWidth - self.doorWidth) * self.height
        items = wallPapers.countItemsNeeded(square)
        price = wallPapers.countPrice(items)
        print("Обои: {0}x{1}={2} руб.".format(items, price, items * price))
        return price

    def paintCeiling(self, ceiling):
        square = self.length * self.width
        items = ceiling.countItemsNeeded(square)
        price = ceiling.countPrice(items)

        print("Краска: {0}x{1}={2} руб.".format(items,
                                                price, items * price))
        return price

    def makeFloor(self, floor):
        square = self.length * self.width
        items = floor.countItemsNeeded(square)
        price = floor.countPrice(items)

        print("Ламинат: {0}x{1}={2} руб.".format(items,
                                                 price, items * price))
        return price

    def estimateConsumption(self, wallPapers, ceiling, floor):
        print(self)
        price = self.doWallpapering(wallPapers)
        price += self.paintCeiling(ceiling)
        price += self.makeFloor(floor)
        return price

    def __str__(self):
        return "[{0}: width: {1} m, length: {2} m, height: {3} m]"\
            .format(self.name, self.width, self.length, self.height)


class Flat(object):
    """docstring for Flat"""

    def __init__(self, *rooms):
        self.rooms = list(rooms)

    def addRoom(self, room):
        self.rooms.append(room)

    def deleteRoom(self):
        self.rooms.remove(room)

    def estimateTotalComsumption(self, wallPapers, ceiling, floor):
        total = reduce(lambda x, y: x + y, list(map(lambda x: x.estimateConsumption(
            wallPapers, ceiling, floor), self.rooms)))
        print('Total: {total} руб. '.format(total=total))


if __name__ == '__main__':
    __main__()
