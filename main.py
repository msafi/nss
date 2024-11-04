from blob import Blob
from environment import Environment


class App:
    def __init__(self):

        environment = Environment(25)

        environment.create_blob(name="blob", size=10)
        environment.create_blob(name="blob2", size=12)

        print(environment)
        # initalizing blob
        # blob = Blob("blob", 10, goobmeld)
        # blob2 = Blob("blob2", 20, goobmeld)

        # list_of_blobs = [blob, blob2]

        # # iterate over the list of blobs and print them
        # for b in list_of_blobs:
        #     print(b)

        # # # filter out blobs that have a size larger than 5
        # # large_blobs = [b for b in list_of_blobs if b.size > 5]

        # print(blob.die_value)
        # blob.roll_area_die()
        # print(blob)
        # print(goobmeld)
        # print("THE NEXT ROUND!")
        # blob.CONSUME_GOOBMELD()
        # print(goobmeld)
        # # blob rolls a die to determine whether it grows or shrinks
        # # blob rolls die
        # # we print new blob size


# initialize app
App()
