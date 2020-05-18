import os
import random

class Student(object):
    # 类的两个属性
    name = ''
    age = 0
    # 初始化函数，赋值

    def __init__(self, name, age):
        self.name = name
        self.age = age
    

#自定义装饰器
def printName(func):
    def output(*args, **kw):
        print("正在处理中 ",args[0].name)
        return func(*args,**kw)
    return output

@printName
def cango(stu):
        if stu.age>=18:
            return True
        else:
            return False

def test():
    nameList=['李华','王雨','张三','Martin','Rico']
    stulist=[]
    admission=[]
    for i in range(5):
        stulist.append(
            #生成student对象并存入列表中
            Student(nameList[i],random.randint(10,25))
        )
    for item in stulist:
        if cango(item):
            print('满足条件:',item.age)
            admission.append(item.name)
        else:
            print('404',item.age)
    with open('one/homework/作业.txt','w',encoding='utf-8') as f:
        for name in admission:
            f.write(name)
test()