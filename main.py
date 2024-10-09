from blob import Blob

class App:
    def run(self):
        #initalizing blob
        blob = Blob("blob", 10)
        print(blob)

        # blob rolls a die to determine whether it grows or shrinks
        # blob rolls die
        # we print new blob size

#initialize app
app = App()
app.run()
