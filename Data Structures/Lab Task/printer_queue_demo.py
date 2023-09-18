import climage
from printer_queue import LinkedList


def main():
    printer = climage.convert("printing.png", width=40)
    print(printer)
    print("This software manages all tasks sent to my printer.\nIt is implemented as a part of Fundamental "
          "Data Structures Labs.\n\n")
    ll = LinkedList()
    print("Banana image is sent to the printer.")
    ll.add_request("banana.png", climage.convert("banana.png", width=40))
    print("Apple image is sent to the printer.")
    ll.add_request("apple.png", climage.convert("apple.png", width=40))
    print("Kiwi image is sent to the printer.")
    ll.add_request("kiwi.png", climage.convert("kiwi.png", width=40))
    print("\nNow, let's check the number of files waiting in the queue ...")
    print(ll.list_len(), 'elements are waiting to be printed.\n')

    print('Printing the first element ...')
    ll.process_request()
    print('Printing the second element ...')
    ll.process_request()
    print('Printing the third element ...')
    ll.process_request()


main()