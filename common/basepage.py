from time import sleep
from datetime import datetime
import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver, WebElement
from pywinauto.keyboard import send_keys

from common.handle_log import log
from common.handle_path import screenshot_path


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def wait_ele_visible(self, loc, png_doc, timeout=20, poll_frequency=0.5):
        """
        显示等待封装
       :param loc: element元素对象
       :param png_doc:操作描述
       :param timeout: 最长等待时间
       :param poll_frequency: 轮寻时间
       :return:
       """
        log.info(f'等待 {loc} 元素的出现。')
        try:
            wait = WebDriverWait(self.driver, timeout, poll_frequency)
            wait.until(EC.visibility_of_element_located(loc))
        except:
            log.exception(f'元素等待失败。')
            # 截图
            self.__screenshot(png_doc)
            raise

    def _get_element(self, loc, png_doc):
        log.info(f'查找 {loc} 元素。')
        try:
            ele = self.driver.find_element(*loc)
            return ele
        except:
            log.exception('元素查找失败。')
            # 截图
            self.__screenshot(png_doc)
            raise

    def get_elements(self, loc, png_doc, timeout=20, poll_frequency=0.5):
        # 等待元素可见
        self.wait_ele_visible(loc, png_doc, timeout, poll_frequency)
        sleep(1)
        log.info(f'查找 {loc} 元素。')
        try:
            eles = self.driver.find_elements(*loc)
            return eles
        except:
            log.exception('元素查找失败。')
            # 截图
            self.__screenshot(png_doc)
            raise

    def element_click(self, loc, png_doc, timeout=20, poll_frequency=0.5):
        """
        元素点击操作封装。
        :param loc: 元素对象
        :param png_doc: 操作描述
        :param timeout:
        :param poll_frequency:
        :return:
        """
        log.info(f'当前动作为：{png_doc}')
        self.wait_ele_visible(loc, png_doc, timeout, poll_frequency)
        ele = self._get_element(loc, png_doc)
        log.info(f'需要点击的元素是:{ele}。')
        try:
            ele.click()
        except:
            log.exception('元素点击失败')
            # 截图
            self.__screenshot(png_doc)
            raise

    def element_input(self, loc, png_doc, *value, timeout=20, poll_frequency=0.5):
        log.info(f'当前动作为：{png_doc}')
        self.wait_ele_visible(loc, png_doc, timeout, poll_frequency)
        ele = self._get_element(loc, png_doc)
        log.info(f'需要输入的元素是:{ele}。')
        try:
            ele.send_keys(*value)
        except:
            log.exception('元素输入失败')
            # 截图
            self.__screenshot(png_doc)
            raise

    def __screenshot(self, png_doc):
        """
        截图功能
        :param png_doc: 描述
        :return:
        """
        # 当前时间
        new_time = datetime.now().strftime("%Y-%m-%d %H：%M：%S")
        # 文件名
        file_name = f"{png_doc}_{new_time}.png"
        # 截图路径
        scr_path = os.path.join(screenshot_path, file_name)
        log.info(f'开始截图，图片路径在 {scr_path}。')
        try:
            self.driver.save_screenshot(scr_path)
        except:
            log.exception('图片截取失败！！')
            raise

    def switch_to_iframe(self, loc, png_doc, timeout=20, poll_frequency=0.5):
        # 进入iframe
        log.info(f'需要进入的iframe为：{loc}')
        try:
            WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.frame_to_be_available_and_switch_to_it(loc))
            sleep(1)
        except:
            log.exception('元素输入失败')
            # 截图
            self.__screenshot(png_doc)
            raise

    def get_element_text(self, loc, png_doc, timeout=20, poll_frequency=0.5):
        """
        获取元素文本
        :param loc:
        :param png_doc:
        :param timeout:
        :param poll_frequency:
        :return:
        """
        log.info(f'当前动作为：{png_doc}')
        if isinstance(loc, WebElement):
            # 判断传入的是否已经是element对象
            ele = loc
        else:
            # 等待元素可见
            self.wait_ele_visible(loc, png_doc, timeout, poll_frequency)
            ele = self._get_element(loc, png_doc)
            log.info(f'需要获取文本的元素是:{ele}。')
        try:
            value = ele.text
            log.info(f"获取到的文本是:{value}")
            return value
        except:
            log.exception('文本获取失败。')
            # 截图
            self.__screenshot(png_doc)
            raise

    def get_element_attr(self, loc, png_doc, value_name, timeout=20, poll_frequency=0.5):
        log.info(f'当前动作为：{png_doc}')
        if isinstance(loc, WebElement):
            # 判断传入的是否已经是element对象
            ele = loc
        else:
            # 等待元素可见
            self.wait_ele_visible(loc, png_doc, timeout, poll_frequency)
            ele = self._get_element(loc, png_doc)
            log.info(f'需要获取文本的元素是:{ele}。')
        try:
            value = ele.get_attribute(value_name)
            log.info(f"获取到的属性是:{value}")
            return value
        except:
            log.exception('属性获取失败。')
            # 截图
            self.__screenshot(png_doc)
            raise

    def handlers_window_switch(self, png_doc, win=-1):
        """
        窗口句柄切换
        :param png_doc:
        :param win: 默认进入最后打开的窗口
        :return:
        """
        log.info(f'当前动作为：{png_doc}')
        try:
            handles = self.driver.window_handles
            self.driver.switch_to.window(handles[win])
            sleep(2)
        except:
            log.exception('窗口切换失败。')
            # 截图
            self.__screenshot(png_doc)
            raise

    def js(self, png_doc, js, element=None):
        """
        js操作
        :param png_doc:
        :param js: js语句
        :param element: 元素对象
        :return:
        """
        log.info(f'当前动作为：{png_doc}')
        try:
            if element:
                self.driver.execute_script(js, self._get_element(element, png_doc))
            else:
                self.driver.execute_script(js)
        except:
            log.exception('窗口切换失败。')
            # 截图
            self.__screenshot(png_doc)
            raise

    def file_upload(self, png_doc, file_path):
        """
        文件上传封装
        :param file_path:
        :return:
        """
        log.info(f'当前动作为：{png_doc}')
        try:
            sleep(2)
            send_keys(file_path)
            send_keys('{VK_RETURN}')
        except:
            log.exception('文件上传失败。')
            # 截图
            self.__screenshot(png_doc)
            raise