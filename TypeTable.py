class TypeTable:
    def __init__(self):
        self.classes = {
            'Object': {
                'name': 'Object',
                'inheritance': None,
                'attributes': [],
                'methods': ['abort', 'type_name', 'copy'],
            },
            'Int': {
                'name': 'Int',
                'inheritance': 'Object',
                'attributes': [],
                'methods': []
            },
            'Bool': {
                'name': 'Bool',
                'inheritance': 'Object',
                'attributes': [],
                'methods': []
            },
            'String': {
                'name': 'String',
                'inheritance': 'Object',
                'attributes': [],
                'methods': []
            },
            'IO': {
                'name': 'IO',
                'inheritance': 'Object',
                'attributes': [],
                'methods': ['out_string', 'out_int', 'in_string', 'in_int']
            }
        }
        self.methods = {
            'abort': {
                'name': 'abort',
                'arguments': [],
                'return_type': 'Object'
            },
            'type_name': {
                'name': 'type_name',
                'arguments': [],
                'return_type': 'String'
            },
            'copy': {
                'name': 'copy',
                'arguments': [],
                'return_type': 'SELF_TYPE'
            },
            'out_string': {
                'name': 'out_string',
                'arguments': ['xS'],
                'return_type': 'SELF_TYPE'
            },
            'out_int': {
                'name': 'out_int',
                'arguments': ['xI'],
                'return_type': 'SELF_TYPE'
            },
            'in_string': {
                'name': 'in_string',
                'arguments': [],
                'return_type': 'String'
            },
            'in_int': {
                'name': 'in_int',
                'arguments': [],
                'return_type': 'Int'
            },
            'length': {
                'name': 'length',
                'arguments': [],
                'return_type': 'Int'
            },
            'concat': {
                'name': 'concat',
                'arguments': ['sCon'],
                'return_type': 'String'
            },
            'substr': {
                'name': 'substr',
                'arguments': ['iSub', 'lSub'],
                'return_type': 'String'
            }
        }
        self.attributes = {
        }
        self.arguments = {
            'xS': {
                'name': 'xS',
                'type': 'String'
            },
            'xI': {
                'name': 'xI',
                'type': 'Int'
            },
            'sCon': {
                'name': 'sCon',
                'type': 'String'
            },
            'iSub': {
                'name': 'iSub',
                'type': 'Int'
            },
            'lSub': {
                'name': 'lSub',
                'type': 'Int'
            }
        }

    def get_classes(self):
        return self.classes

    def get_methods(self):
        return self.methods

    def get_attributes(self):
        return self.attributes

    def get_arguments(self):
        return self.arguments

    def add_attribute(self, name, type):
        self.attributes[name] = {'name': name, 'type': type}

    def add_method(self, name, arguments, return_type):
        self.methods[name] = {'name': name, 'arguments': arguments, 'return_type': return_type}

    def add_type(self, name, current_attributes, current_methods, inheritance=None):
        self.classes[name] = {'name': name, 'attributes': current_attributes, 'methods': current_methods, 'inheritance': inheritance}

    def add_argument(self, name, type):
        self.arguments[name] = {'name': name, 'type': type}

    def type_exists(self, name):
        return name in self.classes

    def does_inherit(self, child, father):
        checking = True
        current_level = child
        while checking:
            if current_level in self.classes:
                if self.classes[current_level]['inheritance'] == father:
                    return True
                else:
                    current_level = self.classes[current_level]['inheritancet']
            else:
                return False
        return False
