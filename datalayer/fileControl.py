"""
    Title:“人脉管理系统”
    [Interpersonal relationship managerment system]

    本模块功能：  文件读写控制类
    所属的项目分层：（后台）
    说明：
    Auther：sunkezhen
    Date:
    Modify Date:
"""
import sys

__all__ = ["FileControl"]


class FileControl(object):
    __instance = None       # 本类实例
    __init_flag = False     # 是否已经初始化

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        if self.__init_flag == False:
            self.__init_flag = True
            # 包名
            self.__pacage_name = "datalayer"
            # 文件访问路径
            if __name__ == "__main__":
                self.__file_PATH = "IRMS_Data.txt"
            else:
                self.__file_PATH = self.__pacage_name + "//IRMS_Data.txt"

    """ 文件写入 """
    def write_data_file(self,list_data):
        """
        写数据到文件
        :param list_data:需要写入的文件列表
        :return:无
        """
        self.__write_data_file(self.__file_PATH, list_data)

    def __write_data_file(self,file_path, list_data, file_encode = "ANSI"):
        """
        写数据到文件
        :param file_path:文件路径
        :param list_data:写入的内容（注： 写入纯文本信息，已“|”做数据间隔）
        :param file_encode:文件的编码函数
        :return:无
        """
        try:
            with open(file_path, 'w', encoding = file_encode) as wf:
                for row_data in list_data:
                    wf.write(row_data + "\n")
        except OSError as e:
            sys.stderr.write("[fileControl.py]/__write_data_file(), 文件操作出错！",e)

    """ 文件读出 """
    def read_data_file(self):
        return self.__read_data_file(self.__file_PATH)

    def __read_data_file(self, file_path, file_encode = "ANSI"):
        """
        从文件读取数据
        :param file_path:文件的读取路径
        :param file_encode:文件的编码格式
        :return:列表信息
        """
        list_read_info = [] # 读取文件的返回信息
        try:
            with open(file_path, 'r', encoding = file_encode) as rf:
                while True:
                    file_data = rf.readline()
                    if (not file_data):
                        break
                    list_read_info.append(file_data.strip())

        except OSError as e:
            sys.stderr.write("fileControl.py/__read_data_file/文件读取不成功！", e)
        else:
            return list_read_info


def _unit_test():
    print("单元测试")
    # # 写入测试
    # list1 = ["你好", "bbb", "ccc"]
    # FileControl().write_data_file(list1)

    # 读取测试
    f = FileControl()
    list_info = f.read_data_file()
    for item in list_info:
        print(item)

if __name__ == "__main__":
    _unit_test()
