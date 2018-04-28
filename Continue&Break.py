# # pass大法
# a = True
# while a:
#     b = input('typesth:')
#     if b == '1':
#         a = False
#     else:
#         pass

# break
# while True:
#     b = input('typesth:')
#     if b == '1':
#         break # 执行到这里，直接跳出循环
#     else:
#         pass
#     print("没跳出")
# print("跳出循环啦")

while True:
    b = input('typesth:')
    if b == '1':
        continue # 执行到这里，不管循环后边内容，重新进行循环
    else:
        pass
    print("没跳出")
print("跳出循环啦")
