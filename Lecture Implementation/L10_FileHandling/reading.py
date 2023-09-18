try:
    file = open("Science", "r")  # with the r mode, the cursor will start at the beginning
    # and then go byte by byte through the entire file and read it
    # the mode r+ will enable both reading and writing but the cursor has to be moved to not overwrite
    print(file.read())  # parameter is no. of bytes; default is -1 meaning everything
    file.close()

    filer = open("Science", "r+")
    print(filer.read())
    filer.write("New Line")
    # since I am reading then writing, the cursor is moving to the end of the file before writing
    filer.close()

    files = open("Science", "r+")
    files.write("New Line")
    print(files.read())
    # the cursor overwrites the beginning of the file, and the reading resumes from where it stopped
    files.close()

except FileNotFoundError:  # if the file we are trying to read does not exist; is thrown in r modes
    print("File unavailable.")

"""
Possible questions:
- What will be the output if line 10 is added to the code under line 9? Under line 8?
- I would like to add the sentence "New Line" at the end/beginning of the text file. Complete the code.
- What is the content of the file after running the following code?
"""

f = open("colors.txt", "r")
counter = 1
for line in f.readlines():  # readlines returns a list
    print("Size of line", counter, 'is', len(line))
    print(line)
    counter += 1
f.close()
