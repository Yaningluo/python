# 有1234四个数，组成不重复且不相同的三位数
"""
定义列表包含1234
定义空列表接受组合数据
"""
list_1 = [1, 2, 3, 4]
list_2 = []
def zuhe():
    for i in list_1:
        for j in list_1:
            for k in list_1:
                if i != j and i != k and j != k:
                    list_2.append(str(i)+str(j)+str(k))
    print(f"{list_2}\n{len(list_2)}")
zuhe()
