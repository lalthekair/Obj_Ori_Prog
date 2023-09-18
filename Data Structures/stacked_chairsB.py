from chair import Chair
from linkedstackB import LinkedStack


def main():
    chair_stack = LinkedStack()
    chair1 = Chair("Blue")
    chair2 = Chair("Red")
    chair3 = Chair("Purple")
    print("Adding 3 chairs to the stack...")
    chair_stack.push(chair1)
    chair_stack.push(chair2)
    chair_stack.push(chair3)
    # chair_stack.list_stack_items()

    chair_stack.temporary()

    print("\nPerforming a few operations to re-arrange the stacked chairs:...")
    while not chair_stack.is_empty():
        chair_stack.pop()
    chair_stack.push(chair1)
    chair_stack.push(chair3)
    # chair_stack.list_stack_items()
    chair_stack.temporary()
    print("\nEmptying the stack of chairs...")
    while not chair_stack.is_empty():
        chair_stack.pop()
    print("\nAttempting to list the stack items:")
    # chair_stack.list_stack_items()
    chair_stack.temporary()
    print("\nAttempting to pop a chair from an empty stack:")
    chair_stack.pop()


main()
