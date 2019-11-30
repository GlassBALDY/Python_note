#==================  第8章  用户输入与while循环  =================#
##########  7.1  函数input()的工作原理

#从input命令中获取一道"文本"
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

Name = input('Tell me your name: ')
print("Hello,", Name + "!")

###########  7.1.1  编写清晰的程序

#选择字符变量作为input()中的提示符
prompt = "If you tell us who you are, we can personalize the messages you see"
prompt += "\nWhat is your name?"
name = input(prompt)
print("Hello, " + name + "!")

###########  7.1.2  使用int()获取数值型输入
age = input("How old are you? ")
#age接受到一个字符型变量，不能与数字变量做比较，可以用int(age)来转换age的变量类型

height = input("How tall are you? ")
height = int(height)
if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're little older!")

###########  7.1.3  求模运算符
# %用这个符号，它将两个数相除并返回余数
#判断某数字是奇数还是偶数
number = input("Enter a number,and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print("\nThe number", str(number), "is even.")
else:
    print("\nThe number", str(number), "is odd.")

#========================  7.2  While循环  ======================#
##########  7.2.1 while循环简介
#for循环针对集合中每个元素的一个代码块，而while循环不断循环直到满足输出条件
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

##########  7.2.2 让用户选择何时退出
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program."
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':  #可以让message = 'quit'时不输出
        print(message)

##########  7.2.3 使用标志
#用一个“标志”来控制整个while循环的进行
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program."
active = True  #声明变量 active 为一个布尔型变量
while active:  #当为“真”时
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

##########  7.2.4 使用break退出循环
#运行到break时立马跳出循环
prompt = "\nPlease enter the name of city you have visited: "
prompt += "\n(Enter 'quit' when you are finished.)"
while True:
    city = input(prompt)
    if city == 'quit':  #当检测到输入为'quit'时，跳出循环
        break
    else:
        print("I'd love to go to", city.title()+"!")

###########  7.2.5 在循环中使用continue
#打印奇数
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:  #这里判断current_number是否为奇数
        continue  #为偶数时，执行continue，忽略后续代码，跳回循环开头
    print(current_number)

###########  7.2.6 避免无限循环

#==================  7.3 使用while循环来处理列表和字典  ===================#
###########  7.3.1 在列表之间移动元素
unconfirmed_users = ['alice', 'garibaldy', 'shirley']
confirmed_users = []
#验证每个用户，直到没有未验证的用户为止，并将已验证过的用户移到新列表中
while unconfirmed_users:
    current_user = unconfirmed_users.pop()  #无参数下弹末尾值
    print("Verifying user:", current_user.title())
    confirmed_users.append(current_user)
#显示所有已验证过的用户
print("\nThe following users have been confirmed:")
for user in confirmed_users:
    print(user.title())

##########  7.3.2 删除包含特定值的所有列表元
pets = ['cat', 'dog', 'dog', 'cat', 'goldfish', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:  #while循环命令，当while后面的条件为“真”时，就执行循环，否则不执行！
    pets.remove('cat')
print(pets)

##########  7.3.3 使用用户输入来填充字典
responses = {}  #生成空字典
polling_active = True
while polling_active:
    #提示输入被调查者的名字和回答
    name = input("\nWhat is your name? ")
    response = input("\nWhich mountain would you like to climb someday? ")
    #将答案存储在字典中
    responses[name] = response
    #查看是否还有人要参与调查？
    repeat = input("\nWould you like to let another person responed? (y/n)")
    if repeat == 'n':
        polling_active = False
#调查结束，显示结果
print("\n------Poll Result------")
for name, response in responses.items():
    print(name.title(), "would like to climb", response + '.')
