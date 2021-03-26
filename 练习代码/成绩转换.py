# coding: utf-8 

"""
!project: code
!file: 成绩转换.py
!time: 2021-03-22 下午 08:55
!product_name: PyCharm
"""

a = float(input('输入成绩：'))
if 100 >= a >= 90:
    print('A')
elif 90 > a >= 80:
    print('B')
elif 80 > a >= 70:
    print('C')
elif 70 > a >= 60:
    print('D')
elif 60 > a >=0:
    print('E')
else:
    print('百分制转换')