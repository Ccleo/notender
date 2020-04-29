from page.home_page import HomePage
from common.function import current_time, conf, upload
import random, os, datetime,time
from dateutil.relativedelta import relativedelta


class BidDocRecordPage(HomePage):

    @property
    def tdInfo_choice_btn(self):
        return self.by_xpath('//*[@id="addtdpjNameTd"]/span/a')

    @property
    def proj_list(self):
        return self.by_xpath('//div[text()="%s"]' % self.tdProjName)

    @property
    def proj_choice_btn(self):
        return self.by_xpath('//*[@id="tenderProjDlgBtn"]/a[1]')

    # 招标文件(正本)份数
    @property
    def bdrInfo_docOriginaNum_text_field(self):
        return self.by_xpath('//input[@name="docOriginaNum"]/../input')

    # 招标文件(副本)份数
    @property
    def bdrInfo_docDuplicateNum_text_field(self):
        return self.by_xpath('//input[@name="docDuplicateNum"]/../input')

    # 招标文件工本费
    @property
    def bdrInfo_docCost_text_field(self):
        return self.by_xpath('//input[@name="docCost"]/../input')

    # 图纸及参考资料费用
    @property
    def bdrInfo_referencesCost_text_field(self):
        return self.by_xpath('//input[@name="referencesCost"]/../input')

    def bdrInfo_docGetStarttime_choice(self):
        current_time('选择招标文件发售时间')
        self.by_xpath('//input[@name="docGetStarttime"]/../span/a').click()
        self.by_xpath("//a[text()='今天']").click()

    def bdrInfo_docGetDeadline_choice(self):
        current_time('选择招标文件发售截止时间')
        self.by_xpath('//input[@name="docGetDeadline"]/../span/a').click() # 点击日历控件按钮
        y = (datetime.date.today() + relativedelta(days=+1)).year
        m = (datetime.date.today() + relativedelta(days=+1)).month
        d = (datetime.date.today() + relativedelta(days=+1)).day
        ymd = '%s,%s,%s' % (y,m,d)
        self.by_xpath('//td[@abbr="%s"]' % ymd).click()
        self.by_xpath('/html/body/div[13]/div/div[3]/table/tbody/tr/td[2]/a').click()

    # 选择项目
    def tdInfo_choice_proj(self):
        self.tdInfo_choice_btn.click()
        self.proj_list.click()
        self.proj_choice_btn.click()

    # 新增招标文件备案
    def add_bidDocRecord(self):
        self.excute_script(self.add_btn)
        self.tdInfo_choice_proj()
        self.bdrInfo_docCost_text_field.send_keys('0.01')
        self.bdrInfo_docGetStarttime_choice()
        self.bdrInfo_docGetDeadline_choice()
