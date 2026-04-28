class MyLife:
    def __init__(self, file_name):
        self.file_name = file_name

    def write_lines(self):
        with open(self.file_name, 'w') as file:
            while True:
                