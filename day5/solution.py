import math
f = open('file.txt').read()
results=[]
array=f.split("\n")
for i in range(len(array)):
    beg=0
    end=127
    col_beg=0
    col_end=7
    for j in range((len(array[i])-3)):
        if(array[i][j]=="F"):
            end=(end-beg)/2 
        if(array[i][j]=="B"):
            beg=(beg-end)/2
        #print("Begingin",math.ceil(abs(beg)),"End",math.floor(abs(end)))   
    for k in range(7,len(array[i])): 
        if(array[i][k]=="L"):
            col_end=(col_end-col_beg)/2
        if(array[i][k]=="R"):
            col_beg=(col_beg-col_end)/2
       # print("Column beg",math.ceil(abs(col_beg)),"Column End",math.floor(abs(col_end)))
   # print("Row",math.floor(abs(end)),"Column",math.floor(abs(col_end)))
    results.append((math.floor(abs(end))*8)+math.floor(abs(col_end)))
    results.sort()
print("Largest Is :", results[-1])
            
            
            #