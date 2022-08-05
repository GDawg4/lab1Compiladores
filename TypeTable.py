class TypeTable:
    def __init__(self):
        self.classes = {
            'Int': {
                'name': 'Int',
            },
            'Bool': {
                'name': 'Bool'
            },
            'String': {
                'name': 'String'
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

    def add_type(self, name, current_attributes, current_methods):
        self.classes[name] = {'name': name, 'attributes': current_attributes, 'methods': current_methods}

    def add_argument(self, name, type):
        self.arguments[name] = {'name': name, 'type': type}

    def type_exists(self, name):
        return name in self.classes
