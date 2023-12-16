####### 黑马程序员Python自动测试教程 p190 案例练习
####### https://www.bilibili.com/video/BV1av411q7dT/?p=190&spm_id_from=pageDriver&vd_source=ef6907a52140ec8bee8c418335efac9d
#######案例练习

### 1 导包
import unittest
### 实例化套件对象
from hm190test import TestAdd

suite=unittest.TestSuite()
### 添加测试方法
suite.addTest(unittest.makeSuite(TestAdd)) ### 一般需要改变
# suite.addTest(unittest.TestLoader.loadTestsFromTestCase(TestAdd))  ###XXX
### 实例化执行对象
runner=unittest.TextTestRunner()
runner.run(suite)





