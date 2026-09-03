#opening a file 'r' mode (reading mode) 
f = open('board.txt', 'r')
#f for file object and then anything
print(f.name)
#close the file 
f.close()