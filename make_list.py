import glob
import re
import subprocess

def main():
    f = open('name_list.txt', 'w')
    for filepath in glob.glob('functions_test/**.func', recursive = True):
        f.write(filepath.split('/')[1])
        f.write('\n')

    print('Done')

if __name__ == '__main__':
    main()
