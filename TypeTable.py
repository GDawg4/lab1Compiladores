class TypeTable:
    def __init__(self):
        self.classes = {
            'Object': {
                'name': 'Object',
                'inheritance': None
            },
            'Int': {
                'name': 'Int',
                'inheritance': 'Object'
            },
            'Bool': {
                'name': 'Bool',
                'inheritance': 'Object'
            },
            'String': {
                'name': 'String',
                'inheritance': 'Object'
            }
        }
        self.methods = {}
        self.attributes = {}
        self.arguments = {}

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
                    current_level = self.classes[current_level]['inheritance']
            else:
                return False
        return False
