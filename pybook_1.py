####第三章
# 3.1~3.2
# .操作，很有趣，指对这个变量执行后面的操作
name = "Garibaldy's python journey"
print(name.title())
print(name.upper())
print(name.lower())

#空白字符
print("Languages:\nPython\nMatlab\nR")
print("Languages:\n\tPython\n\tMatlab\n\tR")

#删除字符串的空白.rstrip() .lstrip() .strip()
favorate_language = 'python is good'
favorate_language.rstrip()

#第三章
#列表操作
#创建+引用
bicycle = ['trek', 'cannondale', 'redline', 'specialized']
message = "My first bicycle was a " + bicycle[0].title()
print(message)

#修改
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

#添加在末尾.append()
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)

#向空数组添加
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

#插入元素.insert()
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')   #将元素插入到0索引处
print(motorcycles)

#删除元素

#del  已知元素索引时可用
print(motorcycles)
del motorcycles[0]   #删除0索引元素
print(motorcycles)

#pop() 删除列表末尾的元素  弹出式删除
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()   #无参数下弹末尾
print(motorcycles)   #返回列表
print(popped_motorcycle)   #返回弹出值

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
first_owned = motorcycles.pop(0)   #有参数下弹索引
print(motorcycles)   #返回列表
print(first_owned)   #返回弹出值

#remove() 根据值删元素
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')   #寻找该元素并删除
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)   #remove()中参数不能用列表
print(motorcycles)
print("\nA "+too_expensive.title()+" is too expensive for me.")
#remove()只删除指定的第一个出现值

#===================分割线===================#
guest = ['Garibaldy', 'Shirley', 'Leon', 'Khabu']
print(guest)
break_appointment = 'Shirley'
print('\n' + break_appointment.title() +" couldn't take part in." )
new_invite = 'Gauss'
print('\n' + new_invite.title() + "is our new guest. ")
guest.remove(break_appointment)
guest.append(new_invite)
print(guest)
print('We found a bigger table.')

new_invite = 'Isabella'
guest.insert(0, new_invite)
guest.insert(2, 'Morpheus')
guest.append('Tom')
print(guest)

print('Unfortunatelly the table\'s deliver is delay, wu could only invite two guest')
guest.pop()
guest.pop()
guest.pop()
guest.pop()
guest.pop()
print(guest)
print(guest[0].title() + " is still in our invitation.")
print(guest[-1].title() + " is still in our invitation. ")
del guest[0]   #del()的参数不能是列表
del guest[-1]
print(guest)
n = len(guest)

#注意，print只能打印字符型变量，所以打印n之前，要先转换变量类型。
print("I invite " + str(n) + " guests to join the dinner." )