# PickleToSaveResult

import pickle

# 写入
a_dict = {1:2,3:4,5:6}
file = open('pickle_example.pickle','wb')
# 一般用.pickle结尾,'wb'表示用二进制写入
pickle.dump(a_dict,file)
# 把字典丢进去
file.close()

# 读取
file = open('pickle_example.pickle','rb')
# with open('pickle_example.pickle','rb') as file : 相同效果，而且不用close
a_dict1 = pickle.load(file)
file.close()
print(a_dict)
print(a_dict1)

# pickle可以存各种奇奇怪怪的数据结构