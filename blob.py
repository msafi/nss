# import threeSidedDie from die.py
from die import Die


# blob class
class Blob:
    die = Die(3)
    areadie = Die(100)

    def __init__(self, name, size):
        self.die_value = self.die.roll()
        self.name = name
        self.areadie_value = self.areadie.roll
        # hibity hopity
        if self.areadie_value == 1:
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

    def roll_areadie(self):
        self.areadie_value = self.areadie.roll

    def __str__(self):
        return (
            f"Blob(name={self.name}, size={self.size}, location={self.areadie_value})"
        )

    def adjust_size(self):
        if self.die_value == 1:
            self.size = self.size - 1
        elif self.die_value == 2:
            self.size = self.size
        else:
            self.size = self.size + 1
