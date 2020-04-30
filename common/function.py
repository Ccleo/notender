import configparser
import os, shutil
import requests
import base64
import time
import cv2
from pywinauto import application

the_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def conf(section, item):
    con = configparser.ConfigParser()
    conf_path = os.path.join(the_path, 'conf.ini')
    con.read(conf_path, encoding='utf-8')
    value = con.get(section, item)
    return value


def current_time(casename=None):
    current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    if casename:
        print(current_time + "---" + casename)
    else:
        return current_time


def baidu_orc(pin_url):
    '''调用百度文字识别通用接口
    :param codeImageUrl:
    :return:
    '''

    API_KEY = conf('Baidu_orc', 'API_KEY')
    SECRET_KEY = conf('Baidu_orc', 'SECRET_KEY')
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s' % (
        API_KEY, SECRET_KEY)
    response = requests.get(host)
    if response:
        print(response.json())
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
    # 二进制方式打开图片文件
    f = open(pin_url, 'rb')
    img = base64.b64encode(f.read())

    params = {"image": img}
    if response:
        access_token = response.json()['access_token']
    else:
        return "No access_token"
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        pin = response.json()
        print(pin)
        try:
            pin = response.json()['words_result'][0]['words'].replace(' ', '')
            # PIN = response.json()['words_result'][0]['words'] # 调试验证码校验

            return pin
        except:
            return None


def upload(file_url):
    app = application.Application()
    # 这里用的class而没有加窗口title，主要为了保证兼容性
    app.connect(class_name='#32770')  # 根据class_name找到弹出窗口
    app["Dialog"]["Edit1"].TypeKeys(file_url)  # 在输入框中输入值
    app["Dialog"]["Button1"].click()  # 点击打开/保存按钮

    # windows控件上传文件
    # def upload(file, title=u'选择要上载的文件，通过: 192.168.1.248'):
    #     dialog = win32gui.FindWindow('#32770', title)
    #     ComboBoxEx = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
    #     ComboBox = win32gui.FindWindowEx(ComboBoxEx, 0, 'ComboBox', None)
    #     Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)
    #     button = win32gui.FindWindowEx(dialog, 0, 'Button', None)
    #     time.sleep(0.5)
    #     win32gui.SendMessage(Edit, win32con.WM_SETTEXT, 0, file)
    #     time.sleep(0.5)
    #     win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)
    #     time.sleep(0.5)


def del_screenshots(path_data):
    for i in os.listdir(path_data):  # os.listdir(path_data)#返回一个列表，里面是当前目录下面的所有东西的相对路径
        file_data = path_data + "\\" + i  # 当前文件夹的下面的所有东西的绝对路径
        if os.path.isfile(file_data) == True:  # os.path.isfile判断是否为文件,如果是文件,就删除.如果是文件夹.递归给del_file.
            os.remove(file_data)
        else:
            del_screenshots(file_data)


def change_sc(file_name, xpath):
    bk_img = cv2.imread(file_name)
    # 在图片上添加文字信息
    cv2.putText(bk_img, xpath, (40, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 0, 255), 1, cv2.LINE_AA)
    cv2.imwrite(file_name, bk_img)
