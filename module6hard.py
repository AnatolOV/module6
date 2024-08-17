class Figure:
    sides_count = 0

    def __init__(self, sides, color, filled):
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
            print(self.__color)

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


a = Figure((3, 4, 15), 'blue', True)
print(a.get_sides())
print(len(a))
a.set_sides(3, 3)
