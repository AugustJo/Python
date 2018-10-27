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
# 9.5. 对象与参考
# 建一个对象并给它赋一个变量的时候，这个变量仅仅 参考 那个对象，而不是表示这个对象本身！
 #!/usr/bin/python
# Filename: reference.py

# print 'Simple Assignment'
# shoplist = ['apple', 'mango', 'carrot', 'banana']
# mylist = shoplist # mylist is just another name pointing to the same object!

# del shoplist[0]

# print 'shoplist is', shoplist
# print 'mylist is', mylist
# # notice that both shoplist and mylist both print the same list without
# # the 'apple' confirming that they point to the same object

# print 'Copy by making a full slice'
# mylist = shoplist[:] # make a copy by doing a full slice
# del mylist[0] # remove first item

# print 'shoplist is', shoplist
# print 'mylist is', mylist
# # notice that now the two lists are different 


######################################################
# 更多字符串的内容
# 9.7 字符串的方法

#!/usr/bin/python
# Filename: str_methods.py

# name = 'Swaroop' # This is a string object 

# if name.startswith('Swa'):
#     print 'Yes, the string starts with "Swa"'

# if 'a' in name:
#     print 'Yes, it contains the string "a"'

# if name.find('war') != -1:
#     print 'Yes, it contains the string "war"'

# delimiter = '_*_'
# mylist = ['Brazil', 'Russia', 'India', 'China']
# print delimiter.join(mylist)



######################################################
# 第10章 解决问题——编写一个Python脚本
# 解决方案

# 版本一
# 例10.1 备份脚本——版本一

# #!/usr/bin/python
# # Filename: backup_ver1.py

# import os
# import zipfile
# import time

# # 1. The files and directories to be backed up are specified in a list.
# source = ['D:/github_python/Python/text1.txt', 'D:/github_python/Python/text2.txt']
# # If you are using Windows, use source = [r'C:\Documents', r'D:\Work'] or something like that

# # 2. The backup must be stored in a main backup directory
# target_dir = 'D:/github_python/Python/'

# # 3. The files are backed up into a zip file.
# # 4. The name of the zip archive is the current date and time
# today = target_dir + time.strftime('%Y%m%d')
# # The current time is the name of the zip archive
# now = time.strftime('%H%M%S')

# # Take a comment from the user to create the name of the zip file
# comment = raw_input('Enter a comment --> ')
# if len(comment) <= 1: # check if a comment was entered
#     target = today + os.sep + now + '.zip'
# else:
#     target = today + os.sep + now + '_' + comment.replace('\r', '') + '.zip'
#     # Notice the backslash!

# # Create the subdirectory if it isn't already there
# if not os.path.exists(today):
#     os.mkdir(today) # make directory
#     print 'Successfully created directory', today

# # 5. We use the zip command (in Unix/Linux) to put the files in a zip archive
# #zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))

# f = zipfile.ZipFile(target, 'w', zipfile.ZIP_DEFLATED)
# for file in source:
#     f.write(os.path.join(file))
# f.close


##################################################
# 第14章 Python标准库
# sys模块（还有sys.stdin  sys.stdout sys.stderr等有用的模块）
# 例14.1 使用sys.argv

#!/usr/bin/python
# Filename: cat.py

# import sys

# def readfile(filename):
#     '''Print a file to the standard output.'''
#     f = file(filename)
#     while True:
#         line = f.readline()
#         if len(line) == 0:
#             break
#         print line, # notice comma
#     f.close()

# # Script starts from here
# if len(sys.argv) < 2:
#     print 'No action specified.'
#     sys.exit()

# if sys.argv[1].startswith('--'):
#     option = sys.argv[1][2:]
#     # fetch sys.argv[1] but without the first two characters
#     if option == 'version':
#         print 'Version 1.2'
#     elif option == 'help':
#         print '''\
# This program prints files to the standard output.
# Any number of files can be specified.
# Options include:
#   --version : Prints the version number
#   --help    : Display this help'''
#     else:
#         print 'Unknown option.'
#     sys.exit()
# else:
#     for filename in sys.argv[1:]:
#         readfile(filename)

###################################################


# os模块
# 这个模块包含普遍的操作系统功能。如果你希望你的程序能够与平台无关的话，这个模块是尤为重要的。即它允许一个程序在编写后不需要任何改动，
# 也不会发生任何问题，就可以在Linux和Windows下运行。一个例子就是使用os.sep可以取代操作系统特定的路径分割符。

# 下面列出了一些在os模块中比较有用的部分。它们中的大多数都简单明了。

# os.name字符串指示你正在使用的平台。比如对于Windows，它是'nt'，而对于Linux/Unix用户，它是'posix'。

# os.getcwd()函数得到当前工作目录，即当前Python脚本工作的目录路径。

# os.getenv()和os.putenv()函数分别用来读取和设置环境变量。

# os.listdir()返回指定目录下的所有文件和目录名。

# os.remove()函数用来删除一个文件。

# os.system()函数用来运行shell命令。

# os.linesep字符串给出当前平台使用的行终止符。例如，Windows使用'\r\n'，Linux使用'\n'而Mac使用'\r'。

# os.path.split()函数返回一个路径的目录名和文件名。

# >>> os.path.split('/home/swaroop/byte/code/poem.txt')
# ('/home/swaroop/byte/code', 'poem.txt')

# os.path.isfile()和os.path.isdir()函数分别检验给出的路径是一个文件还是目录。类似地，os.path.existe()函数用来检验给出的路径是否真地存在。

# 你可以利用Python标准文档去探索更多有关这些函数和变量的详细知识。你也可以使用help(sys)等等。

##########################################################
# 第十五章  更多Python形式
# lambda形式
# 例15.2 使用lambda形式

#!/usr/bin/python
# Filename: lambda.py

def make_repeater(n):
    return lambda s: s*n

twice = make_repeater(2)

print twice('word')
print twice(5)