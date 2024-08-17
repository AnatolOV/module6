import math

class Figure:
    sides_count = 0

    def __init__(self, sides, color, filled = True):
        self.__sides = sides  # список сторон (целые числа)
        self.__color = color  # список цветов в формате RGB
        self.filled = filled  # закрашенный, bool

    def get_color(self):
        return self.__color  # возвращает список RGB цветов.

    def __is_valid_color(self, r, g, b):
        if (0 <= r <= 255) and (0 <= g <= 255) and (0 <= b <= 255):
            return True
        else:
            print('Параметры цвета некорректные')
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
            # print(self.__color)

    def __is_valid_sides(self, *args):
        # print(args)
        for i in args:
            if i <= 0 or len(self.__sides) != len(args):
                return False
        return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        perimeter = sum(self.__sides)
        return perimeter

    def set_sides(self, *new_sides):
        if len(new_sides) != self.sides_count:
            self.sides_count = len(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, sides, color, filled=True):
        super().__init__(sides, color, filled)
        if len(sides) != self.sides_count:
            self.__radius = math.sqrt(sides[1] / 3.14)
        else:
            self.__radius = math.sqrt(sides[0] / 3.14)

    def get_square(self):
        return 3.14 * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, sides, color, filled=True):
        super().__init__(sides, color, filled)

    def get_square(self):
        p = 1 / 2 * (self.get_sides()[0] + self.get_sides()[1] + self.get_sides()[2])
        S_ = math.sqrt(p * (p - self.get_sides()[0]) * (p - self.get_sides()[1]) * (p - self.get_sides()[2]))
        return S_


class Cube(Figure):
    sides_count = 12

    def __init__(self, side, color, filled=True):
        self.__sides = [side] * self.sides_count
        super().__init__(self.__sides, color, filled)

    def get_volume(self):
        # print(self.__sides[0][0], 7777)
        volume = self.__sides[0][0] ** 3
        return volume

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится +
print(circle1.get_color()) # +
# cube1.set_color(300, 70, 15) # Не изменится +
print(cube1.get_color())
#
# # Проверка на изменение сторон:
# cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
# print(cube1.get_sides())
# circle1.set_sides(15) # Изменится
# print(circle1.get_sides())
#
# # Проверка периметра (круга), это и есть длина:
# print(len(circle1))

# # Проверка объёма (куба):
# print(cube1.get_volume())
