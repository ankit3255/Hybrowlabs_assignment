def Create_stack():
    stack = []
    return stack
def Is_empty(stack):
    x = len(stack)
    return x == 0


def push(stack,item):
    stack.append(item)
    print("Here is pushed element : ", item)

def pop(stack):
    if(Is_empty(stack)):
        return "stack is empty"
    return stack.pop()

def peek(stack):
    if(Is_empty(stack) == 0):
        return stack[-1]

stack = Create_stack()
push(stack, str(1))
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))
print("popped item: " + pop(stack))
print("stack after popping an element: " + str(stack))