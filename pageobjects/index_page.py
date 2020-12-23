from selenium.webdriver.remote.webdriver import WebDriver

from pagelocators.index_page_loc import IndexPageLoc
from common.basepage import BasePage


class IndexPage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.loc = IndexPageLoc()

    # 判断头像元素是否存在
    def portrair_is_exist(self):
        try:
            self.wait_ele_visible(self.loc.portrait, "等待头像元素出现")
        except:
            return False
        else:
            return True

    def enter_class_by_name(self, class_name):
        # 根据班级名字进入班级
        new_class_link = self.change_class_name(self.loc.class_link, class_name)
        self.element_click(new_class_link, "根据班级名字进入班级")

    def change_class_name(self, loc: tuple, new_value):
        # 替换所需要的element表达式
        new_loc = loc[1].format(new_value)
        return (loc[0], new_loc)