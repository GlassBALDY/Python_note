# 3.3
# 组织列表
#sort()对列表永久性排序
car = ['bwm', 'audi', 'toyota', 'suzuki']
print(car)
car.sort()   #以字母顺序排列
print(car)

#参数reverse = T控制逆序排列
car = ['bwm', 'audi', 'toyota', 'suzuki']
print(car)
car.sort(reverse=True)
print(car)

#sorted()对列表临时排序
car = ['bwm', 'audi', 'toyota', 'suzuki']
print("This is the original list:")
print(car)
print("This is the sorted list:")
print(sorted(car, reverse=True))   #sorted()临时排序，此函数亦可
print(car)

#反转打印列表
car = ['bwm', 'audi', 'toyota', 'suzuki']
print(car)
car.reverse()   #反转列表
print(car)

#确定列表长度
car = ['bwm', 'audi', 'toyota', 'suzuki']
len(car)   #会返回4

#======================我是分割线=====================#
place = ['Israle', 'America', 'Russia', 'British']
print(place)
print(sorted(place))
print(place)
print(sorted(place, reverse=True))
print(place)

#以下是错误案例，这样并不能输出！
#print(place.reverse())   #反转打印
#print(place.reverse())   #再反转回来打印
#print(place.sort())
#print(place.sort(reverse=True))

#真正的反转打印
place.reverse()
print(place)
place.reverse()
print(place)

#排序打印
place.sort()
print(place)
place.sort(reverse=True)
print(place)








