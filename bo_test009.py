#! /usr/bin/python3.5
import numpy as np 

def pro_c(func):
    def fn_in(*args,**kwargs):
        list_1 = [i for i in range(10)]
        print(list_1)
        func(*args,**kwargs)
    return fn_in

@pro_c
def my_test():
    print('my_git@github.com:create6/test02.git')
    print('my_decorate')

my_test()


arr1 = np.arange(0,20,2)
arr1 = arr1.reshape(-1,1)
arr2 = np.ones((10,1))
#arr3 = np.dot(arr1,arr2)
arr3 = arr1 +arr2

print(arr3)
#print(arr2)
#print(arr1)
print(arr1.shape)


