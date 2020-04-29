from page.home_page import HomePage
from common.function import current_time, conf
import time


class ProjBuildPage(HomePage):


    # 新增单位
    @property
    def add_addOrg_btn(self):
        return self.by_xpath('//*[@id="orgFm"]/table/tbody/tr[1]/td[1]/span/a')

    # 查找机构名称
    def add_addOrg_orgList_radio(self, orgName):  # 机构名称test201905161001
        current_time('招标单位:%s' % orgName)
        return self.by_xpath('//div[text()="%s"]' % orgName)

    # 新增单位选择按钮
    @property
    def add_addOrg_select_btn(self):
        return self.by_xpath('//*[@id="orgDlgBtn"]/a[1]')

    # 项目资金构成-资金来源
    def pjFunds_select(self, funds):
        fd = {'财政': 'finance', '自筹': 'selfRaise', '财政加自筹': 'fAnds', '其他': 'otherSource'}
        return self.by_id(fd[funds])

    # 项目资金构成-其它
    @property
    def pjFunds_otherSource_text_field(self):
        return self.by_xpath('//*[@id="projFm"]/fieldset[1]/table/tbody/tr[1]/td/div/span/input[1]')

    # 项目投资总额
    @property
    def pjFunds_totalInvest_text_field(self):
        return self.by_xpath('//input[@name="totalInvest"]/../input[1]')

    # 文件标题
    @property
    def pjDoc_fileTitle_text_field(self):
        return self.by_xpath('//input[@name="fileTitle"]/../input[1]')

    # 立项机关
    @property
    def pjDoc_projOffice_text_field(self):
        return self.by_xpath('//input[@name="projOffice"]/../input[1]')

    # 立项文号
    @property
    def pjDoc_projNumber_text_field(self):
        return self.by_xpath('//input[@name="projNumber"]/../input[1]')

    # 选择立项日期
    @property
    def pjDoc_projDate_choice(self):
        current_time('选择立项日期')
        self.by_xpath('//input[@name="projDate"]/../span/a').click()
        self.by_xpath("//a[text()='今天']").click()
        projDate = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        current_time('立项日期:%s' % projDate)
        return projDate

    # 立项备注
    @property
    def pjDoc_projRemark_text_field(self):
        return self.by_xpath('//input[@name="projRemark"]/../input[1]')

    # 项目名称
    @property
    def pjInfo_projName_text_field(self):
        return self.by_xpath('//input[@name="projName"]/../input[1]')

    # 项目法人
    @property
    def pjInfo_projLegalman_text_field(self):
        return self.by_xpath('//input[@name="projLegalman"]/../input[1]')

    # 项目联系人
    @property
    def pjInfo_projContactman_text_field(self):
        return self.by_xpath('//input[@name="projContactman"]/../input[1]')

    # 项目联系方式
    @property
    def pjInfo_projContactWay_text_field(self):
        return self.by_xpath('//input[@name="projContactWay"]/../input[1]')

    # 项目建设地点
    @property
    def pjInfo_projSite_text_field(self):
        return self.by_xpath('//input[@name="projName"]/../input[1]')

    # 选择项目所在行政区
    def pjInfo_projRegion_choice(self):
        current_time('选择项目所在行政区')
        self.by_xpath('//*[@id="_easyui_tree_1"]/span[1]').click()  # 省
        self.by_xpath('//*[@id="_easyui_tree_2"]/span[2]').click()  # 市
        self.by_xpath('//*[@id="_easyui_tree_3"]/span[5]').click()  # 区
        self.by_id('_easyui_tree_1').click()
        current_time('项目所在行政区:北京市市辖区东城区')
        return '北京市市辖区东城区'

    # 选择项目行业分类
    def pjInfo_projClass_chocie(self):
        current_time('选择项目行业分类')
        current_time('选择[建筑业]')
        self.by_xpath('//*[@id="projFm"]/fieldset[3]/table/tbody/tr[7]/td[2]/span[1]/span/a').click()
        self.by_id('_easyui_combobox_i3_0').click()
        current_time('选择[建筑业-房屋建筑业]')
        self.by_xpath('//*[@id="projFm"]/fieldset[3]/table/tbody/tr[7]/td[2]/span[2]/span/a').click()
        self.by_id('_easyui_combobox_i9_0').click()
        current_time('选择[建筑业-房屋建筑业-房屋建筑业]')
        self.by_xpath('//*[@id="projFm"]/fieldset[3]/table/tbody/tr[7]/td[2]/span[3]/span/a').click()
        self.by_id('_easyui_combobox_i11_0').click()
        current_time('选择[建筑业-房屋建筑业-房屋建筑业-房屋建筑业]')
        self.by_xpath('//*[@id="projFm"]/fieldset[3]/table/tbody/tr[7]/td[2]/span[4]/span/a').click()
        self.by_id('_easyui_combobox_i12_0').click()
        return "建筑业-房屋建筑业-房屋建筑业-房屋建筑业"

    def pjInfo_projOpenType_choice(self, openType):  # 项目公开类型
        # 依法公开/网站公开/不公开
        current_time('选择项目公开类型')
        self.by_xpath('//*[@id="projFm"]/fieldset[3]/table/tbody/tr[8]/td[2]/span/span/a').click()
        self.by_xpath('//div[text()="%s"]' % openType).click()
        return openType

    def pjInfo_tdForm_choice(self, tdForm):  # 招标组织形式
        # 委托招标/自行招标
        current_time('选择招标组织形式')
        tf = {'委托招标': 'deputeBid', '自行招标': 'selfBid'}
        self.by_xpath('//input[@id="%s"]' % tf[tdForm])

    def pjInfo_projScale_text_field(self):  # 工程规模
        return self.by_xpath('//input[@name="projScale"]/../textarea')

    @property
    def pjInfo_submit_btn(self):
        return self.by_xpath('//*[@id="addDlgBtn"]/a[1]')

    def choice_org(self, orgName):
        self.add_addOrg_btn.click()  # 点击单位选择按钮
        self.add_addOrg_orgList_radio(orgName).click()  # 选择项目
        self.add_addOrg_select_btn.click()

    # 项目报建新增
    def add_pjBuild(self):
        self.switch_driver()
        HomePage(self.driver).enter_page('项目报建')
        ymd = time.strftime('%Y%m%d-%H%M%S', time.localtime(time.time()))
        self.add_btn.click()  # 点击新增按钮
        self.choice_org('机构名称test201905161001')
        # self.pjFunds_select('财政加自筹').click() # 默认选择[财政]
        self.pjFunds_totalInvest_text_field.send_keys('1000')  # 项目投资总额
        self.pjDoc_fileTitle_text_field.send_keys("test文件标题-" + ymd)  # 文件标题
        self.pjDoc_projOffice_text_field.send_keys("test_机关")  # 立项机关
        projNumber = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        self.pjDoc_projNumber_text_field.send_keys(projNumber)  # 立项文号
        self.pjDoc_projDate_choice()  # 立项日期
        self.pjDoc_projRemark_text_field.send_keys(
            'test_projRemark_%s' % time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())))  # 立项备注
        self.projName = '%s-%s-%s' % (ymd, conf('config', 'Version'), conf('config', 'projName'))  # 项目名称
        self.pjInfo_projName_text_field.send_keys(self.projName)
        self.pjInfo_projLegalman_text_field.send_keys('test_legalman_李cc')  # 项目法人
        self.pjInfo_projContactman_text_field.send_keys('test_cont_李cc')  # 项目联系人
        self.pjInfo_projContactWay_text_field.send_keys('13300000000')  # 项目联系方式
        self.pjInfo_projSite_text_field.send_keys('湖北省武汉市硚口区')  # 项目建设地点
        self.pjInfo_projRegion_choice()  # 项目所在行政区:北京市市辖区东城区
        self.pjInfo_projClass_chocie()  # 项目行业分类:建筑业-房屋建筑业-房屋建筑业-房屋建筑业
        self.pjInfo_projOpenType_choice('依法公开')  # 项目公开类型
        self.pjInfo_tdForm_choice('委托招标')  # 招标组织形式
        self.pjInfo_projSite_text_field.send_keys('工程规模xxxxxx-%s' % ymd)
        self.pjInfo_submit_btn.click()  # 提交
        try:
            self.by_xpath('//div[text()="%s"]' % self.projName)
        except:
            return "failed"
        else:
            return "success"

    # 项目报建审核
    # def audit_pjBuild(self):
    #     HomePage(self.driver).change_role('审核人', self.driver)
    #     HomePage(self.driver).enter_page('项目报建')  # 进入项目报建iframe页面
    #     iframe_ele = self.by_xpath("//*[@id='mainTabs']/DIV[2]/DIV[2]/DIV/IFRAME")  # 切换iframe
    #     self.driver.switch_to.frame(iframe_ele)
    #     self.state_btn('待审核').click()
    #     self.by_xpath('//div[text()="%s"]' % self.projName).click()
    #     self.audit_btn.click()
    #     self.audit_info_submit_btn.click()  # 点击提交
    #     self.tips_submit_btn.click()
    #     try:
    #         self.by_xpath('//div[text()="操作成功"]')
    #     except:
    #         return "fail"
    #     else:
    #         self.by_xpath('//div[text()="操作成功"]/../../div[3]/a').click()
    #         return "success"
