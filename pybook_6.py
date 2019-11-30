####第五章

#================  5.4  使用if语句处理列表  ================#
############  5.4.1  检查特殊元素
requested_toppings = ['mushroom', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    print("Adding", requested_topping +".")
print("Finished making your pizza！\n")

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green pepper right now.")
    else:
        print("Adding",requested_topping + ".")
print("Finished making your pizza!\n")

############  5.4.2  确定列表不是空的
requested_toppings = []
if requested_toppings:   #在if语句中，将list写在表达式处，py将在list中至少含有一个元素时输出True
    for requested_topping in requested_toppings:
        print("Adding", requested_topping + ".")
else:
    print("Are you sure you want a plain pizza?")

print("\n")
############  5.4.3  使用多个列表
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepper oni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
       print("Adding", requested_topping +".")
    else:
       print("Sorry, we don't have",requested_topping + ".")
print("Finished making your pizza!")

#=================  Exercise  ==================#
users = ['admin', 'garibaldy', 'shirley', 'Leon']   #有大写有小写
if users:   #检查列表是否为空
    for user in users:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello",user + " , thank you for loggin.")
else:
    print("We need to find some users!")

current_users = ['hana', 'Garibaldy', 'Shirley', 'leon', 'cliff']
new_users = ['Hana', 'shirley', 'Bismark', 'Albert', 'Rudoff']
for new_user in new_users:
    if new_user.lower() in [current_user.lower() for current_user in current_users]:
        print(new_user + ", you need to change a name.")
    else:
        print(new_user + ", you can use this name.")

number = range(1, 10)
#print(number)   #居然打印结果是range(1, 10) ...
for i in number:
    if i == 1:
        print(str(i) + "st")
    elif i == 2:
        print(str(i) + "nd")
    elif i == 3:
        print(str(i) + "rd")
    elif i >= 4:
        print(str(i) + "th")