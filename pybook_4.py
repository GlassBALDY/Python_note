#================  4.5  元组  ==================#

#不可变的列表称为元组

#############  4.5.1  定义元组
#使用圆括号（）来标识元组
dimensions = (200, 50)
# use [] to cite the element
print(dimensions[0])
print(dimensions[1])

# unable to change the element in tuple
#dimensions[0] = 250
# TypeError: 'tuple' object does not support item assignment

print('\n')

##############  4.5.2  遍历元组
dimensions = (200 ,50)
for i in dimensions:
    print(i)

##############  4.5.3  修改元素变量
dimensions = (200 ,50)
print("Original dimensions:")
for i in dimensions:
    print(i)

dimensions = (400, 100)
print("\nModified dimensions:")
for i in dimensions:
    print(i)

#================  4.6  设置代码格式  =================#
#PEP 8 的编码格式