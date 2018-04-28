# Set to find differences

char_list = ['a','a','b','c','d','d']

print(char_list)
print(set(char_list)) # set用来去除所有相同的项,但是返回一个大括号的
print(type(set(char_list))) # 类型为set，乱序
print(type({1:2,2:3})) # 类型为字典

sentence = 'welcome to Beijingbbb'
print(set(sentence)) # 也可以处理数组

unique_char = set(char_list)
unique_char.add('x') # 加一个不同字母进去
# 如果加存在的，就啥都不发生
# 一次只能加一个字母，不能加多个
print(unique_char)
# unique_char.clear() # 清除全部
unique_char.remove('x') # 清除x字母,返回值是None,要看后来的话还得再调用
print(unique_char)
print(unique_char.remove('a')) # 仅仅是打印，但他也执行了去除命令
print(unique_char)
# remove 和 discard, 后者会

print('-------------')
set1 = {'a','b','c'}
set2 = {'b','c','d'}
print(set1.difference(set2)) # a有b没有
print(set1.intersection(set2)) # a有b也有