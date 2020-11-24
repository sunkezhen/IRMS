"""
    Title:“人脉管理系统”
    [Interpersonal relationship managerment system]

    本模块功能：  数据处理工厂（Facade 设计模式的，中枢文件）
    所属的项目分层：（前台/后台）

    说明：
    Auther：sunkezhen
    Date:
    Modify Date:
"""
from datalayer.helper import Person
from datalayer.fileControl import FileControl


__all__ = ["DataDealFactory"]


class DataDealFactory(object):
    __instance = None       # 本类实例
    __init_flag = False     # 是否已经初始化

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        if self.__init_flag == False:
            self.__init_flag = True
            # 实体类集合（缓存项目中所有人员的信息）
            self.__list_person_array = []


    """ 查询人员信息 """
        # 默认所有查询
        # 查询指定人员信息
        # 当前所有人员的最大编号
        # 人员信息列表

    """ 提供后台的操作方法（存储用户信息/删除信息） """
        # 存储联系人信息
        # 删除联系人信息
    """ 内部文件读写转换 """
    # Person实体类转字符串
    def __Person_to_string(self, per):
        """
        Person 实体类转字符串
        :param per: 实体类对象
        :return: 字符串
        """
        str_personInfo = ""
        list_personInfo = []
        #per = Person()
        list_personInfo.append(str(per.person_num) + "|")
        list_personInfo.append(per.type + "|")
        list_personInfo.append(per.name + "|")
        list_personInfo.append(per.mobilPhone + "|")
        list_personInfo.append(per.weChar + "|")
        list_personInfo.append(per.email + "|")
        list_personInfo.append(per.detailInfo + "|")
        str_personInfo = "".join(list_personInfo)
        return str_personInfo

    # 字符串转Person实体类
    def __string_to_person(self,str):
        """
        字符串转Person实体类
        :param str: 字符串
        :return: 实体类
        """
    # 读取文件中的数据，存储到本实例中的“人员信息列表”[__list_person_array]

    def testOnly(self):
        # 字符串转Person对象
        str = "1001|同学|张强|18600256686|zhang520|zhangqiang@263.com|小学非常要好的同学"
        perobj = Person()
        perobj = DataDealFactory().__Person_to_string()
        print(perobj)


def _unit_test():
    print("dataDealFactory 单元测试")
    DataDealFactory().testOnly()


if __name__ == "__main__":
    _unit_test()
