# -*-coding:utf-8 -*-
# tested with python 2.7.15 & python 3.7.0
'''
1.名称：光圈N与曲率半径偏差Re互相转换程序
2.作者：YONG(光杆司令：wanyong_37@hotmail.com)
3.版本：v0.3
4.更新：20180914
    4.1 按照ISO 10110-5中的定义增加CA与Rn相当的情形
    4.2 “Python3中input得到的为str，Python2的input的到的为int型”，使用str将CH统一转换为str类型
5.参考资料：
    5.1 ISO 10110-5:2007 Optics and photonics -- Preparation of drawings for optical elements and systems -- Part 5: Surface form tolerances
6.其他
    当CA/Rn<0.1时，结果验证：http://calc.escooptics.com/metrology?calc=metrology-tolerances
'''
from __future__ import print_function #for python2

import os
import time

print("#################################################\
        \n# 1.名称：光圈N与曲率半径偏差Re互相转换程序\
        \n# 2.作者：光杆司令(wanyong_37@hotmail.com)\
        \n# 3.版本：v0.3\
        \n# 4.更新：20180914\
        \n# 5.参考资料：\
        \n#    5.1 ISO 10110-5:2007 Optics and photonics\
        \n#        -- Preparation of drawings for optical \
        \n#        elements and systems-- Part 5: Surface\
        \n#        form tolerances\
        \n################################################")

print("\n>>转换模式<<\n1.光圈N转换为曲率半径偏差Re\
                         \n2.曲率半径偏差Re转换为光圈N ")
CH=str(input("\n>>请输入 转换模式(1或2) : ")) 

if CH=="1":
    Rn=float(input(u"标称曲率半径R/mm: "))
    CA=float(input(u"有效孔径CA/mm: "))
    W=float(input(u"测试波长lambda/nm: "))
    N=float(input(u"光圈N: "))
    if CA/Rn<0.1: #此时认为CA/Rn可以忽略不计，即认为CA/Rn==0
        Re=4*N*(W*1.0E-6)*Rn**2/CA**2 #曲率半径偏差
        #Ce=(4*W/1.0E-6*N)/CA**2        #曲率偏差
        #print("The difference of Curvature is: %.3f"%Ce,"mm^{-1}")
    else:
        Re=N*(W*1.0E-6)/(1-(1-(CA/Rn/2)**2)**(1/2))/2  
    print(u"曲率半径偏差Re是: %.4f"%Re,"mm")

else:
    Rn=float(input(u"标称曲率半径R/mm: "))
    CA=float(input(u"有效孔径CA/mm: "))
    W=float(input(u"测试波长lambda/nm: "))
    Re=float(input(u"曲率半径偏差Re/mm: "))
    if CA/Rn<0.1: #此时认为CA/Rn可以忽略不计，即认为CA/Rn==0
        N=CA**2*Re/(4*Rn**2*(W*1.0E-6))
    else:
        N=2*Re*(1-(1-(CA/Rn/2)**2)**(1/2))/(W*1.0E-6) 
    print(u"光圈N: %.2f"%N)

##os.system("pause")
time.sleep(15)
