class TreeReturn:
    def __init__(self, return_type, addr=None, code=""):
        self.type = return_type
        self.addr = addr
        self.code = code

    def get_type(self):
        return self.type

    def get_variable(self):
        return self.addr

    def __str__(self):
        return f"{self.type}-{self.addr}-{self.code}"