#Write a program that reverse strings.
#The program asks the user to enter a name.
#The program takes each letter and stores it in a stack.
#The program pops the letters and print the reversed name at the end.

class stackImplementation:
    
    def __init__(self):
        self.lst = []
        
    def push(self, n):
        #listname.append(value)
        self.lst.append(n)
        
    def pop(self):
        poped = self.lst.pop()
        return poped
        
def main():
    
    
    
main()