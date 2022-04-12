# -*- coding: utf-8 -*-
# @Author  : Look at the stars
# @Time    : 2022/2/25 17:10
# @File    : MQ3.py
# @Software: PyCharm

import smbus

# 第一阶段电压-PPM转换
# volat = [1.54, 3.482]
def gas_1(volat):
    return -111.080423 + 72.01658 * volat


# 第二阶段电压-PPM转换
# volat = (3.482, 3.975]
def gas_2(volat):
    return 7868.159413 - 4363.868362 * volat + 617.37 * (volat ** 2)


# 指数拟合
# return 0.99689*math.exp(1.40569*volat)

# 第三阶段电压-PPM转换
# volat = [3.975, 4.2]
def gas_3(volat):
    return -3387.56585 + 922.075319 * volat


class Gas(object):
    def __init__(self, gasN):
        self.address = 0x48
        self.A0 = 0x40
        self.A1 = 0x41
        self.A2 = 0x42
        self.A3 = 0x43
        self.gasN = gasN

        self.bus = smbus.SMBus(1)
        self.bus.write_byte(self.address, self.A0)

    def getGas(self):
        value = self.bus.read_byte(self.address)
        volat = value / 105 * 4.216
        gas = 0.0
        try:
            if 0 <= volat <= 1.54:
                gas = 0.0
            elif volat <= 3.482:
                gas = gas_1(volat)
            elif volat < 3.975:
                gas = gas_2(volat)
            elif volat <= 4.215:
                gas = gas_3(volat)
        except:
            print("Gas ERROR!")
        self.gasN = float(gas)
        return self.gasN
