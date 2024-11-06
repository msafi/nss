# blob class
class Blob:
    def __init__(self, name, size, environment):
        self.name = name
        self.environment = environment
        self.size = size

    def eat(self):
        blob_cell = self.environment.get_blob_cell(self)

        if blob_cell in self.environment.cells_with_food:
            self.size += 1

        print(self, "is eating")

    def __str__(self):
        return f"{self.name}(name={self.name}, size={self.size})"
