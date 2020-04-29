# coding=utf-8
import time
import pytest

'''
说明：
1、用例创建原则，测试文件名必须以“test”开头，测试函数必须以“test”开头。
2、用例运行策略，
*  -s 指定运行目录或文件(可以不加)，例: -s  ./test_case/ ,  -s  /test_case/test_demo.py
*  -q 不打印版本信息
*  --html  指定测试报告目录及文件名。
*  --self-contained-html 表示创建独立的测试报告。
*  --reruns 3   指定用例失败重跑次数。
'''

now_time = time.strftime("%Y-%m-%d_%H_%M_%S")
if __name__ == "__main__":
    pytest.main(["-s", "testcase/", "--html=./reports/"+now_time+" report.html"])
