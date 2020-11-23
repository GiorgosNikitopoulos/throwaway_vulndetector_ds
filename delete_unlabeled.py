import glob
import re
import shutil
import os


def main():
    i = 0
    k = 0
    for filepath in glob.glob('functions_test/**.func', recursive = True):
        f = open(filepath, 'r')
        text = f.read()
        lstripped_text = text.lstrip()
        first_line = lstripped_text.splitlines()[0]
        cl_first_line = first_line.lstrip().rstrip()
        temp = cl_first_line.rsplit('(', 1)[0]
        function_name = temp.rsplit(' ', 1)[1]
        if(function_name.count('bad') == 0 and function_name.count('good') == 0):
            f.close()
            os.remove(filepath)
            continue
        f.close()
if __name__ == '__main__':
    main()
