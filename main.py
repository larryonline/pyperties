
import lib.pyperties as pyperties




if __name__ == '__main__':
    pyp = pyperties.Pyperties("local.properties")

    dir(pyperties.__doc__)


    value = pyp.get('a.b.c')
