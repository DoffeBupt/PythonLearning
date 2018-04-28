a = [1,2,3,4] # 列表
d = {'apple':1,'pear':2,'orange':'wa'} # 前方为键后方为值
print(d['apple']) # 输出键为apple的对应的值
del d['pear'] # 删除键为pear的键值对
print(d)
d['banana']=333 # 插入一个键值对
print(d) # 随机插入，说明字典内实际上内部不会区分顺序
def fun():
    print('fun()被蜜汁调用了？？')

def fun1():
    print('fun1()也被蜜汁调用了？？')
dd = {'apple':1, 'pear':{1:2,'bb':3,'3':fun1()}, 'orange':fun()} # 字典可以嵌套,也可以丢函数进去
# 建立的时候好像会自动调用所有的函数一次
# 内嵌的函数不知道咋调用，而且莫名会被调用，尽量先不管他好了
print(dd['pear']['bb']) # 多重寻找
# dd['pear']['3']