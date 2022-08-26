class SymbolTable:
    def __init__(self):
        self.symbol_table = [
            {
                'out_string': {
                    'name': 'out_string', 'type': 'SELF_TYPE', 'arguments': []
                },
                'abort': {
                    'name': 'abort', 'type': 'Object', 'arguments': []
                },
                'mOut': {
                    'name': 'mOut', 'type': 'Int'
                }
            }
        ]

    def get_symbol_table(self):
        return self.symbol_table

    def peek(self):
        return self.symbol_table[-1]

    def add_scope(self):
        self.symbol_table.append({})

    def add_symbol(self, name, type_name, arguments=None):
        self.symbol_table[-1][name] = {'name': name, 'type': type_name, 'arguments':arguments}

    def remove_scope(self):
        self.symbol_table.pop()

    def check_for_symbol(self, name):
        for i in self.symbol_table:
            if name in i:
                return True
        return False

    def find_symbol(self, name):
        for i in self.symbol_table:
            if name in i:
                return i[name]['type']
        return name
        # return self.symbol_table[-1][name]['type']

    def get_params(self, name):
        for i in self.symbol_table:
            if name in i:
                return i[name]['arguments']
        return []