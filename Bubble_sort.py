import sys

input_list = []

for i in range(1,len(sys.argv)):
    input_list.append(float(sys.argv[i]))

print('Input list = ',input_list)

for i in range (0,len(input_list)-2):
    for j in range(0,len(input_list)-2-i):
        if input_list[j] > input_list[j+1]:
            temp = []
            temp = input_list[j]
            input_list[j] = input_list[j+1]
            input_list[j+1] = temp

print('Input list after bubble sort: ',input_list)