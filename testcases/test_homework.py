from time import sleep
import pytest

from selenium.webdriver.remote.webdriver import WebDriver
from pageobjects.login_page import LoginPage
from pageobjects.index_page import IndexPage
from pageobjects.class_page import ClassPage
from common.handle_data import Data
from testdatas import global_data as GD
from common.handle_log import log



class TestHomeWork:

    def test_teacher_relese_homework(self, set_driver: WebDriver):
        driver = set_driver
        # 登录
        LoginPage(driver).login(*GD.teacher)
        # 选择班级并进入
        sleep(1)
        IndexPage(driver).enter_class_by_name(GD.class_name)
        cp = ClassPage(driver)
        # 点击作业
        cp.click_homework()
        # 发布作业
        cp.sure_homework()
        # homewor_name = cp.sure_homework()
        # setattr(Data, 'homewor_name', homewor_name)

    def test_student_submit_homework(self, set_driver: WebDriver):
        driver = set_driver
        # 登录
        LoginPage(driver).login(*GD.student)
        # 选择班级并进入
        sleep(1)
        IndexPage(driver).enter_class_by_name(GD.class_name)
        cp = ClassPage(driver)
        # 点击作业
        cp.click_homework()
        # 点击刚发布的作业
        cp.click_need_upload_homework()
        # 点击添加作业文件
        cp.add_homework(GD.file_path)
        # 点击提交
        sleep(2)
        cp.submit_homework()
        assert cp.asster_submit_homework()

    def test_teacher_read_homework(self, set_driver: WebDriver):
        driver = set_driver
        # 登录
        LoginPage(driver).login(*GD.teacher)
        # 选择班级并进入
        sleep(1)
        IndexPage(driver).enter_class_by_name(GD.class_name)
        cp = ClassPage(driver)
        # 点击作业
        cp.click_homework()
        # 点击未批改的作业
        cp.in_no_read()
        # 点击进入批阅
        cp.in_read()
        # 切换窗口
        cp.switch_to_new_windows()
        # 输入成绩
        cp.input_fraction('100')



