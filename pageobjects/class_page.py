from pagelocators.class_page_loc import ClassPageLoc
from common.basepage import BasePage
from common.handle_random import random_data


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

    def input_work_number(self, work_number):
        # 输入签到数字
        self.element_input(self.loc.input_work_nember, "学生输入签到数字", work_number)

    def click_homework(self):
        # 点击作业
        self.element_click(self.loc.homework, "首页点击作业")

    def sure_homework(self):
        self.element_click(self.loc.people_homework, '首页点击发布个人作业')
        homework_name = random_data(5)
        self.element_input(self.loc.input_homework_name, "输入作业名称", homework_name)
        self.element_input(self.loc.input_homework_text, '输入作业描述', random_data(10))
        # 日期框输入当天日期
        self.js('js修改日期', self.loc.js_data)
        self.element_input(self.loc.max_score, '输入满分值', 100)
        self.element_click(self.loc.inmyswitch, '关闭是否查重')
        self.element_click(self.loc.sure_people_homework, "确认发布个人作业")
        return homework_name

    def click_need_upload_homework(self):
        self.element_click(self.loc.sure_homework_name, '点击老师刚发布的')

    def add_homework(self, file_path):
        self.element_click(self.loc.upload_homework, '点击添加作业文件')
        self.file_upload('选择需要上传的文件', file_path)

    def submit_homework(self):
        self.element_click(self.loc.submit_homework, '提交作业')

    def asster_submit_homework(self):
        try:
            self.wait_ele_visible(self.loc.submit_homework_ok, "等待上传成功出现")
        except:
            return False
        else:
            return True

    def in_no_read(self):
        self.element_click(self.loc.no_read, '点击未批改的作业')

    def in_read(self):
        self.element_click(self.loc.in_read, '点击进入批阅')

    def switch_to_new_windows(self):
        self.handlers_window_switch('切换进最后打开的那个窗口')

    def input_fraction(self, fraction):
        self.element_input(self.loc.input_fraction, '输入成绩', fraction)





    # def asster_work_number(self):
    #     # 判断元素是否存在进行断言
    #     try:
    #         self.wait_ele_visible(self.loc.asster_work, "签到断言")
    #     except:
    #         return False
    #     else:
    #         return True
