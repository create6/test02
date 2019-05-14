#! /c/Users/struggle6/AppData/Local/Programs/Python/Python37/python

'''
框架程序，处理业务逻辑
'''

import pymysql
import json

route_dict = {}


# 路由装饰器
def route(str_key):
    def route_(func):
        # 装饰器自动执行处，添加方法名至路由字典
        route_dict[str_key] = func
        def fn_in(*args,**kwargs):
            func(*args,**kwargs)
        return fn_in
    return route_


@route('/login.html')
def login():
    status = "200 OK"
    headers = [("Server","python12/2.0")]
    response_body = "登录页面"
    return status , headers , response_body


@route('/index.html')
def index():
    status = "200 OK"
    headers =[("Server","python12.2.0")]
    with open('框架代码/templates/index.html','r')as f:
        response_body = f.read()

  # 查询数据库，把数据替换到 response_body 这个字符串中
    try:
        conn1 = pymysql.connect(host="localhost", port=3306, user="root", password="mysql", database="stock",charset="utf8")
    except:
        print('数据库出错！')
  #   conn1 = pymysql.connect(host="localhost", port=3306, user="root", password="mysqltt", database="stock",charset="utf8")
    cs = conn1.cursor()
    # 执行sql语句
    sql = "select * from info;"
    cs.execute(sql)
    # 获取数据
    data = cs.fetchall()  # 获取到的数据是元组
    cs.close()
    conn1.close()

    # 准备要替换成的数据
    html = ''
    for i in data:  # i 就是 (1, '000007', '全新好', '10.01%', '4.40%', Decimal('16.05'), Decimal('14.60'), datetime.date(2017, 7, 18))
        html += '<tr><td>' + str(i[0]) + '</td><td>' + i[
            1] + '</td><td>'+i[2]+'</td><td>'+i[3]+'</td><td>'+i[4]+'</td><td>'+str(i[5])+'</td><td>'+str(i[6])+'</td><td>'+str(i[7])+'</td><td><input type="button" value="添加" id="toAdd" name="toAdd" systemidvaule="000007"></td></tr>'

        # 替换数据———— 把data数据放入response_body里面去，放在{%content%}的位置上，把它替换掉
    response_body = response_body.replace("{%content%}",html)

    return status, headers, response_body



@route('/center.html')
def center():
    status = "200 OK"
    headers = [("Server","python12/2.0")]
    with open('框架代码/templates/center.html','r')as f:
        response_body = f.read()

    # 1 准备要替换成的数据
    conn1 = pymysql.connect(host="localhost", port=3306, user="root", password="mysql", database="stock",charset="utf8")
    cs = conn1.cursor()
    # 执行sql语句
    sql = "select i.code,i.short,i.chg,i.turnover,i.price,i.highs,f.note_info from info as i  inner JOIN   focus as f on i.id = f.info_id;"
    cs.execute(sql)
    # 获取数据
    data = cs.fetchall()  # 获取到的数据是元组
    cs.close()
    conn1.close()
    # 替换数据
    # 2、把查询出来的数据转换成json格式的字符串
    # (('000007', '全新好', '10.01%', '4.40%', Decimal('16.05'), Decimal('14.60'), "你确定要买这个？"),......)
    data_list=[]
    for i in data:
        data_list.append({
            "code":i[0],
            "short":i[1],
            "chg":i[2],
            "turnover": i[3],
            "price": str(i[4]),
            "highs": str(i[5]),
            "note_info": i[6]
        })
    # 转成json格式的字符串
    json_str = json.dumps(data_list)
    # response_body = response_body.replace("{%content%}", json_str)


    return status ,headers ,json_str

def page_404():
    status = "404 NOT FOUND"
    headers = [("Server","python12/2.0")]
    with open('框架代码/static/404.html','r') as f:
        response_body = f.read()




    return status ,headers , response_body

# 调用路由字典
def application(file_path):
    # 加入异常处理

    return route_dict[file_path]()  # 不加异常处理可以看到出错原因,等收尾时再加入异常处理
    # try:
    #     return route_dict[file_path]()
    # except:
    #     return page_404()



# if __name__ == '__main__':
#
#     application('/index.html')
    # application('/xx.html')
