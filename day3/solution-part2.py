k5=1
k2=3
k1=1
k3=5
k4=7
flag1=flag2=flag3=flag4=flag5=0
with open('file.txt') as my_file:
    testsite_array = my_file.readlines()
# print(((testsite_array[0].strip())*len(testsite_array))[31])

for i in range(2,len(testsite_array),2):
    if(((testsite_array[i].strip())*len(testsite_array))[k5]=="#"):
        flag5=flag5+1
    k5=k5+1


for i in range(1,len(testsite_array)):
    if(((testsite_array[i].strip())*len(testsite_array))[k4]=="#"):
        flag4=flag4+1
    k4=k4+7

for i in range(1,len(testsite_array)):
    if(((testsite_array[i].strip())*len(testsite_array))[k3]=="#"):
        flag3=flag3+1
    k3=k3+5

for i in range(1,len(testsite_array)):
    if(((testsite_array[i].strip())*len(testsite_array))[k2]=="#"):
        flag2=flag2+1
    k2=k2+3
for i in range(1,len(testsite_array)):
    if(((testsite_array[i].strip())*len(testsite_array))[k1]=="#"):
        flag1=flag1+1
    k1=k1+1

print(flag1*flag2*flag3*flag4*flag5)