import random

from blob import Blob


class Environment:
    blobs = []

    cells = [i for i in range(1, 101)]

    cells_with_food = [random.randint(1, 100) for i in range(25)]

    def __init__(self, food_amount=25):
        self.food_amount = food_amount

    def create_blob(self, name, size):
        blob = Blob(name, size, self)
        blob_cell_index = random.choice(self.cells)

        # blob, cell tuple
        blob_tuple = (blob, blob_cell_index)
        self.blobs.append(blob_tuple)

    def begin(self):
        """
        This method is called when the simulation begins
        """
        # for each blob, run .eat() method
        for blob_tuple in self.blobs:
            blob = blob_tuple[0]
            blob.eat()

    def print_blobs(self):
        for blob in self.blobs:
            print(blob)

    def __str__(self):
        number_of_blobs = f"Number of blobs: {len(self.blobs)}\n\n"

        cells_with_food = f"Cells with food: {self.cells_with_food}\n\n"
        cells = f"Cells: {self.cells}\n\n"

        blobs_str = ", ".join(str(blob_tuple[0]) for blob_tuple in self.blobs)
        blobs = f"Blobs: {blobs_str}\n\n"

        return number_of_blobs + cells_with_food + blobs + cells
