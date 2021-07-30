from genericpath import isfile
import os.path
import pyperties as _pyperties

def load(filepath): 

    if (None == filepath or not os.path.isfile(filepath)):
        raise FileExistsError("properties file not exist: \"%s\""%(filepath))

    reader = _pyperties.PypertiesReader()
    _pyperties.read_properties_file(filepath, reader.on)
    return reader.get_data()