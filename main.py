from blob import Blob
from goobmeld import Goobmeld


class App:
    def __init__(self):
        # initalizing blob
        goobmeld = Goobmeld(25)
        blob = Blob("blob", 10, goobmeld)
        print(blob.die_value)
        blob.roll_area_die()
        print(blob)

        # blob rolls a die to determine whether it grows or shrinks
        # blob rolls die
        # we print new blob size


# initialize app
App()
