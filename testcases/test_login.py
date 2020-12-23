from time import sleep
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from pageobjects.login_page import LoginPage
from pageobjects.index_page import IndexPage



class Test_Login:

    @pytest.mark.smokey
    def test_login(self, set_driver:WebDriver):
        # 实例化driver对象
        driver = set_driver
        # 登录
        LoginPage(driver).login('18800237392', 'QIlei62198491')
        # 断言
        sleep(1)
        assert IndexPage(driver).portrair_is_exist() == True
        assert driver.current_url == 'https://www.ketangpai.com/Main/index.html'

