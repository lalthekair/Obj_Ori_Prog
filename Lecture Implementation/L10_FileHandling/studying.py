f = open('colors.txt', 'w')

f.write('Blue - Violets')
f.write('\nRed - Roses')
f.write('\nYellow - Daffodil')
f.write('\nWhite - Daisy')
f.write('\nPink - Tulip')
f.write('\nBlack - Nightshade')
f.write('\nGrey - Lily')

f.close()

"""f = open('colors.txt', 'r')
for x in f.readlines():
    print('an example of flowers colored', x)
print(f.readline())  # doesn't return anything because cursor is at the end of the file
print()
f.close()"""

f = open('colors.txt', 'r+')
"""for x in f.readlines():
    print('an example of flowers colored', x)
# since the cursor moved, we will not be overwriting anything"""
# f.write('\nOrange - Hydrangea')
print(f.read())
f.close()  # to move cursor back to beginning
f = open('colors.txt', 'w+')
print(f.read(4))  # reads only first 4 bytes
print(f.readline())  # prints remaining of line
print(f.readlines())
f.close()