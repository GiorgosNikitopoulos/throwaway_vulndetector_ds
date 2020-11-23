import glob
import re
import shutil
import os


def main():
    for filepath in glob.glob('functions_test/**.func', recursive = True):
        special_name = 'common_name'
        #print(i)
        name = filepath.rsplit('/')[1]
        f = open(filepath, "r")
        entire_text = f.read()
        p = re.compile('(CWE.+_)?good(G2B\d*|B2G\d*)?Source(_[a-z])?')
        entire_text = p.sub(special_name, entire_text)
        p = re.compile('(CWE.+_)?good(G2B\d*|B2G\d*)?Sink(_[a-z])?')
        entire_text = p.sub(special_name, entire_text)
        p = re.compile('(CWE.+_)?badSource(_[a-z])?')
        entire_text = p.sub(special_name, entire_text)
        p = re.compile('(CWE.+_)?badSink(_[a-z])?')
        entire_text = p.sub(special_name, entire_text)

        p = re.compile('(CWE.+_)?((helperGood(G2B|B2G)?\d*)|(good(G2B|B2G)?\d*VaSink[BG]?))')
        entire_text = p.sub(special_name, entire_text)
        p = re.compile('good(\d+|G2B\d*|B2G\d*)')
        entire_text = p.sub(special_name, entire_text)
        p = re.compile('(CWE.+_)?(helperBad|badVaSink[BG]?)')
        entire_text = p.sub(special_name, entire_text)
        p = re.compile('(CWE.*_)?bad')
        entire_text = p.sub(special_name, entire_text)
        p = re.compile('(CWE.*_)?good')
        entire_text = p.sub(special_name, entire_text)

        f2 = open('common_func/' + name, 'w')
        f2.write(entire_text)
        f2.close()
        f.close()


if __name__ == '__main__':
    main()
