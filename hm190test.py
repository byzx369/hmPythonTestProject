####### 黑马程序员Python自动测试教程 p189 案例练习
####### https://www.bilibili.com/video/BV1av411q7dT/?p=190&spm_id_from=pageDriver&vd_source=ef6907a52140ec8bee8c418335efac9d
#######案例练习

### 1 导包
import unittest
from tools import add
### 2 自定义测试类
class TestAdd(unittest.TestCase):
    ### 3. 书写测试方法，就是测试用例代码
    def test_method1(self):
        ### 1,2,3判断实际结果和预期结果是否相符
        if add(1,2)==3:
            print("Test Pass")
        else: print("Test Fail")

    def test_method2(self):
        ### 1,2,3判断实际结果和预期结果是否相符
        if add(10,20)==30:
            print("Test Pass")
        else: print("Test Fail")

    def test_method3(self):
        ### 1,2,3判断实际结果和预期结果是否相符
        if add(2,3)==5:
            print("Test Pass")
        else: print("Test Fail")

