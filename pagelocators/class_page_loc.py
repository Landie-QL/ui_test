from selenium.webdriver.common.by import By


class ClassPageLoc:
    # 考勤键
    work_button = (By.XPATH, '//span[text()="考勤"]/parent::a')
    # 考勤框的iframe
    work_iframe = (By.XPATH, '//iframe[contains(@id,"layui-layer-content")]')
    # 新建考勤
    new_work_button = (By.XPATH, '//a[text()="新建考勤"]')
    # 数字考勤
    number_work = (By.XPATH, '//div[@class="iconarea digit"]/div')
    # 开始考勤
    start_work = (By.XPATH, '//div[@id="new-perform"]//a[text()="开始考勤"]')
    # 四个考勤数字
    four_work_nember = (By.XPATH, '//div[@class="number-box"]//span')
    # 学生立即签到
    sure_active = (By.XPATH, '//a[text()="立即签到"]')
    # 签到输入框
    input_work_nember = (By.ID, 'phoneVer_modalAuthInput')
    # 考勤人数
    work_people = (By.XPATH, '//div[@id="number-attend"]//i[@class="ing"]')
    # 结束考勤
    over_work = (By.XPATH, '//div[@id="number-attend"]//a[text()="结束"]')
    # 确认结束考勤
    confirm_over_work = (By.XPATH, '//div[@id="end-attend"]//a[text()="结束"]')
    # 断言元素  //*[text()="学生通过以上数字完成签到"]
    asster_work = (By.XPATH, '//*[text()="学生通过以上数字完成签到"]')