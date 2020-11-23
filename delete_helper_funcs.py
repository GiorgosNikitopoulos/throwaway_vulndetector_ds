import glob
import re
import shutil


def main():
    i = 0
    k = 0
    for i in range(374661):
        f = open('functions/' + str(i) + '.func', 'r')
        text = f.read()
        lstripped_text = text.lstrip()
        first_line = lstripped_text.splitlines()[0]
        cl_first_line = first_line.lstrip().rstrip()
        temp = cl_first_line.rsplit('(', 1)[0]
        function_name = temp.rsplit(' ', 1)[1]
        print(function_name)
        f.close()
if __name__ == '__main__':
    main()
