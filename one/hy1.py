class student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age



def dun(now):
    def judge(*args,**kw):
        n = now(*args)
        if(n < 18):
            print('不可以去网咖')
        else:
            print('可以去网咖')
    return judge


@dun
def now(student):
    print(student.name)
    return student.age


l1 = student('李三', 13)
l = [l1]


now(l1)
