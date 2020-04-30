from common.function import conf, current_time, change_sc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time, os

default_seconds = int(conf('config', 'DEFAULT_SECONDS'))
the_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class BasePage(object):

    # 初始化基础类
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.projName = '2020-04-28-auto'
        self.projNo = None
        self.LotName = None
        self.tdProjName = 'E4201000127000717002'

    # id定位元素,定位失败则自动截图
    def by_id(self, the_id, ds=default_seconds):
        # 显示等待

        try:
            WebDriverWait(self.driver, ds).until(EC.visibility_of_element_located((By.ID, the_id)))
        except Exception as e:
            file_name = the_path + '/screenshots/%s.png' % (time.strftime("%Y-%m-%d_%H_%M_%S"))
            self.driver.get_screenshot_as_file(file_name)
            change_sc(file_name, the_id)
            msg = "找不到元素" + the_id
            # print(msg)
            raise TimeoutException(msg)

        # 隐式等待
        # driver.implicitly_wait(2)
        return self.driver.find_element_by_id(the_id)

    def by_xpath(self, the_xpath, ds=default_seconds):
        # 显示等待
        try:
            WebDriverWait(self.driver, ds).until(EC.visibility_of_element_located((By.XPATH, the_xpath)))
        except Exception as e:
            file_name = the_path + '/screenshots/%s.png' % time.strftime("%Y-%m-%d_%H_%M_%S")
            self.driver.get_screenshot_as_file(file_name)
            change_sc(file_name, the_xpath)
            msg = "找不到元素" + the_xpath
            print(msg)
            # raise TimeoutException(msg)

            # 隐式等待
            # driver.implicitly_wait(2)
        return self.driver.find_element_by_xpath(the_xpath)

    def by_xpath_complex(self, the_xpath, ds=default_seconds):
        # 显示等待
        try:
            WebDriverWait(self.driver, ds).until(EC.visibility_of_all_elements_located((By.XPATH, the_xpath)))
        except Exception as e:
            self.driver.get_screenshot_as_file(the_path + '/screenshots/%s.png' % time.strftime("%Y-%m-%d_%H_%M_%S"))
            msg = "找不到元素" + the_xpath
            # print(msg)
            raise TimeoutException(msg)

        # 隐式等待
        # driver.implicitly_wait(2)
        return self.driver.find_elements_by_xpath(the_xpath)

    def switch_driver(self):
        driver = self.driver
        current_window = driver.current_window_handle
        all_window = driver.window_handles
        for window in all_window:
            if window != current_window:
                driver.switch_to.window(window)
        current_window = driver.current_window_handle
        return current_window

    def excute_script(self, ele):
        return self.driver.execute_script('arguments[0].click();', ele)

    def switch_frame(self, frame):
        iframe_ele = self.by_xpath(frame)
        self.driver.switch_to.frame(iframe_ele)
        current_time('切换iframe-success')
