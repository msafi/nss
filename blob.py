# import threeSidedDie from die.py
from die import Die


# blob class
class Blob:
    die = Die(3)
    area_die = Die(100)

    def __init__(self, name, size):
        self.name = name

        self.roll_die()
        self.roll_area_die()

        if self.die_value == 1:
            self.size = size - 1
        elif self.die_value == 2:
            self.size = size
        else:
            self.size = size + 1

    def grow(self, amount):
        self.size += amount

    def shrink(self, amount):
        self.size = max(0, self.size - amount)

    def roll_die(self):
        self.die_value = self.die.roll()

    def roll_area_die(self):
        self.area_die_value = self.area_die.roll()

    #   # def food_check(self):
    #        if self.area_die.roll() < food_amount + 1:

    def __str__(self):
        return (
            f"Blob(name={self.name}, size={self.size}, location={self.area_die_value})"
        )

    def agust_size(self):
        if self.die_value == 1:
            self.size = self.size - 1
        elif self.die_value == 2:
            self.size = self.size
        else:
            self.size = self.size + 1
