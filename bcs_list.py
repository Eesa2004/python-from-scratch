class node:
    value = None
    next = None

    def __init__(self, v, n=None):
        self.value = v
        self.next = n

    def append(self, newNode):
        self.next = newNode


class bcs_list:
    head = None

    def get(self, index):
        if self.head == None:
            raise IndexError("No such index in list")

        runner = self.head
        while index > 0:
            if runner.next == None:
                raise IndexError("No such index in list")
            runner = runner.next
            index -= 1

        return runner.value

    def append(self, newValue):
        if self.head == None:
            self.head = node(newValue)

        else:
            runner = self.head
            while runner.next != None:
                runner = runner.next

            runner.append(node(newValue))

    def remove(self, index):
        value = self.get(index)

        if index == 0:
            self.head = self.head.next

        else:
            runner = self.head
            while index > 1:
                if runner.next == None:
                    raise IndexError("No such index in list")
                runner = runner.next
                index -= 1

            if runner.next != None:
                runner.next = runner.next.next

        return value

    def length(self):
        length = 0

        if self.head != None:
            runner = self.head
            length += 1

            while runner.next != None:
                runner = runner.next
                length += 1

        return length

    def clear(self):
        self.head = None
