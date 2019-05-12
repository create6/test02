#! /usr/bin/python3.5

#冒泡排序

def swap(c_list,idx1,idx2):
    #交换函数
    tmp = c_list[idx1]
    c_list[idx1] = c_list[idx2]
    c_list[idx2] = tmp

def sort_list(c_list):
    i = 0
    while i < len(c_list)-1:
        j =0 
        while j < len(c_list) - i -1:
            if c_list[j] > c_list[j+1]:
                swap(c_list,j,j+1)
            j += 1
        i += 1
c_1 = [9,7,2,6,10,3,4]
sort_list(c_1)
print(c_1)

