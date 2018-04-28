# import 现有的模块
# import time # 第一种加载模块的方法
# import time as t # 第二种改名办法
# from time import time,localtime # 只调用模块，用之前直接localtime就可以
# from time import * # 全部引入，而且不用写time.
# print(time.localtime())
# print(t.localtime())

# 测试自己建立的模块
import CreatPackageTest
CreatPackageTest.testfun()

# 外部模块 /usr/bin, /usr/local/bin 里


