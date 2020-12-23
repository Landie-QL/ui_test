from pagelocators.class_page_loc import ClassPageLoc
from common.basepage import BasePage


class ClassPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.loc = ClassPageLoc()

    def work_button_click(self):
        self.element_click(self.loc.work_button, "首页—点击考勤")

    def in_the_iframe(self):
        self.switch_to_iframe(self.loc.work_iframe, "首页-进入iframe")

    def new_work_button_star(self):
        self.element_click(self.loc.new_work_button, "首页-考勤-新建考勤")
        self.element_click(self.loc.number_work, "首页-考勤-新建考勤-数字考勤")
        self.element_click(self.loc.start_work, "首页-考勤-新建考勤-数字考勤-开始考勤")

    def get_work_number(self):
        # 获取考勤数字
        work_number = ''
        eles = self.get_elements(self.loc.four_work_nember, "获取考勤数字")
        for ele in eles:
            work_number += self.get_element_text(ele, '获取1个考勤数字')
        return work_number

    def get_work_people(self):
        # 获取签到的人数
        number = self.get_element_text(self.loc.work_people, "获取考勤人数")
        return number

    def over_work(self):
        # 结束考勤
        self.element_click(self.loc.over_work, "点击结束考勤")
        # 点击确认结束考勤
        self.element_click(self.loc.confirm_over_work, "再次确认点击结束考勤")

    def sure_active(self):
        # 学生点击立即签到点击立即签到
        self.element_click(self.loc.sure_active, "学生账号点击立即签到")

    def imput_work_number(self, work_number):
        # 输入签到数字
        self.element_import(self.loc.input_work_nember, "学生输入签到数字", work_number)

    # def asster_work_number(self):
    #     # 判断元素是否存在进行断言
    #     try:
    #         self.wait_ele_visible(self.loc.asster_work, "签到断言")
    #     except:
    #         return False
    #     else:
    #         return True