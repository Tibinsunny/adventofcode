f = open('file.txt').read()
flag = 0
valid=0
sum=0
array=f.strip().split('\n\n')
# print(array)
required= ['iyr','ecl','pid','eyr','hcl','byr','hgt']
for i in range(len(array)):
    sum=0
    for j in range(len(required)):
        if(required[j] in array[i]):
            sum=sum+1
        if(sum==7):
            valid=valid+1
print(valid)


