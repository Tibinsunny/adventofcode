f1=open("file.txt","r")
#xs=[for int(value) in f1.read().splitlines()]
xs=[int(value) for value in f1.read().splitlines()]
for loop1 in range(len(xs)):
    for loop2 in range(len(xs)):
        for loop3 in range(len(xs)):
            if(xs[loop1]+xs[loop2]+xs[loop3]==2020):
                print(xs[loop1],xs[loop2],xs[loop1]*xs[loop2]*xs[loop3])
            
