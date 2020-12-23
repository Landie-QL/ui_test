from selenium.webdriver.common.by import By


class LoginPageLoc:
    # 用户名输入
    import_user = (By.XPATH, '//input[@name="account"]')
    # 密码输入
    import_pwd = (By.XPATH, '//input[@name="pass"]')
    # 登录
    login_button = (By.XPATH, '//div[contains(@class,"pt-login")]//a[text()="登录"]')