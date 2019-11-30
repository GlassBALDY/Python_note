####第四章
#===============  4.1  遍历整个列表  ================#
#for循环遍历
magicians = ['Garibaldy', 'Shirley', 'Leon']
for magician in magicians:   #py的for循环如同matlab，也可以这样方便的定义变量，并且更加方便，直接遍历！
                             #magician是一个临时变量
    print(magician)

############  4.1.2  for循环中更多操作
magicians = ['Garibaldy', 'Shirley', 'Leon']
#缩进中全是循环体
for magician in magicians:
    print(magician.title() + ", that was a great trick.")
    print("I can't wait to see your next trick, " + magician.title() + ".")

#############  4.1.3  在for循环结束后执行一些操作
magicians = ['Garibaldy', 'Shirley', 'Leon']
for magician in magicians:
    print(magician.title() + ", that was a great trick.")
    print("I can't wait to see your next trick, " + magician.title() + ".")

#循环外的命令
print("Thank you, everyone. That was a great magic show!")

#==============  4.2  避免缩进错误  =================#
#py对缩进很敏感，缩进代表从属于前一行代码，所以要避免不必要的缩进。
#for循环莫要忘了冒号：

#==============  4.3  创建数值列表  =================#

##############  4.3.1  range()函数
for value in range(1, 5):
    print(value)
#range(1, 5)只会输出1~4，并不会输出5，这是range()函数的一个注意点

n = range(1, 5)
type(n)
#很有趣，type显示n是个‘range’类变量

#############  4.3.2  使用range()创建数字列表
numbers = list(range(1, 6))
print(numbers)   #打印出列表

#指定数列步长
even_numbers = list(range(2, 11, 2))
print(even_numbers)

#通过函数创造自己的数列
squares = []
for i in range(1, 11):
    square = i ** 2
    squares.append(square)
print(squares)   #打印squares列表

#（亦可不使用临时变量）
squares = []
for i in range(1, 11):
    squares.append(i** 2)
print(squares)   #打印squares列表

###############  4.3.3  对数字列表的简单统计计算
digits = list(range(1, 11))
print(min(digits))   #print可以打印任何变量，但是+号作为一个连字符，不能连不相同的变量
print(max(digits))
print(sum(digits))

###############  4.3.4  列表解析
# formula + for i in list
squares = [value ** 2 for value in range(1, 11)]
print(squares)

##
numbers = []
for i in range(1, 21):
    print(i)

numbers = [i for i in range(1, 1000001)]
print(numbers)
print(sum(numbers))

numbers = [i for i in range(1, 21, 2)]
print(numbers)

numbers = [i * 3 for i in range(1, 11)]
print(numbers)

numbers = [i ** 3 for i in range(1, 11)]
for i in numbers:
    print(i)

#==================  4.4  使用列表的一部分  ==================#

##############  4.4.1  切片
players = ['charles', 'martina', 'michael', 'eli', 'florence']
#提取1~3个元素
print(players[ 0: 3])   #这只会输出索引0，1，2

#提取2~4个元素
print(players[ 1: 4])

#不指定第一个索引，py自动从第一个元素开始
print(players[ : 4])

#同理有自动切片到结尾
print(players[ 2: ])

#输出倒数三名球员
print(players[ -3: ])

#################  4.4.2  遍历切片
players = ['charles', 'martina', 'michael', 'eli', 'florence']
print("Here are the first three players in my team:")
for i in players[:3]:
    print(i.title())

##############  4.4.3  复制列表
#([:])引用所有元素
my_foods = ['noodles', 'dunplims', 'carrot cake']
friend_foods = my_foods[:]
print("My favorate foods are: ")
print(my_foods)
print("\nMy friend's favorate foods are:")
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorate foods are: ")
print(my_foods)
print("\nMy friend's favorate foods are:")
print(friend_foods)

print('\n')
#注意！！这样不对：
my_foods = ['noodles', 'dunplims', 'carrot cake']
friend_foods = my_foods  #py中，该语句会让两个变量指向同一个列表
#所以，如果执行添加的操作，会有：
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorate foods are: ")
print(my_foods)
print("\nMy friend's favorate foods are:")
print(friend_foods)
#结果是都加上了

