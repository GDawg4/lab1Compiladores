class TreeReturn:
    def __init__(self, return_type):
        self.type = return_type

    def get_type(self):
        return self.type

    def __str__(self):
        return f"{self.type}"