# -*- coding: UTF-8 -*-
'''
@Author  ：Jiangtao Shuai
@Date    ：09/02/2023 1:57 PM 
'''

import sys

print(sys.path)
import pysbf

if __name__ == '__main__':


    with open('../data/IMU_log.sbf') as sbf_fobj:
        for blockName, block in pysbf.load(sbf_fobj):
            print(blockName)
