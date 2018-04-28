import copy
a = [1,2,3]
b = a # b的索引指到a的索引
print(id(a))
print(id(b))
# 此时a,b的都相当于一个指针
# id 即为查看他们的索引
# 改ａ，改ｂ都会去在那个地址产生影响
a[2] = 33
print(a)
print(b)
# 改了ａ去看ｂ，ｂ也变了
c = copy.copy(a)
print (id(a) == id(b)) # a,b同地址
print (id(b) == id(c)) # b,c不是一个地址
# 相当于在一个新的地址复制了一遍
d = [1,2,[3,4]] # 第三组可能相当于还是一个指向那个[3,4]的地址
e = copy.copy(d)
print('-------------')
print(id(d)==id(e))       # 输出为Flase
print(id(d[2])==id(e[2])) # 输出为True
# 相当于只复制了一层
# 第二层那个位置实际上还是一个地址
# 所以还是被调进来
f = copy.deepcopy(d)      # 超牛逼的copy,全部层都复制的
print('-------------')
print(id(f)==id(d))       # 输出为Flase
print(id(f[2])==id(d[2])) # 输出为Flase
# deepcopy 所有层全部打包带走
