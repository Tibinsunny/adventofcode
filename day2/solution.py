import re
valid=0
with open('file.txt') as my_file:
    testsite_array = my_file.readlines()
for i in range(len(testsite_array)-1):
    pol=re.split('; |, |\-|:| |\n',testsite_array[i])
    occurance=pol[4].count(pol[2])
    if(occurance>=int(pol[0]) and occurance<=int(pol[1])):
        valid=valid+1
print("No Of total Valid Conditions are =",valid)
    
    
    # occurence=pol.count(flag)
    # print(occurence)
# pol=re.split('; |, |\-|:| |\n',testsite_array[4])
# print(pol)
