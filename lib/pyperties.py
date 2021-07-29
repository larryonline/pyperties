import os.path
import re

'''
Pyperties

a simple .properties file parser
'''

def read_file(filepath, line_parser):
    if (os.path.isfile(filepath)):
        with open(filepath, 'r', encoding='utf-8') as f:
            line_no = 0
            while(True):
                line = f.readline()
                if (line == None or 0 == len(line)):
                    break
                else:
                    line_parser(line_no, line)
                    line_no += 1
    else:
        line_parser(err=FileNotFoundError(filepath))

# class Pyperties:
#     '''
#     Python .properties file detector
    
#     Structure of .properties file

#     data: {
#         "section1": {
#             "key1": {
#                 "key1.1": {
#                     "key1.1.1" : {
#                         value: "value is here"
#                     }
#                 }
#             },
#             "key2": ...
#         },
#         "section2": ...
#     }
#     '''
    
#     _filepath = None
#     _data = None
#     _section_cursor = None

#     def __init__(self, filepath):
#         self._filepath = filepath
#         pass

    
#     def readPropertiesFrom(self, filepath):
#         '''读取 .properties 文件'''
#         if (not os.path.isfile(filepath)):
#             raise FileNotFoundError("file \'%s\' not found"%(filepath))
#         else:
#             file = open(filepath)

#             while(True):
#                 line = file.readline()
#                 if (line == None or len(line) == 0):
#                     break

#                 print("line: %s "%(line))
#         pass

#     def writePropertiesInto(self, filepath, data):
#         '''写入 .properties 文件'''
#         pass

#     def findValueFrom(self, key, section='Default'):
#         if (self._data == None):
#             # load data from .properties
#             self._data = self.readPropertiesFrom(self._filepath)
#             pass
        
        

#         pass

#     def section(self, section_name): 
#         '''指定获取值的区域'''
#         self._section_cursor = section_name
#         return self


#     def get(self, key):
#         '''
#         获取参数键对应的字符串. 如果没有就返回None
#         '''

#         return self.findValueFrom(key, self._section_cursor)

#     def getNumber(self, key):
#         '''
#         获取参数键对应的数字, 如果没有返回0, 如果不是数字报错
#         '''
#         raise NotImplementedError()
#         return 0
    
#     def getString(self, key):
#         '''
#         获取参数键对应的字符串, 如果没有返回None
#         '''
#         raise NotImplementedError()
#         pass


#     def set(self, key, value):
#         '''
#         设置键值对
#         如果该键已有值则更新该值.
#         @param key 目标键, 可以是 xx.xx.xxx.xx 的方式. 最后和最前不能是 .
#         @param value 字符串
#         @param comment 注释说明. 默认是空值
#         '''
#         pass

#     def save(self):
#         pass


class PypertiesReader:

    SECTION_LINE = "^\\[(\w+)\\]\s*(#.*)"
    KV_LINE = "^(\w+(\\.\w+)+)\s*=\s*([^#]+)(#.*)?$"
    COMMENT_LINE = "^\s*#.*"

    _section_cursor = None
    _data = {}

    def __init__(self):
        pass

    def on(self, no=0, line=None, err=None):
        if (err != None):
            raise err

        line = line.strip()
        if (None == line):
            return

        print("[%s]%s"%(no, line))

        if (re.match(self.SECTION_LINE, line)):
            self._section_cursor = re.findall(self.SECTION_LINE, line)[0][0]
            # print("line[%s] is section line"%(no))
            # print("line[%s] got section: %s"%(no, self._section_cursor))
        elif (re.match(self.KV_LINE, line)):

            ret = line.split("=", 1)

            # ret = re.findall(self.KV_LINE, line)
            # print("line[%s] is kv line"%(no))
            print("line[%s] got kv: %s"%(no, ret))
        elif (re.match(self.COMMENT_LINE, line)):
            print("line[%s] is comment line"%(no))
        # else:
            # raise SyntaxError("syntax error at line[%s] \"%s\""%(no, line))


        



if __name__ == '__main__':
    
    reader = PypertiesReader()
    read_file("local.properties", reader.on)
