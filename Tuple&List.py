a0_tuple = (1,2,3,4,5)
a1_tuple = 2,4,5,6,7



# 列表与数组的迭代

# a_list = [1,2,3,4,5,6]
# for content in a_list: # 迭代输出一个个值（列表）
#     print(content)
#     # content在执行完代码后竟然不会被杀掉
#
# for content in a0_tuple: # 迭代一个个值（元组）
#      print(content)
#
# for index in range(len(a_list)):
#     # range(5)=>(0,1,2,3,4)
#     print(a_list[index])

# 列表的一些命令

# a2 = [1,2,3]
# a2.append(0) # 在a2的最后加上０
# print(a2)
# a2.insert(1,0) # 在１的位置加上０
# print(a2)
# a2.remove(2) # 第一个出现的设定的值(2)
# print(a2)
# print(a2[2]) # 打印第二位
# print(a2[-1]) # 打印最后那个
# print(a2[1:3]) # 从1到3位(3忽略)
# print(a2[1:]) # 从第一位往后
# print(a2.index(3)) # 返回第一次出现3的索引
# print(a2.count(0)) # 出现０的次数
# a3 = a2.sort() # 只要出现，默认会覆盖掉a2
# print(a2) # 对a2进行排序，从小到大
# a2.sort(reverse=True)
# print(a2) # 从大到小

# 多维列表
a = [1,2,3,4,5,6,7] # 一维list
multi_dim_a = [[2,3,4],
               [1,2,3],
               [3,4,5]] # 多维list
print(a[1])
print(multi_dim_a[2])
print(multi_dim_a[0][2])
