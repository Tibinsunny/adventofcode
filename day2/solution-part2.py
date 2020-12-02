import re
valid=0
with open('file.txt') as my_file:
    testsite_array = my_file.readlines()
for i in range(len(testsite_array)):
    pol=re.split('; |, |\-|:| |\n',testsite_array[i])
    letter_first_index=int(pol[0])
    letter_second_index=int(pol[1])
    # print(pol)
    # print(letter_first_index)
    # print(letter_second_index)
    # print(pol[4][letter_first_index-1])
    # print(pol[4][letter_second_index-1])
    if(pol[4][letter_first_index-1]==pol[2] and pol[4][letter_second_index-1]!=pol[2] or pol[4][letter_second_index-1]==pol[2] and pol[4][letter_first_index-1]!=pol[2] ):
        valid=valid+1
print(valid)
