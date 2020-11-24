'''
    Title:“人脉管理系统”
    [Interpersonal relationship managerment system]

    本模块功能：  帮助类
    所属的项目分层：（后台）
    
    说明：
    Auther：sunkezhen
    Date:   
    Modify Date: 
'''
import sys

__all__ = ["Person"]


class Person(object):
    def __init__(self):
        __person_num = 0    # 人员编号
        __type = ""         # 联系人类别
        __name = ""         # 姓名
        __mobilPhone = ""   # 手机
        __weChat = ""       # 微信
        __email = ""        # 电子邮件
        __detailInfo = ""   # 详细信息

    @property
    def person_num(self):
        return self.__person_num
    @person_num.setter
    def person_num(self, per_num):
        self.__person_num = per_num

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type):
        self.__type = type

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def mobilPhone(self):
        return self.__mobilPhone
    @mobilPhone.setter
    def mobilPhone(self, phone):
        self.__mobilPhone = phone

    @property
    def weChar(self):
        return self.__weChar
    @weChar.setter
    def weChar(self, weChar):
        self.__weChar = weChar

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def detailInfo(self):
        return self.__detailInfo
    @detailInfo.setter
    def detailInfo(self, info):
        self.__detailInfo = info


def _unit_test():
    pass


if __name__ == "__main__":
    _unit_test()
