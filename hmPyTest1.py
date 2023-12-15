### hm190+hm197+hm198+data.json

import json
import unittest
from parameterized import parameterized
from hm192tools import login
from tools import add

def build_data():
    with open('data.json', encoding="utf-8")as f:
        result=json.load(f)  ###[{},{},{}]
        data=[]
        for i in result: ### i={}
            data.append((i.get('username'), i.get('password'), i.get('expect')))
    return data

class TestLogin(unittest.TestCase):
    @parameterized.expand(build_data())
    def test_login(self, username, password, expect):
        self.assertEqual(expect, login(username,password))

version=30
class TestDemo(unittest.TestCase):
    @unittest.skip("No reason, just don't want to run")
    def test_1(self):
        print('Test Method 1')

    @unittest.skipIf(version >=30, 'version>=30, so skip')
    def test_2(self):
        print('Test Method 2')

    def test_3(self):
        print('Test Method 3')

class TestAdd(unittest.TestCase):
    def test_method1(self):
        if add(1,2)==3:
            print("Test Pass")
        else: print("Test Fail")

    def test_method2(self):
        if add(10,20)==30:
            print("Test Pass")
        else: print("Test Fail")

    def test_method3(self):
        if add(2,3)==5:
            print("Test Pass")
        else: print("Test Fail")
