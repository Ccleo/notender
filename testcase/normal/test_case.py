'''
pytest会找当前以及递查找子文件夹下面所有的test_*.py或*_test.py的文件，把其当作测试文件
在这些文件里，pytest会收集下面的一些函数或方法，当作测试用例
不在类定义中的以test_开头的函数或方法
在以Test开头的类中(不能包含__init__方法)，以test_开头的方法
pytest也支持unittest模式的用例定义

setup_class/teardown_class 在当前测试类的开始与结束执行。
setup/treadown 在每个测试方法开始与结束执行。
setup_method/teardown_method 在每个测试方法开始与结束执行，与 setup/treadown 级别相同
setup_module/teardown_module 在所有测试用例执行之后和之后执行。
setup_function/teardown_function 在每个测试用例之后和之后执行。

'''
import os, sys  # 处理导入模块目录问题

my_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# 返回当前文件的path规范化的绝对路径os.path.abspath()
sys.path.insert(0, my_path)
from selenium import webdriver
from page.login_page import LoginPage
from page.home_page import HomePage
from page.pm_projBuild_page import ProjBuildPage
from page.pm_tenderProjRecord_page import TenderProjRecordPage
from common.function import current_time, conf, del_screenshots
from page.td_bidDocRecord_page import BidDocRecordPage


class Test_NoTender_NormalCase():
    """使用本地selenium"
    #     self.driver = webdriver.Chrome()
    #     # GlobalVar().set_value('driver', self.driver)
    #     self.driver.implicitly_wait(10)
    #     self.BASE_URL = getConfig('URL', 'BASE_URL')
    #     self.LP = LoginPage(self.driver)
    '''使用selenim grid'''
    # HUB_IP = getConfig('Selenium', 'HUB_IP')
    # self.driver = webdriver.Remote(command_executor=HUB_IP,desired_capabilities=DesiredCapabilities.CHROME)
    # self.driver.implicitly_wait(10)
    # self.BASE_URL = getConfig('URL', 'BASE_URL')
    # self.LP = LoginPage(self.driver)"""

    def setup(self):
        self.driver = webdriver.Chrome()
        self.url = conf('URL', 'base_url')
        self.driver.get(self.url)

    def teardown(self):
        self.driver.quit()

    def test_login(self):
        result = LoginPage(self.driver).login('华杰工程咨询有限公司', '000000')
        print(result)
        assert result == "login_success"  # todo:测试-登录页-登录功能

    def test_proj_build_audit(self):
        LP = LoginPage(self.driver)
        HP = HomePage(self.driver)
        BDRP = BidDocRecordPage(self.driver)
        LP.choice_role('招标代理')
        HP.enter_page('招标文件备案')
        BDRP.add_bidDocRecord()

del_screenshots(os.path.join(conf('config','root_dir'),'screenshots'))
run = Test_NoTender_NormalCase()
run.setup()
run.test_login()
run.test_proj_build_audit()
run.teardown()
