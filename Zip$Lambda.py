# Zip,lambda,map
# ZIP
a = [1,2,3,4,5,6,7]
b = [8,9,0,1,2,3]
c = zip(a,b) # 只这样子只是一个对象
print(c)
d = list(c) # 这样子才会被合成一个列表，对应的怼在一起，没有对应项的舍弃
print(d)

for i,j in zip(a,b): # objective 可以直接打印
    print(i/2,j*2)
for i,j in d:        # 这样子也蜜汁可以
    print(i/2,j*2)

e = list(zip(a,b,a,a)) # 多个拼合
print(e)

# LAMBDA
fun2 = lambda x,y:x+y
# 简单版本的小函数，前方为传参，后方为执行返回的内容
print(fun2(3,4))
print(fun2(0,0))

# MAP
g = map(fun2,[1,2,3,4],[4,5,6]) # 指定的函数，一组x,一组y,返回一组结果，如果没有对应的ｙ／ｘ，则舍弃
print(list(g))