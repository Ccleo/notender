from page.base_page import BasePage
from page.login_page import LoginPage
from common.function import current_time


class HomePage(BasePage):
    @property
    def pm_btn_xpath(self):  # 项目管理
        return '/html/body/div[2]/div/ul/li[1]/a'

    @property
    def pm_projBuild_btn_xpath(self):  # 项目报建
        return '//a[@name="pm/projBuild"]'

    @property
    def pm_tenderProjRecord_btn_xpath(self):  # 招标项目备案
        return '//a[@name="pm/tenderProjRecord"]'

    @property
    def tdBack_btn_xpath(self):  # 招标过程
        return '/html/body/div[2]/div/ul/li[2]/a'

    @property
    def tdBack_bidDocRecord_btn_xpath(self):  # 招标文件备案
        return '//a[@name="td/back/bidDocRecord"]'

    @property
    def tdBack_bidDocNotice_btn_xpath(self):  # 招标公告
        return '//a[@name="td/back/bidDocNotice"]'

    @property
    def tdBack_bidInvitation_btn(self):  # 投标邀请书
        return self.by_xpath('//a[@name="td/back/bidInvitation"]')

    @property
    def tdBack_supplyChangeNotice_btn(self):  # 补充变更公告
        return self.by_xpath('//a[@name="td/back/supplyChangeNotice"]')

    @property
    def tdBack_bidDocClarify_btn(self):  # 招标文件澄清修改
        return self.by_xpath('//a[@name="td/back/bidDocClarify"]')

    @property
    def openBd_btn(self):  # 开评标
        return self.by_xpath('/html/body/div[2]/div/ul/li[3]/a')

    @property
    def openBd_bidOpenRecord_btn(self):  # 开标记录
        return self.by_xpath('//a[@name="openbd/bidOpenRecord"]')

    @property
    def openBd_evalCommiteeBuild_btn(self):  # 组建评标委员会
        return self.by_xpath('//a[@name="openbd/evalCommiteeBuild"]')

    @property
    def openBd_evalBidReport_btn(self):  # 评标报告
        return self.by_xpath('//a[@name="openbd/evalBidReport"]')

    @property
    def openBd_openbdCandidatePublic_btn(self):  # 中标候选人公示
        return self.by_xpath('//a[@name="openbd/openbdCandidatePublic"]')

    @property
    def openBd_winBidResultNotice_btn(self):  # 中标结果公示
        return self.by_xpath('//a[@name="openbd/winBidResultNotice"]')

    @property
    def em_btn(self):  # 费用管理
        return self.by_xpath('/html/body/div[2]/div/ul/li[4]/a')

    @property
    def em_advancePayQuery_btn(self):  # 投标保证金进账查询
        return self.by_xpath('//a[@name="em/advancePayQuery"]')

    @property
    def em_bidDocFeeQuery_btn(self):  # 文件费进账查询
        return self.by_xpath('//a[@name="em/bidDocFeeQuery"]')

    @property
    def sys_btn(self):  # 子锁用户录入
        return self.by_xpath('/html/body/div[2]/div/ul/li[5]/a')

    @property
    def sys_userManage_btn(self):  # 子锁用户管理
        return self.by_xpath('//a[@name="sys/userManage"]')

    @property
    def func_changeRole_btn(self):  # 切换角色
        return self.by_xpath('//*[@id="changeRole"]')

    def state_btn(self, state):
        sd = {'全部状态': 1, '未提交': 2, '待审核': 3, '审核通过': 4, '审核未通过': 5}
        return self.by_xpath('//*[@id="stateBtn"]/a[%d]' % sd[state])

    @property
    def audit_btn(self):
        return self.by_xpath('//*[@id="auditBtn"]/span')

    @property
    def audit_info_submit_btn(self):
        return self.by_xpath('//*[@id="auditDlgBtn"]/a[1]')

    @property
    def tips_submit_btn(self):
        return self.by_xpath('/html/body/div[31]/div[3]/a[1]')

    @property
    def operate_success_btn(self):
        return self.by_xpath('//div[text()="操作成功"]/../../div[3]/a')

    @property
    def frame_xpath(self):
        return "//*[@id='mainTabs']/DIV[2]/DIV[2]/DIV/IFRAME"

    def change_role(self, role):
        self.driver.switch_to.default_content()  # 切换到主iframe
        self.func_changeRole_btn.click()  # 点击切换角色按钮
        self.switch_driver()  # 页面跳转切换driver
        LoginPage(self.driver).choice_role(role)
        self.switch_driver()

    # 进入菜单页面
    def enter_page(self, page):
        dc = {'项目报建': (self.pm_btn_xpath, self.pm_projBuild_btn_xpath),
              '招标项目备案': (self.pm_btn_xpath, self.pm_tenderProjRecord_btn_xpath),
              '招标文件备案': (self.tdBack_btn_xpath, self.tdBack_bidDocRecord_btn_xpath),
              '招标公告': (self.tdBack_btn_xpath, self.tdBack_bidDocNotice_btn_xpath)}
        try:
            self.by_xpath('/html/body/div[33]/div[3]/a', ds=2)  # 预留3秒寻找是否有修改密码弹窗
        except:
            return 'No Popup'
        else:
            self.by_xpath('/html/body/div[33]/div[3]/a', ds=3).click()
            current_time('关闭修改密码提示弹窗')
        self.by_xpath(dc[page][0]).click()
        self.by_xpath(dc[page][1]).click()
        current_time('点击%s' % page)
        self.switch_frame(self.frame_xpath)

    # 审核
    def audit(self, type):
        self.change_role('审核人')
        self.enter_page(type)  # 进入type对应项目的iframe页面
        iframe_ele = self.by_xpath("//*[@id='mainTabs']/DIV[2]/DIV[2]/DIV/IFRAME")  # 切换iframe
        self.driver.switch_to.frame(iframe_ele)
        self.state_btn('待审核').click()
        self.by_xpath('//div[text()="%s"]' % self.tdProjName).click()  # 根据招标项目选择对应待审核项目
        self.audit_btn.click()  # 点击审核按钮
        self.audit_info_submit_btn.click()  # 点击提交
        self.tips_submit_btn.click()
        self.operate_success_btn.click()
        self.state_btn('审核通过').click()  # 在审核通过列表中寻找
        try:
            audit_state = self.by_xpath('//div[text()="%s"]/../../td[@field="auditState"]/div' % self.tdProjName).text
        except:
            return "fail"
        else:
            return audit_state

    # 新增按钮
    @property
    def add_btn(self):
        return self.by_id('addBtn')
    # 切换到主iframe
