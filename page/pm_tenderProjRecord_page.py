from page.home_page import HomePage
from common.function import current_time, conf, upload
import random, os


class TenderProjRecordPage(HomePage):

    @property
    def add_btn(self):
        return self.by_xpath('//*[@id="addBtn"]')

    @property
    def proj_choice_btn(self):
        return self.by_xpath('//*[@id="addTr"]/td[1]/span/a')

    @property
    def choice_proj_search_text_field(self):
        return self.by_xpath('//input[@id="projSearch"]/../span/input')

    @property
    def choice_proj_search_btn(self):
        return self.by_xpath('//input[@id="projSearch"]/../span/span')

    @property
    def choice_proj_choice_btn(self):
        return self.by_xpath('//*[@id="projDlgBtn"]/a[1]')

    # 选择项目-搜索项目功能
    def choice_proj_search_func(self):
        self.choice_proj_search_text_field.send_keys(self.projName)
        self.choice_proj_search_btn.click()
        try:
            # todo: 测试 - 新增招标项目备案 - 选择项目 - 项目名称搜索功能
            assert self.by_xpath('//tr[@id="datagrid-row-r15-2-0"]/td[5]/div') == self.projName
        except:
            return 'fail'
        else:
            self.by_xpath('//tr[@id="datagrid-row-r15-2-0"]/td[5]/div').click()
            self.choice_proj_choice_btn.click()

    # 选择项目
    def choice_proj(self):
        self.proj_choice_btn.click()
        self.choice_proj_search_func()  # 使用搜索功能选择项目

    @property
    def bPI_title_text_field(self):
        return self.by_xpath('//*[@id="tdProjFm"]/table/tbody/tr[1]/td[2]/span/input[1]')

    # 采购类型
    def bPI_bdMode_choice_btn(self, mode):
        cd = {'招标': 1, '比选': 2, '询价': 3, '单一来源': 4, '竞争性谈判': 5, '竞争性磋商': 6, '其它': 7}
        return self.by_xpath('//form[@id="tdProjFm"]/table/tbody/tr[4]/td[2]/ul/li[%d]/input' % cd[mode])

    # 采购方式
    def bPI_bdWay_choice_btn(self, mode):
        cd = {'公开': 1, '邀请': 2}
        return self.by_xpath('//form[@id="tdProjFm"]/table/tbody/tr[5]/td[2]/input[%d]' % cd[mode])

    # 监督部门编码
    @property
    def bPI_spDpCode_text_field(self):
        return self.by_xpath('//*[@id="tdProjFm"]/table/tbody/tr[6]/td[2]/span/input[1]')

    # 监督部门名称
    @property
    def bPI_spDpName_text_field(self):
        return self.by_xpath('//*[@id="tdProjFm"]/table/tbody/tr[6]/td[4]/span/input[1]')

    # 审核部门编码
    @property
    def bPI_adDpCode_text_field(self):
        return self.by_xpath('//*[@id="tdProjFm"]/table/tbody/tr[7]/td[2]/span/input[1]')

    # 审核部门名称
    @property
    def bPI_adDpName_text_field(self):
        return self.by_xpath('//*[@id="tdProjFm"]/table/tbody/tr[7]/td[4]/span/input[1]')

    # 招标内容与范围
    @property
    def bPI_tdContentAndScope_text_field(self):
        return self.by_xpath('//*[@id="tdProjFm"]/table/tbody/tr[9]/td[2]/span/textarea')

    # 标段信息-添加标段
    @property
    def LI_addLot_btn(self):
        return self.by_xpath('//*[@id="secPart"]/div/div/div[1]/table/tbody/tr/td[1]/a')

    # 标段信息-修改标段
    @property
    def LI_changeLot_btn(self):
        return self.by_xpath('//*[@id="secPart"]/div/div/div[1]/table/tbody/tr/td[3]/a')

    # 标段信息-删除标段
    @property
    def LI_delLot_btn(self):
        return self.by_xpath('//*[@id="secPart"]/div/div/div[1]/table/tbody/tr/td[5]/a')

    @property
    def aL_name(self):
        return self.by_xpath('//*[@id="addSecFm"]/table/tbody/tr[1]/td[2]/span/input[1]')

    @property
    def aL_sectionEvalprice_text_field(self):
        return self.by_xpath('//*[@id="addSecFm"]/table/tbody/tr[5]/td[2]/span/input[1]')

    @property
    def aL_bdEnsureMoney_text_field(self):
        return self.by_xpath('//*[@id="addSecFm"]/table/tbody/tr[6]/td[2]/span/input[1]')

    @property
    def aL_highestPrice_text_field(self):
        return self.by_xpath('//*[@id="addSecFm"]/table/tbody/tr[7]/td[2]/span/input[1]')

    @property
    def aL_sectionContent_text_field(self):
        return self.by_xpath('//*[@id="addSecFm"]/table/tbody/tr[8]/td[2]/span/textarea')

    @property
    def aL_bdQualification_text_field(self):
        return self.by_xpath('//*[@id="addSecFm"]/table/tbody/tr[9]/td[2]/span/textarea')

    @property
    def aL_submit_btn(self):
        return self.by_xpath('//*[@id="addSecTool"]/a[1]')

    # @property
    # def LI_changeLot_btn(self):
    #     return self.by_xpath('//*[@id="secPart"]/div/div/div[1]/table/tbody/tr/td[3]/a')

    @property
    def nextStep_btn(self):
        return self.by_xpath('//*[@id="addDlgBtn"]/a[1]')

    @property
    def submitAudit_btn(self):
        return self.by_xpath('//*[@id="secAndAmDlgTool"]/a[1]')

    def fI_upload_btn(self, file_type):
        return self.by_xpath('//*[@id="datagrid-row-r8-2-%d"]/td[4]/div/a' % file_type)

    @property
    def fI_choice_file_btn(self):
        return self.by_xpath('//*[@id="file_upload"]')

    @property
    def aF_upload_file_btn(self):
        return self.by_xpath('//*[@id="SWFUpload_0"]')

    @property
    def aF_define_btn(self):
        return self.by_xpath('/html/body/div[42]/div[3]/a')

    @property
    def fI_submit_audit_btn(self):
        return self.by_xpath('//*[@id="secAndAmDlgTool"]/a[1]')

    @property
    def fI_submit_define_btn(self):
        return self.by_xpath('//div[text()="确定要将该数据提交至待审核状态？"]/../../div[3]/a')

    @property
    def fI_operat_success_btn(self):
        return self.by_xpath('//div[text()="操作成功"]/../../div[3]/a')

    # 选择标段类别
    def aL_choice_LotType(self):
        self.by_xpath('//*[@id="addSecFm"]/table/tbody/tr[2]/td[2]/span[1]/span/a').click()  # 点击下拉按钮1
        self.by_xpath('//*[@id="_easyui_combobox_i3_0"]').click()  # 选择[工程]
        self.by_xpath('//*[@id="addSecFm"]/table/tbody/tr[2]/td[2]/span[2]/span/a').click()  # 点击下拉按钮2
        self.by_xpath('//*[@id="_easyui_combobox_i6_0"]').click()  # 选择[规划]
        self.by_xpath('//*[@id="addSecFm"]/table/tbody/tr[2]/td[2]/span[2]/span/a').click()  # 点击下拉按钮2
        self.by_xpath('//*[@id="_easyui_combobox_i8_0"]').click()  # 选择[国民经济和社会发展规划]
        self.by_xpath('//*[@id="addSecFm"]/table/tbody/tr[2]/td[2]/span[4]/span/a').click()  # 点击下拉按钮3
        self.by_xpath('//*[@id="_easyui_combobox_i9_0"]').click()  # 选择[总体规划]
        return '工程-规划-国民经济和社会发展规划-总体规划'

    # 添加标段
    def add_Lot(self):
        self.LI_addLot_btn.click()
        self.LotName = self.projName + '-bd01'  # 标段名称
        self.aL_name.send_keys(self.LotName)
        self.aL_choice_LotType()
        self.aL_sectionEvalprice_text_field.send_keys('1')  # 合同估算价 1
        self.aL_bdEnsureMoney_text_field.send_keys('0.01')  # 投标保证金 0.01
        self.aL_highestPrice_text_field.send_keys('999999999')  # 最高限价
        self.aL_sectionContent_text_field.send_keys('test-添加标段-%s' % current_time())
        self.aL_submit_btn.click()
        try:
            # todo:测试-新增招标项目备案-标段信息-添加标段功能
            assert self.by_xpath('//*[@id="datagrid-row-r2-2-0"]/td[4]/div').text == self.LotName
        except:
            return 'add Lot fail'
        else:
            return 'add Lot success'

    # 修改标段
    def change_Lot(self):
        pass

    # 删除标段
    def del_Lot(self):
        pass

    # 附件信息上传
    def add_file(self, i):
        dc = {0: '招标条件备案申请表', 1: '招标方式核准表', 2: '招标文件在行业主管部门备案证明', 3: '法人授权委托书', 4: '被委托人身份证',
              5: '招标项目负责人身份证', 6: '招标代理合同', 7: '资金到位证明', 8: '其他文件'}
        self.fI_upload_btn(i).click()
        self.fI_choice_file_btn.click()
        self.aF_upload_file_btn.click()
        file_url = os.path.join(conf('config', 'root_dir'), 'common', '测试上传文件.png')
        upload(file_url)
        try:
            self.by_xpath('//*[text()="添加附件成功！"]')
        except:
            return 'fail'
        else:
            print(dc[i] + '-- 附件上传成功')
            self.aF_define_btn.click()
            return 'success'

    # 招标项目备案新增
    def add_tenderProjRecord(self):
        self.switch_driver()
        HomePage(self.driver).enter_page('招标项目备案')
        self.add_btn.click()
        self.change_role('招标代理')
        self.choice_proj()  # 选择项目
        # self.bPI_bdMode_choice_btn('比选').click()  # 默认比选
        # self.bPI_bdWay_choice_btn('公开').click()  # 默认公开
        self.bPI_spDpCode_text_field.send_keys(random.randint(1000, 9999))  # 监督部门编码
        self.bPI_spDpName_text_field.send_keys('test-监督部门')
        self.bPI_adDpCode_text_field.send_keys(random.randint(1000, 9999))  # 审核部门编码
        self.bPI_spDpName_text_field.send_keys('test-审核部门')
        self.bPI_tdContentAndScope_text_field.send_keys('test-招标内容与范围-%s' % current_time())
        # 添加标段
        self.add_Lot()
        self.nextStep_btn.click()
        # 提交审核
        self.submitAudit_btn.click()
        # 附件信息上传
        for i in range(0, 9):
            assert self.add_file(i) == 'success'  # todo:测试-招标文件备案-上传附件功能
        self.fI_submit_audit_btn.click()
        self.fI_submit_define_btn.click()
        self.fI_operat_success_btn.click()
        try:
            self.by_xpath('//div[text()="%s"]' % self.projName)
        except:
            return 'fail'
        else:
            self.tdProjName = self.by_xpath('//div[text()="%s"]/../../td[@field="tdpjNo"]/div' % self.projName)
            return 'success'
