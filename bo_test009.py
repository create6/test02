#! /usr/bin/python3.5


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

