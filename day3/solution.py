k=3
flag=0;
p=[]
with open('file.txt') as my_file:
    testsite_array = my_file.readlines()
# print(((testsite_array[0].strip())*len(testsite_array))[31])
for i in range(1,len(testsite_array)):
    if(((testsite_array[i].strip())*len(testsite_array))[k]=="#"):
        flag=flag+1
    k=k+3
# for i in range(1,len(testsite_array)):
#     if((testsite_array[i]*i)[k]=="#"):
#         flag=flag+1
#     k=k+3
print(flag)
