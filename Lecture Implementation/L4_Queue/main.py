class Queue:

    def __init__(self):
        self.__queue = []  # Without capacity because it's easier to work with a queue this way

    def enqueue(self, val):
        self.__queue.append(val)

    def dequeue(self):
        return self.__queue.pop(0)

    def __str__(self):
        return str(self.__queue)


def main():
    q = Queue()  # can instantiate an object without a variable
    # the variable just stores a reference in the memory for ease of access to the object
    q.enqueue(5)
    q.enqueue(6)
    q.enqueue(7)
    q.dequeue()
    print(q)
    print(q.dequeue())
    print(q)


main()