"""
面向对象学员管理系统
系统要求：学员数据存储在文件中
系统功能：添加学员、删除学员、修改学员信息、查询学员信息、显示所有学员信息、保存学员信息及退出系统等
"""


# 1. 导入ManagerSystem模块
from ManagerSystem import *


# 2. 启动学员管理系统
# 保证是当前文件运行才启动系统
if __name__ == '__main__':
    student_manager = StudentManager()
    student_manager.run()
