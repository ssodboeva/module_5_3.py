class House:
    def __init__ (self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __str__ (self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"


    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self

    def __iadd__(self, value):
        return self.__add__(value)

    def __radd__(self, value):
        return self.__add__ (value)

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors


home_1 = House ('ЖК "Эльбрус"', 30)
home_2 = House ('ЖК "Акация"', 25)

print (home_1)
print (home_2)
print (home_1 == home_2)
home_2 + 5
print (home_2)
print (home_1 == home_2)
home_2 += 5
print (home_2)
home_1 = home_1 + 5
print (home_1)
print (home_1 < home_2)
print (home_1 <= home_2)
print (home_1 > home_2)
print (home_1 >= home_2)
print (home_1 != home_2)