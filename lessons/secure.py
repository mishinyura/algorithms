class Chif:
    def __init__(self, data: str):
        self.data = data
        if len(data) < 256:
            pass

    def increase_size(self):
        while len(self.data) < 256:
            break

