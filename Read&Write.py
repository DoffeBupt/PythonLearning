append_text = "aaa"
myfile = open("aaa.txt","w")
# 此时myfile相当于一个文件，内容在file.read()里
# ｗ:写入(完全重写)，ｒ:读入,不可写，ａ:多写点, append
# 有行数的在readline里,readline一次一行,readlines一次全部,存在列表里
myfile.write("aaa")
myfile.close() # 不要忘记关掉
myfile = open("aaa.txt","r")
print(myfile.read())
myfile.close()