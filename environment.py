from blob import Blob


class Environment:
    blobs = []

    def __init__(self, food_amount=25):
        self.food_amount = food_amount

    def create_blob(self, name, size):
        blob = Blob(name, size, self)
        self.blobs.append(blob)
        return blob

    def print_blobs(self):
        for blob in self.blobs:
            print(blob)

    def __str__(self):
        return f"Environment(food_amount={self.food_amount}, blobs={len(self.blobs)})"
