# -*- coding:utf-8 -*-  
#############################################################
# !/usr/bin/python
# Filename: while.py

# number = 23
# running = True

# while running:
#     guess = int(raw_input('Enter an integer : '))

#     if guess == number:
#         print 'Congratulations, you guessed it.' 
#         running = False # this causes the while loop to stop
#     elif guess < number:
#         print 'No, it is a little higher than that' 
#     else:
#         print 'No, it is a little lower than that' 
# else:
#     print 'The while loop is over.' 
#     # Do anything else you want to do here

# print 'Done'
##########################################################
# !/usr/bin/python
# Filename: for.py

# for i in range(1, 5):
#     print i
# else:
#     print 'The for loop is over'
##########################################################
# !/usr/bin/python
# Filename: break.py

# while True:
#     s = raw_input('Enter something : ')
#     if s == 'quit':
#         break
#     print 'Length of the string is', len(s)
# print 'Done'
##########################################################
 #!/usr/bin/python
# Filename: func_doc.py

# def printMax(x, y):
#     '''Prints the maximum of two numbers.

#     The two values must be integers.'''
#     x = int(x) # convert to integers, if possible
#     y = int(y)

#     if x > y:
#         print x, 'is maximum'
#     else:
#         print y, 'is maximum'

# printMax(3, 5)
# print printMax.__doc__ 
##########################################################
 #!/usr/bin/python
# Filename: using_sys.py

# import sys

# print 'The command line arguments are:'
# for i in sys.argv:
#     print i

# print '\n\nThe PYTHONPATH is', sys.path, '\n' 


# from sys import argv
# from sys import path

# print 'The command line arguments are:'
# for i in argv:
#     print i

# print '\n\nThe PYTHONPATH is', path, '\n' 
########################################################
 #!/usr/bin/python
# Filename: using_name.py

# if __name__ == '__main__':
#     print 'This program is being run by itself'
# else:
#     print 'I am being imported from another module' 
########################################################
# 简明python教程 
# 第9章 数据结构
# 9.1. 列表 方括号 可修改
#!/usr/bin/python
# Filename: using_list.py

# # This is my shopping list
# shoplist = ['apple', 'mango', 'carrot', 'banana']

# print 'I have', len(shoplist),'items to purchase.'

# print 'These items are:', # Notice the comma at end of the line
# for item in shoplist:
#     print item,

# print '\nI also have to buy rice.'
# shoplist.append('rice')
# print 'My shopping list is now', shoplist

# print 'I will sort my list now'
# shoplist.sort()
# print 'Sorted shopping list is', shoplist

# print 'The first item I will buy is', shoplist[0]
# olditem = shoplist[0]
# del shoplist[0]
# print 'I bought the', olditem
# print 'My shopping list is now', shoplist

########################################################
# 9.2. 元组 圆括号 不可修改
 #!/usr/bin/python
# Filename: using_tuple.py

# zoo = ('wolf', 'elephant', 'penguin')
# print 'Number of animals in the zoo is', len(zoo)

# new_zoo = ('monkey', 'dolphin', zoo)
# print 'Number of animals in the new zoo is', len(new_zoo)
# print 'All animals in new zoo are', new_zoo
# print 'Animals brought from old zoo are', new_zoo[2]
# print 'Last animal brought from old zoo is', new_zoo[2][2] 

# 元组与打印语句
# 元组最通常的用法是用在打印语句中，下面是一个例子
 #!/usr/bin/python
# Filename: print_tuple.py

# age = 22
# name = 'Swaroop'

# print '%s is %d years old' % (name, age)
# print 'Why is %s playing with that python?' % name 

########################################################
# 9.3. 字典 大括号
# 把键（名字）和值（详细情况）联系在一起。
# 注意，你只能使用不可变的对象（比如字符串）来作为字典的键，但是你可以不可变或可变的对象作为字典的值。
 #!/usr/bin/python
# Filename: using_dict.py

# 'ab' is short for 'a'ddress'b'ook

# ab = {       'Swaroop'   : 'swaroopch@byteofpython.info',
#              'Larry'     : 'larry@wall.org',
#              'Matsumoto' : 'matz@ruby-lang.org',
#              'Spammer'   : 'spammer@hotmail.com'
#      }

# print "Swaroop's address is %s" % ab['Swaroop']

# # Adding a key/value pair
# ab['Guido'] = 'guido@python.org'

# # Deleting a key/value pair
# del ab['Spammer']

# print '\nThere are %d contacts in the address-book\n' % len(ab)
# for name, address in ab.items():
#     print 'Contact %s at %s' % (name, address)

# if 'Guido' in ab: # OR ab.has_key('Guido')
#     print "\nGuido's address is %s" % ab['Guido'] 


########################################################
# 9.4. 序列
# 序列的两个主要特点是索引操作符和切片操作符。
 #!/usr/bin/python
# Filename: seq.py

# shoplist = ['apple', 'mango', 'carrot', 'banana']

# # Indexing or 'Subscription' operation
# print 'Item 0 is', shoplist[0]
# print 'Item 1 is', shoplist[1]
# print 'Item 2 is', shoplist[2]
# print 'Item 3 is', shoplist[3]
# print 'Item -1 is', shoplist[-1]
# print 'Item -2 is', shoplist[-2]

# # Slicing on a list
# print 'Item 1 to 3 is', shoplist[1:3]
# print 'Item 2 to end is', shoplist[2:]
# print 'Item 1 to -1 is', shoplist[1:-1]
# print 'Item start to end is', shoplist[:]

# # Slicing on a string
# name = 'swaroop'
# print 'characters 1 to 3 is', name[1:3]
# print 'characters 2 to end is', name[2:]
# print 'characters 1 to -1 is', name[1:-1]
# print 'characters start to end is', name[:] 

#####################################################
# 9.5. 参考
# 建一个对象并给它赋一个变量的时候，这个变量仅仅 参考 那个对象，而不是表示这个对象本身！
 #!/usr/bin/python
# Filename: reference.py

print 'Simple Assignment'
shoplist = ['apple', 'mango', 'carrot', 'banana']
mylist = shoplist # mylist is just another name pointing to the same object!

del shoplist[0]

print 'shoplist is', shoplist
print 'mylist is', mylist
# notice that both shoplist and mylist both print the same list without
# the 'apple' confirming that they point to the same object

print 'Copy by making a full slice'
mylist = shoplist[:] # make a copy by doing a full slice
del mylist[0] # remove first item

print 'shoplist is', shoplist
print 'mylist is', mylist
# notice that now the two lists are different 
