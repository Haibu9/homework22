from math import pi

class Figure:
    sides_count = 0

    def __init__(self,__color, *args, filled = False):
        self.__sides = args
        self.__color = __color
        self.filled = filled

    def get_color(self):
        return [self.__color[0], self.__color[1], self.__color[2]]

    def __is_valid_color(self, r, g, b):
        RGB = [r, g, b]
        for col in RGB:
            if isinstance(col, int) and col >= 0 and col <= 255:
                continue
            else:
                return False
        return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def get_sides(self):
        return list(self.__sides)

    def __is_valid_sides(self, *args):
        for line in args:
            if isinstance(line, int) and line > 0 and len(args) == self.sides_count:
                continue
            else:
                return False
        return True

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = new_sides

class Circle(Figure):
    sides_count = 1

    def __init__(self, __color, *args):
        if len(args) != self.sides_count:
            args = 1
        super().__init__(__color, *args)
        self.__radius = args[0] / (2 * pi)

    def get_square(self):
        return self.__radius ** 2 * pi

class Triangle(Figure):
    sides_count = 3

    def __init__(self, __color, *args):
        args = list(args)
        if len(args) == 1:
            while len(args) < self.sides_count:
                args.append(args[0])
        elif len(args) != self.sides_count:
            args = []
            for side in range(0, self.sides_count - 1):
                args.append(1)
        super().__init__(__color, *args)

    def get_square(self):
        res = len(self) / 2
        a = self.get_sides()
        res = (res * (res - a[0]) * (res - a[1]) * (res - a[2])) ** 0.5
        return res

class Cube(Figure):
    sides_count = 12

    def __init__(self, __color, *args):
        args = list(args)
        set_ = set(args)
        if len(args) == 1:
            while len(args) < self.sides_count:
                args.append(args[0])
        elif len(args) != self.sides_count or len(args) == self.sides_count and set_ != 1:
            args = []
            for side in range(0, self.sides_count - 1):
                args.append(1)
        super().__init__(__color, *args)

    def get_volume(self):
        a = self.get_sides()
        return a[0] ** 3

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

