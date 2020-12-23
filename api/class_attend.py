import requests
from jsonpath import jsonpath
from testdatas import global_data as GD


class ClassAttend:
    def __init__(self, user, pwd):
        # 调用接口处理前置条件
        self.s = requests.Session()
        # 登录
        self.s.post("https://www.ketangpai.com/UserApi/login",
                    data={"email": user, "password": pwd})

    def close_class_attend(self):
        # 目前班级id写死，后期可以改成传参
        resp = self.s.get("https://www.ketangpai.com/AttenceApi/getNotFinishAttence?courseid=MDAwMDAwMDAwMLWGvZWH36do")
        if resp.json()['lists']:
            value = jsonpath(resp.json(), '$..id')
            # 调用关闭方法
            self.s.post('https://www.ketangpai.com/AttenceApi/overAttence', data={'id': f'{value[0]}'})

    def join_class(self, code):
        # 前置加入班级
        self.s.post('https://www.ketangpai.com/CourseApi/joinCourseByCode',
                    data={'code': code})


if __name__ == '__main__':
    from pprint import pprint
    a = ClassAttend(GD.student[0], GD.student[1])
    b = a.join_class('BG8W6H')
    pprint(b)
