f1=open("file.txt","r")
xs=[int(x)for x in f1.read().splitlines()]
for loop1 in range(len(xs)):
    for loop2 in range(len(xs)):
        if(xs[loop1]+xs[loop2]==2020):
            print(xs[loop1],xs[loop2],xs[loop1]*xs[loop2])
           
