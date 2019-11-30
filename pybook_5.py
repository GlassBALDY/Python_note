####第五章

#================  5.1  if语句简单示例  ================#
#检查车的品牌，对bwm全大写输出
cars = ['audi', 'bwm', 'subaru', 'toyota']
for car in cars:
    if car == 'bwm':
        print(car.upper())
    else:
        print(car.title())

#===============  5.2  条件测试  ==================#
print('\n')
###########  5.2.1  检查是否相等
car = 'bwm'
print(car == 'bwm')

car = 'audi'
print(car == 'bwm')

###########  5.2.2  检查是否相等时不考虑大小写
print('\n')
#统一大小写后再检查
car = 'Audi'
print(car == 'audi')
print(car.lower() == 'audi')

##########  5.2.3  检查是否不相等
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

##########  5.2.4  比较数字
age = 18
print(age == 18)

answer = 17
if answer != 47:
    print("That is not the correct answer. Try again.")

###########  5.2.5  检查多个条件
# and or
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)
print(age_0 >= 21 or age_1 >= 21)

###########  5.2.6  检查特定值是否包含在列表中
# 关键字 in
requested_topping = ['mushrooms', 'oinons', 'pineapple']
print('mushrooms' in requested_topping)

###########  5.2.7  检查特定值是否不包含在列表中
#关键字 结合if  not in
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")

###########  5.2.8  布尔表达式
# True False

print("\n")
#==================  5.3  if语句  ====================#
############  5.3.1  简单的if语句
age = 19
if age >= 18:  #符合判断条件，则会执行缩进格以下的代码
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

###########  5.3.2  if-else语句
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

############  5.3.3  if-elif-else语句
#测试通过后，py执行紧跟在其后的代码，并跳过余下的测试
age = 12
if age < 4:
    print("Your admission cost is 0$")
elif age < 18:
    print("Your admission cost is 5$")
else:
    print("Your admission cost is 10$")

#换个写法
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10
print("Your admission cost is",price,"$.")

###########  5.3.4  多个elif模块
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 0
print("Your admission cost is",price,"$.")

############  5.3.5  省略else
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:  #这样条件更明朗
    price = 0
print("Your admission cost is",price,"$.")

##############  5.3.6  测试多个条件
requested_topping = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_topping:
    print("Adding mushrooms.")
if 'pepperoni' in requested_topping:
    print("Adding pepperoni.")
if 'extra cheese' in requested_topping:
    print("Adding extra cheese.")

#=============  Exercise  ==============#

alien_condition = ['red', 'green', 'yellow']
alien_color = 'green'
if alien_color == 'green':
    print("player earn 5 points.")
alien_color = alien_condition[0]
if alien_color == 'green':
    print("player earn 5 points.")

alien_color = alien_condition[1]
if alien_color == 'green':
    print("player earns 5 points from killing a alien.")
else:
    print("player earns 10 points.")

alien_color = alien_condition[0]
if alien_color == 'green':
    print("player earns 5 points from killing a alien.")
if alien_color != 'green':
    print("player earns 10 points.")

