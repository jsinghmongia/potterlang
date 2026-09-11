class Environment:
    def __init__(self, parent=None):
        self.values = {}
        self.parent = parent

    def define(self, name: str, value):
        curr = self
        while curr is not None:
            if name in curr.values:
                curr.values[name] = value
                return
            curr = curr.parent
        self.values[name] = value

    def assign(self, name: str, value):
        if name in self.values:
            self.values[name] = value
            return
        if self.parent:
            self.parent.assign(name, value)
            return
        raise NameError(f"Cannot assign to undefined variable '{name}'.")

    def get(self, name: str):
        if name in self.values:
            return self.values[name]
        if self.parent:
            return self.parent.get(name)
        raise NameError(f"Undefined variable '{name}'.")