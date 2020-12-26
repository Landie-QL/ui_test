from selenium.webdriver.common.by import By
from datetime import datetime
from common.handle_data import Data

now_time = datetime.now().strftime("%Y-%m-%d")


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
    # 作业
    homework = (By.XPATH, '//div[@id="third-nav"]//a[text()="作业"]')
    # 发布个人作业
    people_homework = (By.XPATH, '//a[text()="发布个人作业"]')
    # 输入作业名称
    input_homework_name = (By.XPATH, '//input[@placeholder="作业名称"]')
    # 输入作业简介
    input_homework_text = (By.XPATH, '//div[@class="wangEditor-txt"]')
    # 日期框js语句
    js_data = 'var a = document.getElementsByClassName("date-txt")[0];' \
              f'a.value = "{now_time}"'
    # 满分值
    max_score = (By.XPATH, '//input[@class="maxScore fl"]')
    # 是否查重
    inmyswitch = (By.XPATH, '//div[@id="needcheckswitch"]/div')
    # 确认发布个人作业
    sure_people_homework = (By.XPATH, '//div[@class="opt-btn fr"]//a[text()="发布个人作业"]')

    # 发布后的作业名字
    # sure_homework_name = (By.XPATH, f'//a[text()={getattr(Data, "homewor_name")}')
    # 点击第一个上传
    sure_homework_name = (By.XPATH, '//a[text()="上传作业"]')
    # 上传作业
    upload_homework = (By.XPATH, '//a[@class="sc-btn webuploader-container"]')
    # 提交作业
    submit_homework = (By.XPATH, '//a[text()="提交"]')
    # 作业提交成功
    submit_homework_ok = (By.XPATH, '//div[text()="作业提交成功"]')
    # 未批改的作业
    no_read = (By.XPATH, '//a[text()="未批"]')
    # 修改对学生可见操作
    student_never_see_fraction = (By.XPATH, '//div[@class="hs-opt fr"]/span')
    # 改成可见
    student_can_see_fraction = (By.XPATH, '//a[text()="对学生显示成绩"]')
    # 进入批阅
    in_read = (By.XPATH, '//a[text()="进入批阅"]')
    # 成绩输入
    input_fraction = (By.XPATH, '//div[contains(@class,"edstate")]//input')
    # 保存成绩
    save_fraction = (By.XPATH, '//label[text()="成绩："]')
    # 保存成功
    save_ok = (By.XPATH, '//div[@id="show-tip"]/span')
    # 查看成绩
    see_fraction = (By.XPATH, '//a[text()="查看成绩"]')
    # 学生成绩
    student_fraction = (By.XPATH, '//p[@class="score fr"]/span')