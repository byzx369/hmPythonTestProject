####### 黑马程序员Python自动测试教程 p187 testSuite
####### https://www.bilibili.com/video/BV1av411q7dT/?p=187&spm_id_from=pageDriver&vd_source=ef6907a52140ec8bee8c418335efac9d
#######

###1. 导包
import unittest

###2. 自定义测试类， 需要继承unittest 模块中的TestCase类即可
class TestDemo2(unittest.TestCase):
### 3. 书写测试方法， 即用例代码， 目前没有真正的用例代码， 使用print代替
### 书写要求，测试方法，必须以 test_开头（本质是以test 开头）
    def test_method1(self):
        print('TestMethod2-1')

    def test_method2(self):
        print('TestMethod2-2')
    
### 4.执行用例（方法）
### 4.1 将光标放在类名的后边 运行， 会执行类中的所有的测试方法
### 4.2 将光标放在方法名的后边 运行， 只执行当前的方法
