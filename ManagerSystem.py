# 管理员角色
"""
需求：
    1. 存储数据的文件：文件(student.data)
        1.1 加载文件数据
        1.2 修改数据后保存到文件
    2. 存储数据的形式：列表存储学员对象
    3. 系统功能：添加学员、删除学员、修改学员信息、查询学员信息、显示所有学员信息、保存学员信息及退出系统等
"""


from student import *


# 1. 定义类
class StudentManager(object):
    def __init__(self):
        # 存储学员数据 -- 列表
        self.student_list = []

# 2. 管理系统框架
    # 2.1 程序入口函数
    def run(self):
        # 2.1.1 加载数据
        self.load_student()

        while True:
            # 2.1.2 显示功能菜单
            self.show_menu()
            # 2.1.3 用户输入功能序号
            menu_num = int(input('请选择功能：'))

            # 2.1.4 根据用户输入的不同功能序号执行不同的功能
            if menu_num == 1:
                # 添加学员
                self.add_student()
            elif menu_num == 2:
                # 删除学员
                self.del_student()
            elif menu_num == 3:
                # 修改学员信息
                self.modify_student()
            elif menu_num == 4:
                # 查询学员信息
                self.search_student()
            elif menu_num == 5:
                # 显示所有学员信息
                self.show_student()
            elif menu_num == 6:
                # 保存学员信息
                self.save_student()
            elif menu_num == 7:
                # 退出系统 -- 退出循环
                break

    # 2.2 系统功能函数
    # 2.2.1 显示功能菜单 -- 打印序号的功能对应关系 -- 静态
    @staticmethod
    def show_menu():
        print('1:添加学员')
        print('2:删除学员')
        print('3:修改学员信息')
        print('4:查询学员信息')
        print('5:显示所有学员信息')
        print('6:保存学员信息')
        print('7:退出系统')

    # 2.2.2 添加学员
    def add_student(self):
        # 用户输入姓名性别手机号
        name = input('请输入学员姓名:')
        gender = input('请输入学员性别:')
        tel = input('请输入学员手机号:')

        # 创建学员对象 -- 类在student文件里 -- 先导入student模块，再创建对象
        students = Student(name, gender, tel)

        # 将该对象添加到学员列表
        self.student_list.append(students)

        print('添加成功')
        # print(self.student_list)
        # print(students)

    # 2.2.3 删除学员
    def del_student(self):
        # 用户输入要删除的学员姓名
        del_name = input('请输入要删除的学员姓名：')

        # 遍历学员列表，如果学员存在则删除学员对象，否则提示查无此人
        for i in self.student_list:
            if del_name == i.name:
                self.student_list.remove(i)
                print('删除成功')
                break
        else:
            # 循环正常结束执行的代码
            print('查无此人！')

        print(self.student_list)

    # 2.2.4 修改学员信息
    def modify_student(self):
        # 用户输入目标学员姓名
        modify_name = input('请输入要修改的学员姓名：')

        # 遍历学员列表，如果学员存在则修改其信息，否则提示查无此人
        for i in self.student_list:
            if modify_name == i.name:
                i.name = input('姓名：')
                i.gender = input('性别：')
                i.tel = input('手机号：')
                print(f'修改学员信息成功，姓名：{i.name}, 性别：{i.gender}, 手机号：{i.tel}')
                break
        else:
            print('查无此人！')

    # 2.2.5 查询学员信息
    def search_student(self):
        # 用户输入目标学员姓名
        search_name = input('请输入要查询的学员姓名：')

        # 遍历学员列表，如果学员存在则打印学员信息，否则提示查无此人
        for i in self.student_list:
            if search_name == i.name:
                print(f'姓名：{i.name}, 性别：{i.gender}, 手机号：{i.tel}')
                break
        else:
            print('查无此人！')

    # 2.2.6 显示所有学员信息
    def show_student(self):
        # 打印表头
        print('姓名\t性别\t手机号')

        # 遍历学员列表，打印所有学员信息
        for i in self.student_list:
            print(f'{i.name}\t\t{i.gender}\t\t{i.tel}')

    # 2.2.7 保存学员信息
    def save_student(self):
        # 打开文件
        f = open('student.data', 'w')

        # 文件写入学员数据
        # 注意1：文件写入的数据不能是学员对象的内存地址，需要吧学员数据转换成列表字典数据再存储
        new_list = [i.__dict__ for i in self.student_list]  # 列表推导式

        # 注意2：文件内数据要求为字符串类型，故需要先转换数据类型为字符串才能写入数据
        f.write(str(new_list))

        # 关闭文件
        f.close()

        print('保存成功！')

    # 2.2.8 加载学员信息
    def load_student(self):
        # 打开文件，尝试 r 打开，如果有异常 w
        try:
            f = open('student.data', 'r')
        except:
            f = open('student.data', 'w')
        else:
            # 读取数据：文件读取出的数据是字符串还原列表类型：[{}] 转换 [学员对象]
            data = f.read()  # 字符串
            new_list = eval(data)  # 字符串转列表
            self.student_list = [Student(i['name'], i['gender'], i['tel']) for i in new_list]
        finally:
            # 关闭文件
            f.close()
