####第六章

#================  6.1 一个简单的字典  ================#
#以下是一个储存了外星人属性的字典
alien_0 = {'color': 'green', 'points': 5}  #注意字典的创建与数组的创建符号不同，
print(alien_0['color'])  #引用方式也不同
print(alien_0['points'])

print('\n')

#python中，字典是一系列 键-值对，每个键都与一个值相关联。
#这个值可以是数字，字符，列表，或者新的字典或任何对象。

#================  6.2 使用字典  ==============#

############  6.2.1 访问字典中的值
new_points = alien_0['points']
print('You just earned', str(new_points), 'points')

print('\n')


############  6.2.2 添加键值对
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0  #添加键值对时，依次指定字典名、用方括号括起的键和相关联的值。
alien_0['y_position'] = 25
print(alien_0)

print('\n')


############  6.2.3 创建空字典
alien_1 = {}  #创建空字典
alien_1['color'] = 'green'
alien_1['points'] = 5
print(alien_1)

print('\n')


############  6.2.4 修改字典中的值
print("The alien is", alien_1['color'], '.')
alien_1['color'] = 'yellow'  #修改字典中的值
print("The alien is now", alien_1['color'], '.')

#外星人的移动
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position:", str(alien_0['x_position']))
#向右移动外星人
#依据外星人的速度决定将其移动多远

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position:", str(alien_0['x_position']))

print('\n')



###########  6.2.5 删除键-值对
#使用del函数将相应的键-值对彻底删除
alien_0 = {'color':0, 'points':5}
print(alien_0)
del alien_0['points']  #删除时，指定字典名和要删除的键
print(alien_0)

print('\n')


###########  6.2.6 由类似对象组成的字典
favorate_languages = {
    'Garibaldy': 'Python',
    'Shirley': 'C++',
    'Jernan': 'Matlab'
    }  #注意对齐规则
print(favorate_languages)
print("Shirley's favorite language is",
      favorate_languages['Shirley'].title(),
      '.')  #注意对齐规则，相同地位的元素退格要一致
print('\n')


#==================  6.3 遍历字典  ===================#
#python支持对字典的遍历，可遍历键-值对，键或值

###########  6.3.1  遍历所有的键-值对
user_0 = {
    'username': 'garibaldy',
    'first': 'leon',
    'last': 'garibaldy',
    }
#随意声明两个变量，用于存储键-值对中的键与值
for k, v in user_0.items():
    print('\nKey:', k)
    print('Value:', v)
#注意，遍历字典时，py并不关心键-值对的存储顺序，py只跟踪键和值之间的关联关系

#遍历favorate_language字典
for name, language in favorate_languages.items():
    print(name.title() + "'s favorite language is", language.title() + '.')
print('\n')


###########  6.3.2  遍历字典中的所有键
favorate_languages['edward'] = 'ruby'
favorate_languages['phil'] = 'python'  #向favorite_language字典中添加两个元素
print(favorate_languages)
for name in favorate_languages.keys():  #.keys()提取favorite_language中的所有键，并依次存储到name中
    print(name.title())
print('\n')

#遍历字典时，默认遍历所有的键
for name in favorate_languages:  #不加后缀函数时，默认遍历所有键
    print(name.title())
friends = ['Phil', 'Garibaldy']
for name in favorate_languages.keys():
    print(name.title())
    if name.title() in friends:  #判别name是否在列表friends中
        print("Hi", name.title() + ', I see your favorite language is', favorate_languages[name].title() + "!")

if 'erin'.title() not in favorate_languages.keys():
    print("Erin, please take our poll!")
print('\n')

###########  6.3.3 按顺序遍历字典中的所有键
#若是要以特定顺序返回元素，一种办法是在for循环中对返回的键进行排序。
#可以使用sorted()函数来获得特定顺序排列的键列表的副本
favorate_languages = {
    'jen': 'python',
    'garibaldy': 'c',
    'rorschach': 'R',
    'edward': 'Matlab',
    'shirley': 'c++',
    }
for name in sorted(favorate_languages.keys()):  #sorted函数会在遍历前对这个列表排序
    print(name.title() + ', thank you for taking the poll.')
#这样输出时会按顺序输出键名称
print('\n')

############  6.3.4  遍历字典中所有的值

favorate_languages = {
    'jen': 'python',
    'garibaldy': 'c',
    'rorschach': 'R',
    'edward': 'Matlab',
    'shirley': 'c++',
    }
print("The following languages has been mentioned:")

for language in favorate_languages.values():
    print(language.title())
#注意，这种做法可以提取所有的值，但是不会考虑值是否重复了。
#当字典很大时，可能会出现大量重复项。为剔除重复项，可使用set函数
print('\n')

for language in set(favorate_languages.values()):
    print(language.title())

print('\n')

#=================  6.4  嵌套  ==================#
 #将一系列字典储存在列表中，或将列表作为值储存在字典中，这称为嵌套。
 #万物可嵌套

 ##########  6.4.1 字典列表
 #成群结队的外星人，每个外星人都是一个字典
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]  #构造以各字典为元素的列表
for alien in aliens:
    print(alien)

print('\n')

#自动生成一批外星人列表

aliens= []  #创建一个空列表
for alien_number  in range(30):  #批量生成30个外星人
    new_alien = {'color': 'green', 'points' : 5, 'speed' : 'slow'}
    aliens.append(new_alien)

#显示前5个外星人
for alien in aliens[:5]:  #切片0，1，2，3，4
    print(alien)
print("...")

#显示创建了多少外星人
print("Total number of aliens:", str(len(aliens)))

print('\n')

#修改前三个外星人的值
for alien in aliens[:3]:  #切片0，1，2
    if alien['color'] == 'green':
        alien['color'] = 'yellow'  #修改颜色
        alien['speed'] = 'medium'  #修改速度
        alien['points'] = 10  #修改分数

#显示前5个外星人
for alien in aliens[:5]:  #切片0，1，2，3，4
    print(alien)

print("...")

print('\n')


#########  6.4.2  在字典中存储列表
pizza = {'crust': 'thick', 'toppings': ['mushrooms', 'extra cheese'],}
#概述所点的比萨
print("You ordered a", pizza['crust'] + "-crust pizza", "with the following toppings:")
for topping in pizza['toppings']:
    print('\t' + topping)

print('\n')

#双变量循环
favorate_languages = {
    'garibaldy': ['matlab', 'R'],
    'shirley': ['c', 'python'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }
for name, languages in favorate_languages.items():
    print('\n' + name.title() + "'s favorite languages are:")
    for language in languages:
        print('\t' + language.title())

##########  6.3.4  在字典中嵌套字典
#网站将用户名储存在一个字典中，每个用户的属性值又储存在一个字典中
user = {
    'aeinstein': {'first': 'albert', 'last': 'einstein', 'location': 'prinston'},
    'mcurie': {'first': 'marie', 'last': 'curie', 'location': 'paris'},
    }

for user_name, user_info in user.items():
    print("\nUsername:", user_name)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\nFull name:", full_name.title())
    print("\tLocation:", location.title())

print('\n')











