class TypeTable:
    def __init__(self):
        self.classes = {
            'Object': {
                'name': 'Object',
                'inheritance': None,
                'attributes': [],
                'methods': ['abort', 'type_name', 'copy'],
                'size': 0
            },
            'Int': {
                'name': 'Int',
                'inheritance': 'Object',
                'attributes': [],
                'methods': [],
                'size': 8
            },
            'Bool': {
                'name': 'Bool',
                'inheritance': 'Object',
                'attributes': [],
                'methods': [],
                'size': 1
            },
            'String': {
                'name': 'String',
                'inheritance': 'Object',
                'attributes': [],
                'methods': [],
                'size': 8
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

    def add_type(self, name, current_attributes, current_methods, inheritance=None, size=0):
        self.classes[name] = {
            'name': name,
            'attributes': current_attributes,
            'methods': current_methods,
            'inheritance': inheritance,
            'size': size
        }

    def add_argument(self, name, type):
        self.arguments[name] = {'name': name, 'type': type}

    def type_exists(self, name):
        return name in self.classes

    def get_size(self, name):
        if name in self.classes:
            return self.classes[name]['size']
        return 0

    def does_inherit(self, child, father):
        checking = True
        current_level = child
        while checking:
            if current_level in self.classes:
                if self.classes[current_level]['inheritance'] == father:
                    return True
                else:
                    current_level = self.classes[current_level]['inheritance']
            else:
                return False
        return False

    def exists_in_parent(self, child, thing):
        current = child
        attrs = []
        methods = []
        while True:
            if current in self.classes or current is not None:
                attrs += self.classes[current]['attributes']
                methods += self.classes[current]['methods']
                current = self.classes[current]['inheritance']
            else:
                break
        return thing in attrs or thing in methods
