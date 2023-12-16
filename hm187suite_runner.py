####### 黑马程序员Python自动测试教程 p187 testSuite
####### https://www.bilibili.com/video/BV1av411q7dT/?p=187&spm_id_from=pageDriver&vd_source=ef6907a52140ec8bee8c418335efac9d
#######

###1. 导包(unittest)
import unittest
###2. 实例化（创建对象）套件对象
from hm187testcase1 import TestDemo1
from hm187testcase2 import TestDemo2

###3. 使用套件对象添加用力方法
suite=unittest.TestSuite()

### App1方式一， 套件对象.addTest（测试类名（‘方法名’）） ## 建议测试类名和方法名直接去复制，不要手写
suite.addTest(TestDemo1('test_method1'))
suite.addTest(TestDemo1('test_method2'))
suite.addTest(TestDemo2('test_method1'))
suite.addTest(TestDemo2('test_method2'))

### App2方式二，将一个测试类中的所有方法进行添加
### 套件对象.addTest(unittest.makeSuite(测试类))
### unittest.makeSuite() is deprecated and will be removed in Python 3.13. Please use unittest.TestLoader.loadTestsFromTestCase() instead.
suite.addTest(unittest.makeSuite(TestDemo1))
suite.addTest(unittest.makeSuite(TestDemo2))

###4. 实例化运行对象
runner=unittest.TextTestRunner()
###5. 使用运行对象去执行套件对象
###运行对象.run（套件对象）
runner.run(suite)

