from blob import Blob

class App:
    def __init__(self):
        #initalizing blob
        blob = Blob("blob", 10)
        print(blob.die_value)
        blob.roll_die()
        print(blob.die_value)
        blob.adjust_size()

        print(blob)

        # blob rolls a die to determine whether it grows or shrinks
        # blob rolls die
        # we print new blob size

#initialize app
App()
