from debug_log import log


# blob class
class Blob:
    def __init__(self, name, size, environment):
        log(f'Blob "{name}" initialized, size={size}')

        self.name = name
        self.environment = environment
        self.size = size

    def eat(self):
        log(f'Blob "{self.name}" wants to eat')
        blob_cell = self.environment.get_blob_cell(self)

        if blob_cell in self.environment.cells_with_food:
            self.size += 1
            log(f'Blob "{self.name}" ate and grew to size {self.size}')
        else:
            self.size -= 1
            log(f'Blob "{self.name}" did not eat and shrunk to size {self.size}')

    def __str__(self):
        return f"{self.name}(name={self.name}, size={self.size})"
