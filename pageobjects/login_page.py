from selenium.webdriver.remote.webdriver import WebDriver

from pagelocators.login_page_loc import LoginPageLoc
from common.basepage import BasePage


class LoginPage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.loc = LoginPageLoc()

    # 登录功能
    def login(self, user, pwd):
        self.element_input(self.loc.import_user, "输入用户名", user)
        self.element_input(self.loc.import_pwd, "输入密码", pwd)
        self.element_click(self.loc.login_button, "点击登录")

