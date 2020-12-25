from time import sleep
import pytest

from selenium.webdriver.remote.webdriver import WebDriver
from pageobjects.login_page import LoginPage
from pageobjects.index_page import IndexPage
from pageobjects.class_page import ClassPage
from common.handle_data import Data
from testdatas import global_data as GD
from api.class_attend import ClassAttend
from common.handle_log import log


@pytest.fixture(scope='class')
def close_class_attend():
    # 调用接口关闭未签到
    ca = ClassAttend(GD.teacher[0], GD.teacher[1])
    ca.close_class_attend()


@pytest.mark.usefixtures('close_class_attend')
class TestWorkAttend:

    def test_teacher_start_attend(self, set_driver: WebDriver):
        driver = set_driver
        # 登录
        LoginPage(driver).login(*GD.teacher)
        # 选择班级并进入
        IndexPage(driver).enter_class_by_name(GD.class_name)
        cp = ClassPage(driver)
        # 点击考勤
        cp.work_button_click()
        # 进入iframe
        cp.in_the_iframe()
        # 点击新建考勤
        sleep(1)
        cp.new_work_button_star()
        # 获取签到码
        sleep(1)
        work_number = cp.get_work_number()
        setattr(Data, "work_number", work_number)
        # assert cp.asster_work_number() is True

    @pytest.mark.parametrize("students_list", GD.students_list)
    def test_student_sign_attend(self, set_driver: WebDriver, students_list):
        driver = set_driver
        # 登录
        LoginPage(driver).login(*students_list)
        # 选择班级并进入
        sleep(1)
        IndexPage(driver).enter_class_by_name(GD.class_name)
        # 刷新
        driver.refresh()
        # 点击立即签到
        sleep(1)
        cp = ClassPage(driver)
        cp.sure_active()
        # 输入签到码
        sleep(1)
        cp.input_work_number(getattr(Data, "work_number"))
        sleep(5)

    def test_teacher_over_atted(self, set_driver: WebDriver):
        driver = set_driver
        # 登录
        LoginPage(driver).login(*GD.teacher)
        # 选择班级并进入
        IndexPage(driver).enter_class_by_name(GD.class_name)
        cp = ClassPage(driver)
        # 点击考勤
        cp.work_button_click()
        # 进入iframe
        cp.in_the_iframe()
        # 获得考勤人数
        student_number = cp.get_work_people()
        # 结束考勤
        cp.over_work()
        log.info(f'当前考勤人数：{student_number}')
        log.info(f'参与考勤学生人数：{GD.students_list}')
        assert int(student_number) == len(GD.students_list)
        sleep(5)
