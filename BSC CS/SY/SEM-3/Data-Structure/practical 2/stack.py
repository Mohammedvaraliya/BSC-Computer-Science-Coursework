class Stack:

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print("Pushed item : " , item)

    def pop(self):
        if len(self.stack) < 1:
            print("The stack is empty you cant pop ")
            return

        pop = self.stack.pop()
        print("Popping item : ", pop)
        return pop
        
    def display_stack(self):
        print(self.stack)

    def size_of_stack(self):
        print(len(self.stack))

if __name__ == "__main__":
    stack = Stack()
    stack.push("1")
    stack.push("2")
    stack.push("3")
    stack.push("4")
    stack.push("5")
    stack.display_stack()

    stack.pop()
    stack.display_stack()

    stack.size_of_stack()