# 英制单位英寸和公制单位厘米互换 1英寸 = 2.54cm
shuzhi = float(input('input'))
danwei = input('输入单位(in and cm)')

if danwei == 'in' or danwei == '英寸':
    print('英寸%f = 厘米%f' % (shuzhi, shuzhi*2.54))
elif danwei == 'cm' or danwei == '厘米':
    print('厘米%f = 英寸%f' % (shuzhi, shuzhi/ 2.45))