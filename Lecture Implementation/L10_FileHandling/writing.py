"""
The steps when it comes to file handling:
1. open
2. access mode (read, write, ...)
3. close

Access modes:
w - write (overwrite)
a - append
r - read
The program only has ONE permission per these modes
"""

try:
    # 1
    file = open("Science", "w")  # second parameter is one of six access modes; the reason to open the file

    # 2
    file.write("Burritos are superior to tacos because they don't have shells that make your mouth roof bleed.")
    file.write("\nWill this append? Will this overwrite? Who knows?")
    # since the file was already open, it will not be overwritten when I write stuff here (between open - close)
    # reading not allowed

    # 3
    file.close()

except ValueError:
    print("Forbidden operation.")


# w and w+ modes, when opening a file, will overwrite everything in the file to empty
# slide 15