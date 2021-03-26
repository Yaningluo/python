# 学生管理系统
# 选项详情
def info_print():
    print("-"*20)
    print("\t|1|\t|添加信息|")
    print("\t|2|\t|删除信息|")
    print("\t|3|\t|修改信息|")
    print("\t|4|\t|查询信息|")
    print("\t|5|\t|显示信息|")
    print("\t|6|\t|退出系统|")
    print("-"*20)

# 全局变量info用来接收数据
info = []

# 添加信息的函数
def add_info():
    """添加信息"""
    print("-"*20)
    new_id = input('ID识别码:')
    print("-"*20)
    new_key = input('密码')
    global info     #调用全局变量
    for i in info:  # 循环遍历info
        if new_id == i['ID']:
            print("-" * 20)
            print("该用户已存在")
            return
    info_i = {}
    info_i['ID'] = new_id
    info_i['key'] = new_key
    info.append(info_i)
    print(info)

# 删除信息函数
def del_info():
    """删除信息"""
    print("-"*20)
    del_id = input('输入删除的ID:')
    global info
    for i in info:
        if del_id == i['ID']:
           info.remove(i)
           break
    else:
        print("-"*20)
        print("此ID不存在")

# 修改信息函数
def mod_info():
   """修改信息"""

   print("-"*20)
   mod_id = input('修改的ID:')
   global info
   for i in info:
       if mod_id == i['ID']:
           print("-" * 20)
           i['key'] = input('输入新的密码:')
           break
   else:
        print("-" * 20)
        print("此ID不存在")

# 查询函数
def see_info():
    """查询信息"""
    print("-" * 20)
    see_key = input('查看key配对的ID:')
    global info
    for i in info:
        if see_key == i['key']:
            print("------查询信息如下-----")
            print(f"此key:{i['key']}配对的ID是:{i['ID']}")
            break
    else:
        print("-"*20)
        print("此key不存在或者错误")
def print_all():
    global info
    print("\tID\tkey")
    for i in info:
        print(f"\t{i['ID']}\t{i['key']}")


# 代码主体
while True:     # 死循环用来重复代码执行
    info_print()
    user = input("请选择:")
    if user == '1':
        add_info()
    elif user == '2':
        del_info()
    elif user == '3':
        mod_info()
    elif user == '4':
        see_info()
    elif user == '5':
        print_all()
    elif user == '6':
        print("-"*20)
        Y = input('退出输入Y:')
        if Y == 'Y' or 'y':
            break
        else:
            print("-"*20)
            print("输错说明你还不想退出")
    else:
        print("-" * 20)
        print("未知选项")