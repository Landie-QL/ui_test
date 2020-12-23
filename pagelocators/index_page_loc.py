from selenium.webdriver.common.by import By


class IndexPageLoc:
    # 头像元素
    portrait = (By.XPATH, '//img[@class="avatar"]')
    # 班级链接
    class_link = (By.XPATH, '//a[text()="{}"]')