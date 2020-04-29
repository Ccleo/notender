from page.base_page import BasePage
from common.function import conf, current_time, baidu_orc
# from common.Globalvar import *
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
import time
import os
from PIL import Image


class LoginPage(BasePage):
    @property
    def username_text_field(self):
        return self.by_id('username')

    @property
    def password_text_field(self):
        return self.by_id('password')

    @property
    def pin_text_field(self):
        return self.by_id('randomCode')

    @property
    def login_btn(self):
        return self.by_xpath('//*[@id="loginForm"]/div/div/div[1]/input')

    @property
    def pin_img(self):
        return self.by_id('vimg')

    @property
    def change_key_window(self):
        return self.by_xpath('/html/body/div[33]/div[2]/div[2]')

    def role_btn(self, role):
        return self.by_xpath('//*[text()="%s"]' % role)

    def get_pin_url(self):
        pin_imgDir_url = os.path.join(conf('config', 'root_dir'), 'common', 'PIN')
        self.driver.save_screenshot(os.path.join(pin_imgDir_url, "01.png"))
        ran = Image.open(os.path.join(pin_imgDir_url, "01.png"))
        box = eval(conf('config', 'box'))  # 获取验证码位置,手动定位，（左，上，右，下）,用画图工具打开后定位即可
        pin_url = os.path.join(pin_imgDir_url, "02.png")
        ran.crop(box).save(pin_url)
        return pin_url

    def enter_pin(self):
        pin_url = self.get_pin_url()
        pin = baidu_orc(pin_url)
        if pin:
            self.pin_text_field.clear()
            self.pin_text_field.send_keys(pin)
        else:
            self.pin_img.click()
            self.enter_pin()

    def login(self, username, password):
        # self.driver = webdriver.Chrome()
        # self.driver.get()
        self.username_text_field.clear()
        self.username_text_field.send_keys(username)
        time.sleep(0.5)
        self.password_text_field.clear()
        self.password_text_field.send_keys(password)
        time.sleep(0.5)
        self.enter_pin()
        self.login_btn.click()
        try:
            info = self.by_xpath('/html/body/div/div/div[1]/ul/li[1]', 2).text
            if info == '请选择主体类型登录[退出登录]':
                current_time("登录成功")
                result = "login_success"
                return result
            else:
                result = 'login_fail'
                return result
        except:
            print('except')
            info = self.by_xpath('//*[@id="loginForm"]/div/div/div[2]/span', 1).text
            if info == "验证码错误":
                time.sleep(0.5)
                current_time("验证码错误")
                self.login(username, password)
            elif info == "用户名或密码错误":
                current_time("用户名或密码错误")
                self.login(username, password)
            else:
                result = 'login_error'
                return result


    def choice_role(self, role):
        # rd = {'招标代理': 'type-agent', '投标人': 'type-bidder', '审核人': 'type-audit', '招标人': 'type-tenderer',
        #       '系统管理员': 'type-superAdmin', '运营单位': 'type-operationUnit'}
        self.switch_driver()
        self.role_btn(role).click()
        try:
            if self.change_key_window.text == '您的登录密码已经长时间未作修改，建议您每三个月修改一次！':
                current_time('切换[%s]角色成功' % role)
                self.switch_driver()
                return 'success'
        except:
            current_time('切换[%s]角色失败' % role)
            return 'fail'
