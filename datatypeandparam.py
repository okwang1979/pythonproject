#coding:utf-8
message="Hello world!"
print(message)
# 字符串测试
message = 'Hello world2!'
print(message)
message = 'hEllo "world2"!'
print(message)
# 字符串函数 
print("title fun:"+message.title())
print("fun:"+message.upper())
# 去掉空白
message  = "     Hello  "
print(message+"!")
print(message.rstrip().lstrip()+"!")
# 乘方运算
num = 3+2
print(num**2)
# 使用str做数值的字符串转换
print("this is num:"+str(num))
# 列表
selfList = ["one",2,"three"]
print(selfList[1])
print(selfList[-1])
# 列表相关操作
selfList.append("four") # 末尾插入
print(selfList)
selfList.insert(4,"five") # 插入
print(selfList)
del selfList[-1] # 删除
print(selfList)