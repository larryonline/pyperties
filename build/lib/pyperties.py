from genericpath import isfile
import os.path
import re
import sys

'''
Pyperties

a simple .properties file parser
'''

def read_properties_file(filepath, line_parser):
    if (os.path.isfile(filepath)):
        with open(filepath, 'r', encoding='utf-8') as f:
            line_no = 1
            while(True):
                line = f.readline()
                if (line == None or 0 == len(line)):
                    break
                else:
                    line_parser(line_no, line)
                    line_no += 1
    else:
        line_parser(err=FileNotFoundError(filepath))

class PypertiesReader:

    _section_cursor = None
    _data = {}

    def __init__(self):
        pass

    def get_section(self, section):
        if (None == section):
            return self._data
        else:
            ret = self._data.setdefault(section, {})
            return ret

    def on(self, no=0, line=None, err=None):
        if (err != None):
            raise err

        # ignore empty line
        if (None == line or re.match("^\s+$", line)):
            return

        if (re.match("^\s*\\[\w+\\]\s*(#.*)?$", line)):
            self.on_section_line(line)
        elif (re.match("^\s*#.*$", line)):
            self.on_comment_line(line)
        elif (re.match("^\s*\w+(\\.\w+)+\s*=\s*.*$", line)):
            self.on_kv_line(line)
        else:
            raise SyntaxError("syntax error at line[%s]: \"%s\""%(no, line))

    def on_section_line(self, line):
        found = re.findall("^\s*\\[(\w+)\\]\s*(#.*)?$", line)
        self._section_cursor = found[0][0]
        # print("section: %s" % (self._section_cursor))

    def on_comment_line(self, line):
        # ignore comment line
        pass

    def on_kv_line(self, line):
        couple = line.split("=", 1)
        key = couple[0].strip()
        value = couple[1].strip()

        if (None == self._section_cursor):
            self._data[key] = value
        else:
            section = self._data.setdefault(self._section_cursor, {})
            section[key] = value
        pass

    def get_data(self):
        return self._data


def load(filepath):
    if (None == filepath or not os.path.isfile(filepath)):
        raise RuntimeError("\n\nyou should invoke script like this: `python pyperties.py <properties_file_path>`\n\n")

    reader = PypertiesReader()
    read_properties_file(filepath, reader.on)

    print(reader.get_data())


if __name__ == '__main__':
    
    filepath = sys.argv[1]
    if (None == filepath or not os.path.isfile(filepath)):
        raise RuntimeError("\n\nyou should invoke script like this: `python pyperties.py <properties_file_path>`\n\n")

    reader = PypertiesReader()
    read_properties_file(filepath, reader.on)

    print(reader.get_data())