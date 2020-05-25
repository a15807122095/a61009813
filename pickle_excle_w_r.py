


# import pickle
# message = ['123',3.14,['文件']]
# #写入
# pickle_file = open('./my_list.pkl','wb')#以二进制的模式写入
# pickle.dump(message,pickle_file)  #将my_list以二进制的方式存储在文件中
# pickle_file.close()
#
# #读取
# pickle_file1 = open('./my_list.pkl','rb')#以二进制的模式读取
# my_list1 = pickle.load(pickle_file1)
# pickle_file1.close()
# print(my_list1, type(my_list1))


# **********************************************************************************************************************
import os
import xlwt
import xlrd
import openpyxl

# # 2、创建workbook（其实就是excel，后来保存一下就行）
# workbook = xlwt.Workbook(encoding = 'ascii')
#
# # 3、创建表
# worksheet = workbook.add_sheet('My Worksheet')
#
# # 4、往单元格内写入内容
# worksheet.write(0, 0, label = 'Row 0, Column 0 Value')
#
# # 5、保存
# workbook.save('./Desktop/Excel_Workbook.xls')

print("获取当前文件路径——" + os.path.realpath(__file__))

parent = os.path.dirname(os.path.realpath(__file__))
print("获取其父目录——" + parent)  # 从当前文件路径中获取目录
print("获取文件名" + os.path.basename(os.path.realpath(__file__)))  # 获取文件名
# 当前文件的路径
pwd = os.getcwd()
print("当前运行文件路径" + pwd)
# 当前文件的父路径
father_path = os.path.abspath(os.path.dirname(pwd) + os.path.sep + ".")
print("运行文件父路径" + father_path)
# 当前文件的前两级目录
grader_father = os.path.abspath(os.path.dirname(pwd) + os.path.sep + "..")
print("运行文件父路径的父路径" + grader_father)


'''
环境变量就是一些命令的集合
操作系统的环境变量就是操作系统在执行系统命令时搜索命令的目录的集合
'''
#getenv() 获取系统的环境变量
result = os.getenv('PATH')
print(result)



