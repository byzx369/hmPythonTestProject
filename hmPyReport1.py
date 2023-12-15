#### from hm199report.py

import unittest
from HTMLTestRunner import HTMLTestRunner

suite=unittest.defaultTestLoader.discover('.', 'hmPyTest1.py')
file= 'hmPyTestReport1.html'
with open(file, 'w') as f:
    runner =HTMLTestRunner(f, 2,"PyTestReport1",'python3' )
    runner.run(suite)