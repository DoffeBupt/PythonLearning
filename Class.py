class Calculator:
        # 固有属性
        name = 'Good Calculator'
        price = 18
        # 功能
        # init函数，构造函数
        # 可以用来初始化属性
        # 可以设置默认参数
        def __init__(self,name,price = 1,height = 2,width = 3):
            self.name = name
            self.price = price
            self.hight = height
            self.width = width
        def add(self,x,y):
            # 引入self，这样可以调用类内的属性
            # 类外用.就可以调用，类内用self调用
            print(self.name)
        def minus(self,x,y):
            print(self.name)