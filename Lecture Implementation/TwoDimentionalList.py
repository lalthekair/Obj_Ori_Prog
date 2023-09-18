def twoDimentionalList():
    
    lst = [[0,0,0,5],[0,0,0,77],[0,0,60,30]]

#of inner lists = rows
#of elements in the inner list = columns

    for x in range(3):    
        for y in range(4):
        #ListName [r][c]
            if y % 2 == 0:
                lst[x][y] = 10
            if y % 2 == 1:
                lst[x][y] = 5
                
    print(lst)
    
twoDimentionalList()

