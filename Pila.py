class Stack():
    def __init__(self):
        self.list = []

    def push(self, element):
        self.list.append(element)

    def pop(self):
        if len(self.list) > 0:
            return self.list.pop()
        else:
            return None

    def size(self):
        return len(self.list)

    def peek(self):
        if len(self.list) > 0:
            return self.list[len(self.list) - 1]
        else:
            return None

    def empty(self):
        if len(self.list) > 0:
            return False
        else:
            return None



objeto1 = Stack()
objeto1.push("Libro_1")
objeto1.push("Libro_2")
objeto1.push("Libro_3")
print(objeto1.list)
print("Ultimo elemento de la lista " + objeto1.peek())
print(objeto1.pop())
print(objeto1.list)
